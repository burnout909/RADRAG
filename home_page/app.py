# app.py 또는 app.ipynb
import gradio as gr
import home, about, features, team, result

css = """
html, body {
    scroll-behavior: smooth;
    margin: 0;
    padding: 0;
    width: 100%;
}

.container {
    max-width: 100%;
    margin: 0 auto;
}

.hero-section {
    display: flex;
    align-items: center;
    gap: 68px;
    margin-left: 117px;
    margin-right: 97.8px;
}

.text-box {
    width: 519px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.title {
    font-size: 52px; 
    font-weight: bold;
}

.subtitle {
    font-size: 36px; 
    font-weight: bold; 
}

.description {
    font-size: 18px; 
    color: #9A9EA5; 
    line-height: 1.6; 
}

.cta-btn {
    width: 160px;
    height: 50px;
    border-radius: 5px;
    padding: 5px 26px;
    background-color: #007AFF;
    color: white;
    font-weight: bold;
    font-size: 16px;
    border: none;
    cursor: pointer;
}
"""


with gr.Blocks(css=css) as demo:
    home.app.render()

with demo.route("Result", path="/result"):
    result.app.render()

with demo.route("About", path="/about"):
    about.app.render()

with demo.route("Features", path="/features"):
    features.app.render()

with demo.route("Team", path="/team"):
    team.app.render()


demo.launch(share=True, show_api=False, show_error=True, inbrowser=True)
