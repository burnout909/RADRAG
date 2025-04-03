import gradio as gr

with gr.Blocks(css="""
    html, body {
        scroll-behavior: smooth;
        margin: 0;
        padding: 0;
        width: 100%;
    }

"""
) as app:

    with gr.Column(elem_classes=["container"]):
        

        # body
        with gr.Row(elem_classes=["body"]):
            with gr.Column(elem_classes=["text-box"], scale=1):
                gr.HTML("<div class='title'>RADRAG2</div>")
                

app = app