import gradio as gr

def render_dropdown_box(label="환자 선택", options=None):
    if options is None:
        options = ["12334", "56789", "89123"]
    options_html = "\n".join([f"<option value='{opt}'>{opt}</option>" for opt in options])

    return gr.HTML(f"""
        <style>
            .dropdown-card {{
                border: 1px solid #eee;
                border-radius: 12px;
                background-color: #fff;
                padding: 20px;
                width: 280px;
                font-family: Arial, sans-serif;
                box-shadow: 0px 3px 8px rgba(0,0,0,0.05);
            }}
            .dropdown-card label {{
                font-size: 16px;
                font-weight: bold;
                margin-bottom: 8px;
                display: block;
                color: #333;
            }}
            .dropdown-card select {{
                width: 100%;
                padding: 10px;
                font-size: 15px;
                border-radius: 8px;
                border: 1px solid #ccc;
            }}
        </style>
        <div class='dropdown-card'>
            <label>{label}</label>
            <select>
                {options_html}
            </select>
        </div>
    """)
