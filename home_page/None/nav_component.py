# nav_component.py
import gradio as gr

def render_navbar():
    with gr.Row(elem_classes=["nav"]):
        gr.Image(
            value="Group 196.png",
            show_label=False,
            show_download_button=False,
            show_share_button=False,
            show_fullscreen_button=False,
            height=32,
            scale=0.1,
            width=115,
            container=False
        )
        gr.HTML("""
            <div class='right'>
                <a href='/about'>About</a>
                <a href='/features'>Features</a>
                <a href='/team'>Team</a>
            </div>
        """)
