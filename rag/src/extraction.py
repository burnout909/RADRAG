import os 
import json
import requests
import pandas as pd 
from sentence_transformers import SentenceTransformer
import faiss
from tqdm import tqdm
from dotenv import load_dotenv
import base64
from openai import OpenAI
from fpdf import FPDF
import textwrap

def text_to_pdf(text, pdf_path="user_input.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)

    # 텍스트를 줄바꿈 포함하여 100자 단위로 자름
    lines = []
    for line in text.split('\n'):
        wrapped = textwrap.wrap(line, width=100)
        lines.extend(wrapped if wrapped else [" "])  # 빈 줄 유지

    # 각 줄을 PDF에 cell로 출력
    for line in lines:
        pdf.cell(0, 10, line, ln=True)

    pdf.output(pdf_path)
    return pdf_path

# Read file
def encode_to_base64(file_path):
    with open(file_path, 'rb') as f:
        file_bytes = f.read()
        base64_encoded = base64.b64encode(file_bytes).decode('utf-8')
        return base64_encoded

def load_faiss_and_mapping(concept_type, base_path):
    safe_concept_type = concept_type.strip().lower().replace("/", "_").replace(" ", "_")
    index_path = os.path.join(base_path, f"faiss_index_{safe_concept_type}.index")
    mapping_path = os.path.join(base_path, f"snomed_id_mapping_{safe_concept_type}.tsv")

    index = faiss.read_index(index_path)
    mapping_df = pd.read_csv(mapping_path, sep="\t")

    return index, mapping_df

def match_text_to_snomed(input_text, index, mapping_df, model, top_k=1):
    embedding = model.encode([input_text])
    D, I = index.search(embedding, top_k)

    results = []
    for idx in I[0]:
        concept_id = mapping_df.iloc[idx]["concept_id"]
        concept_name = mapping_df.iloc[idx]["concept_name"]
        results.append((concept_id, concept_name))
    return results

def mapping(output_json, ASSETS_PATH, model):
    output_rows = []
    for hierarchy, description in output_json.items():
        if not description.strip():
            output_rows.append({
                "Hierarchy": hierarchy,
                "Input Description": "No description provided.",
                "Match #": "-", "Concept Name": "-", "Concept ID": "-"
            })
            continue

        try:
            index, mapping_df = load_faiss_and_mapping(hierarchy, ASSETS_PATH)
            matches = match_text_to_snomed(description, index, mapping_df, model, top_k=3)  # top 3 반환

            if matches:
                for i, (concept_id, concept_name) in enumerate(matches, 1):
                    output_rows.append({
                        "Hierarchy": hierarchy,
                        "Input Description": description,
                        "Match #": i,
                        "Concept Name": concept_name,
                        "Concept ID": concept_id,
                    })
            else:
                output_rows.append({
                    "Hierarchy": hierarchy,
                    "Input Description": description,
                    "Match #": "-", "Concept Name": "No match found", "Concept ID": "-"
                })

        except FileNotFoundError:
            output_rows.append({
                "Hierarchy": hierarchy,
                "Input Description": description,
                "Match #": "-", "Concept Name": "FAISS file not found", "Concept ID": "-"
            })
        except Exception as e:
            output_rows.append({
                "Hierarchy": hierarchy,
                "Input Description": description,
                "Match #": "-", "Concept Name": f"Error: {str(e)}", "Concept ID": "-"
            })
        
                # DataFrame으로 정리해서 출력
    df_output = pd.DataFrame(output_rows)
    return df_output