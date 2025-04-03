import gradio as gr
import os

image_path = os.path.abspath("img/Group.png")

with gr.Blocks() as app:

    with gr.Column(elem_classes=["container"]):
        

        # Hero Section
        with gr.Row(elem_classes=["hero-section"]):
            with gr.Column(elem_classes=["text-box"], scale=1):
                gr.HTML("<div class='title'>RADRAG</div>")
                gr.HTML("<div class='subtitle'>Standardization Tool of <br> Radiology Free-text</div>")
                gr.HTML("""
                    <div class='description'>
                        Make smart clinical decisions and seamless claims with <br>
                        RADRAG – your LLM-based standardization tool for radiology <br>
                        free-text.
                    </div>
                """)
                gr.HTML("<a href='/result'><button class='cta-btn'>GET STARTED</button></a>")

            with gr.Column(scale=1):
                gr.Image(
                    value=image_path,
                    show_label=False,
                    show_share_button=False,
                    show_download_button=False,
                    show_fullscreen_button=False,
                    height=464,
                    width=638,
                    elem_classes=["hero-image"],
                    container=False
                )

app = app