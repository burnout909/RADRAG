# RADRAG

**RADRAG: Retrieval-Augmented Generation-based Standardization of Radiology Reports**  
This project was developed for the **2025 AGI Hackathon**, hosted by **YBIGTADS** and **Upstage**.

## Project Overview

RADRAG is a **Retrieval-Augmented Generation (RAG)** based tool that standardizes free-text radiology reports into **SNOMED CT** concepts.  
It is designed for use in **clinical settings**, integrating external terminology knowledge and extraction models to enable precise concept mapping.

## Preparing the Dataset

### 1. Download SNOMED CT

- Download the [SNOMED CT International version](https://www.nlm.nih.gov/healthit/snomedct/index.html) from the UMLS website.
- Registration and license approval are required.
- Once downloaded, store the vocabulary files in the `data/` directory.
⚠️ The SNOMED CT files are **not included** in this repository due to licensing restrictions.

### 2. Flatten SNOMED CT Hierarchy

SNOMED CT is hierarchical by design. To enable effective embedding and search, a flat version of the terminology is needed:

```bash
python process_data.py make-flattened-terminology
```
### 3. Generate SNOMED CT Dictionary
This step creates a dictionary file containing terms related to the flattened concept list:

```bash
python process_data.py generate-sct-dictionary --output-path assets/newdict_snomed.txt
```

## Building the FAISS Index
We use sentence-transformers/all-MiniLM-L12-v2 as our embedding model.
Concepts are grouped by concept_type_subset, and separate FAISS indices are built for each group.

Relevant code: [rag/generate_snomedct_faiss.py](https://github.com/burnout909/RADRAG/blob/main/rag/generate_snomedct_faiss.py
)

## Free-text Extraction & Matching
We use the **Upstage Information Extraction API**, which supports key-based entity extraction.
Keys are aligned with the concept_type_subset definitions used for SNOMED CT.

The extracted results are mapped to the nearest concepts in the corresponding FAISS index.

Relevant code: [rag/extraction.py](https://github.com/burnout909/RADRAG/blob/main/rag/extraction.py)

## 🎛 Gradio-based Prototype
We implemented a web-based prototype using Gradio for interactive testing and visualization.
Code directory: gradio/

Live demo (temporary): https://320d3ce3b3fd23f293.gradio.live/playground
![Header 71](https://github.com/user-attachments/assets/10e9d231-a25c-4976-88f5-34679b3f2c7b)


⚠️ Deployment to Hugging Face Spaces is pending due to licensing restrictions.
