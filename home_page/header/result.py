import gradio as gr

# 환자 정보 더미 데이터 (예시)
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

with gr.Blocks(css="""
    .section-title {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .info-box {
        border: 1px solid #ccc;
        border-radius: 10px;
        padding: 20px;
        background-color: #f8f9fa;
    }
    .menu-box {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 20px;
        background-color: #ffffff;
    }
""") as app:

    gr.Markdown("### Patient")

    with gr.Row():
        # 환자 선택 드롭다운
        patient_selector = gr.Dropdown(choices=list(patients.keys()), label="Select Patient ID", value="12334")

    with gr.Row():
        # 좌측 메뉴
        with gr.Column(scale=1):
            gr.Markdown("**Patient Information**", elem_classes=["section-title"])
            with gr.Column(elem_classes=["menu-box"]):
                gr.Button("Medical History")
                gr.Button("Medications")
                gr.Button("All Visits")

        # 우측 정보 카드
        with gr.Column(scale=2):
            gr.Markdown("**Information**", elem_classes=["section-title"])
            info_display = gr.Markdown(elem_classes=["info-box"])
    
    # 연동
    patient_selector.change(fn=display_info, inputs=patient_selector, outputs=info_display)
    info_display.value = display_info("12334")  # 초기값

app = app
