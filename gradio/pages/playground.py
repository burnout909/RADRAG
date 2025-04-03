import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))            
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))       
rag_path = os.path.join(project_root, "rag")              
sys.path.append(rag_path)

from dropdown import render_dropdown_box
import gradio as gr
import base64
from extraction import *


def encode_image_to_base64(path):
    with open(path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode('utf-8')
        return f"data:image/png;base64,{encoded}"

def build_result_page():
    with gr.Blocks() as result_app:
        with gr.Row():
            with gr.Column(scale=1):
                render_dropdown_box("Patient")

                gr.HTML("""
                    <div class="info-box">
                        <style>
                            .info-box {
                                background-color: white;
                                border-radius: 12px;
                                box-shadow: 0px 3px 8px rgba(0,0,0,0.05);
                                font-family: Arial, sans-serif;
                                overflow: hidden;
                                width: 280px;
                                margin-top: 10px;
                            }
                            .info-box .title {
                                font-weight: bold;
                                padding: 12px 16px;
                                font-size: 15px;
                                border-bottom: 1px solid #ddd;
                                background-color: #f8f8f8;
                            }
                            .info-box .item {
                                padding: 12px 16px;
                                font-size: 14px;
                                border-bottom: 1px solid #ddd;
                                cursor: pointer;
                                background-color: white;
                            }
                            .info-box .item:hover {
                                background-color: #f0f0f0;
                            }
                            .info-box .item:last-child {
                                border-bottom: none;
                            }
                        </style>
                        <div class="item"><strong>Patient Information</strong></div>
                        <div class="item">Medical History</div>
                        <div class="item">Medications</div>
                        <div class="item">All Visits</div>
                    </div>
                """)
            with gr.Column(scale=1):
                gr.HTML("""
                    <style>
                        .card {
                            background-color: #ffffff;
                            border-radius: 16px;
                            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.08);
                            padding: 24px;
                            width: 368px;
                            height: 304px;
                            font-family: 'Arial', sans-serif;
                            color: #333333;
                            margin: 10px;
                            box-sizing: border-box;
                        }
                        .card h3 {
                            margin: 0 0 12px 0;
                            font-size: 17px;
                            font-weight: 600;
                        }
                    </style>
                    <div class='card'>
                        <h3>Patient Information</h3>
                        <p><strong>Name:</strong> Lola Greenwood</p>
                        <p><strong>Patient ID:</strong> 12334</p>
                        <p><strong>Gender:</strong> female</p>
                        <p><strong>Nationality:</strong> USA</p>
                        <p><strong>Pay Type:</strong> IP</p>
                        <p><strong>Insurance ID:</strong> 2123767</p>
                        <p><strong>Sub Insurance ID:</strong> 222388</p>
                    </div>
                """)
            with gr.Column(scale=1):
                gr.HTML("""
                    <style>
                        .card_empty {
                            border-radius: 16px;
                            padding: 24px;
                            width: 368px;
                            height: 304px;
                            font-family: 'Arial', sans-serif;
                            color: #333333;
                            margin: 10px;
                            box-sizing: border-box;
                            box-shadow:none;
                        }
                    </style>
                    <div class='card_empty'>
                    </div>
                """)

        with gr.Row():
            render_dropdown_box("Procedures", ["0001.dcm", "0002.dcm", "0003.dcm"])

            xray_image = encode_image_to_base64("img/image.png")
            gr.HTML(f"""
                <style>
                    .card {{
                        background-color: #ffffff;
                        border-radius: 16px;
                        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.08);
                        padding: 24px;
                        width: 368px;
                        height: 304px;
                        font-family: 'Arial', sans-serif;
                        color: #333333;
                        margin: 10px;
                        box-sizing: border-box;
                    }}
                    .card h3 {{
                        margin: 0 0 12px 0;
                        font-size: 17px;
                        font-weight: 600;
                    }}
                </style>
                <div class='card'>
                    <img src="{xray_image}" style="width: 100%; height: auto; max-height: 265px; object-fit: contain; border-radius: 8px;" />
                </div>
            """)

            gr.HTML("""
                <div style='background-color: #ffffff; border-radius: 16px; box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.08); padding: 20px; width: 368px; height: 304px; font-family: Arial, sans-serif; color: #333333; margin: 10px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between;'>
                    <div>
                        <h3 style='margin: 0 0 12px 0; font-size: 17px; font-weight: 600;'>DICOM Metadata</h3>
                        <table style='width:100%; font-size: 12.5px; border-collapse: collapse; line-height: 1.3;'>
                            <tr><td>Modality</td><td>DX</td></tr>
                            <tr><td>Study Instance UID</td><td>1.2.840.113...</td></tr>
                            <tr><td>SOP Instance UID</td><td>1.2.840.113...</td></tr>
                            <tr><td>Acquisition Date</td><td>2023-04-01</td></tr>
                            <tr><td>kVp</td><td>120</td></tr>
                            <tr><td>View Position</td><td>AP</td></tr>
                        </table>
                    </div>
                    <div style='margin-top: 8px; color: #007AFF; font-weight: bold; font-size: 13.5px; text-decoration: underline; cursor: pointer; align-self: center;' onclick="alert('Viewing all tags...')">
                        Find Tag
                    </div>
                </div>
            """)
        with gr.Row():
                with gr.Column(scale=1):
                    gr.Interface(
                    fn=extraction_and_mapping,
                    inputs=gr.Textbox(
                        label ="clinical notes",
                        lines=15,
                        placeholder="Enter the clinical text"
                    ),
                    outputs=gr.Dataframe(
                        headers=["Hierarchy", "Input Description", "Concept Name", "Concept ID"],
                        label="SNOMED CT Mapping Results",
                        wrap=True
                    ),
                    title="Standardize your clinical notes"
                )

    return result_app
