import gradio as gr
import pandas as pd

patients = {
    "12334": {"name": "John Doe", "gender": "Male", "nationality": "USA", "insurance": "Aetna"},
    "56789": {"name": "Jane Smith", "gender": "Female", "nationality": "Canada", "insurance": "BlueCross"},
    "89123": {"name": "Minsoo Kim", "gender": "Male", "nationality": "Korea", "insurance": "NHIS"}
}

def display_info(patient_id):
    info = patients[patient_id]
    return (
        f"**Name**: {info['name']}\n\n"
        f"**Gender**: {info['gender']}\n\n"
        f"**Nationality**: {info['nationality']}\n\n"
        f"**Insurance**: {info['insurance']}"
    )

def display_menu(patient_id, menu_name):
    info = patients[patient_id]
    return (
        f"## {menu_name}\n\n"
        f"**Patient**: {info['name']} (ID: {patient_id})\n\n"
        f"*(이 영역에 '{menu_name}' 관련 상세 정보를 표시할 수 있습니다.)*"
    )

def build_result_page():
    with gr.Blocks(css="""
.card {
    border: 1px solid #eee;
    border-radius: 10px;
    background-color: #fff;
    padding: 20px;
    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    min-height: 150px;
    margin-bottom: 15px;
}
    """) as app:

        with gr.Row():
            with gr.Column(scale=1, min_width=250):
                with gr.Column(elem_classes=["card"]):
                    gr.Markdown("### Patient")
                    patient_selector = gr.Dropdown(
                        choices=list(patients.keys()), 
                        value="12334",
                        label="Select Patient ID"
                    )
                
                with gr.Column(elem_classes=["card"]):
                    btn_info = gr.Button("Patient Information")
                    btn_history = gr.Button("Medical History")
                    btn_meds = gr.Button("Medications")
                    btn_visits = gr.Button("All Visits")

            with gr.Column(scale=1, min_width=300):
                with gr.Column(elem_classes=["card"]):
                    gr.Markdown("### Information")
                    info_display = gr.Markdown() 

            with gr.Column(scale=1, min_width=250):
                with gr.Column(elem_classes=["card"]):
                    gr.Markdown("### Clinical Notes")
                    clinical_notes = gr.Textbox(
                        placeholder="진단 메모 등을 작성",
                        lines=10
                    )
                    standardize_btn = gr.Button("Standardization")


        with gr.Row():
            with gr.Column(scale=1, min_width=250):
                with gr.Column(elem_classes=["card"]):
                    gr.Markdown("### Procedures")
                    gr.Dropdown(
                        choices=["0001.dcm", "0002.dcm", "0003.dcm"],
                        value="0001.dcm",
                        label="Select Procedure"
                    )

        
            with gr.Column(scale=1, min_width=300):
                with gr.Column(elem_classes=["card"]):
                    gr.Markdown("### X-Ray Image")
                    gr.Image(
                        label="Preview", 
                        value=None, 
                        type="filepath"
                    )
        
            with gr.Column(scale=1, min_width=300):
                with gr.Column(elem_classes=["card"]):
                    gr.Markdown("### DICOM Metadata")
                    meta_df = pd.DataFrame([
                        {"Tag": "(0008,0060)", "Attribute": "Modality", "Value": "DX"},
                        {"Tag": "(0020,000D)", "Attribute": "Study Instance UID", "Value": "1.2.840.113..."},
                        {"Tag": "(0008,0018)", "Attribute": "SOP Instance UID", "Value": "1.2.840.113..."},
                        {"Tag": "(0008,0022)", "Attribute": "Acquisition Date", "Value": "20230401"},
                        {"Tag": "(0018,0060)", "Attribute": "kVp", "Value": "120"},
                        {"Tag": "(0018,5101)", "Attribute": "View Position", "Value": "AP"}
                    ])
                    dicom_table = gr.DataFrame(
                        value=meta_df,
                        headers=["Tag", "Attribute", "Value"],
                        datatype=["str", "str", "str"],
                        interactive=False,
                        label="DICOM Metadata Table"
                    )
                    gr.Markdown("<a href='#'>Find Tag</a>")

        info_display.value = display_info("12334")

        patient_selector.change(
            fn=display_info,
            inputs=patient_selector,
            outputs=info_display
        )

        btn_info.click(
            fn=display_info,
            inputs=patient_selector,
            outputs=info_display
        )

        btn_history.click(
            fn=lambda pid: display_menu(pid, "Medical History"),
            inputs=patient_selector,
            outputs=info_display
        )
        btn_meds.click(
            fn=lambda pid: display_menu(pid, "Medications"),
            inputs=patient_selector,
            outputs=info_display
        )
        btn_visits.click(
            fn=lambda pid: display_menu(pid, "All Visits"),
            inputs=patient_selector,
            outputs=info_display
        )

    return app
