import gradio as gr
from header import home, about, features, team, result


css = """
html, body {
    scroll-behavior: smooth;
    margin: 0;
    padding: 0;
    width: 100%;
    font-size: 16px;
    font-family: sans-serif;
}

.container {
    max-width: 100%;
    margin: 0 auto;
    padding: 0 5%;
}

.hero-section {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 4vw;
    margin: 4vh 0;
}

.text-box {
    flex: 1 1 40%;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    min-width: 300px;
}

.title {
    font-size: 3.25rem; 
    font-weight: bold;
    margin-bottom: 0.5rem;
}

.subtitle {
    font-size: 2.25rem; 
    font-weight: bold;
    margin-bottom: 1rem;
}

.description {
    font-size: 1.125rem;  
    color: #9A9EA5;
    line-height: 1.6;
    margin-bottom: 2rem;
}

.cta-btn {
    width: 10rem;
    height: 3.125rem;
    border-radius: 5px;
    padding: 0.5rem 1.5rem;
    background-color: #007AFF;
    color: white;
    font-weight: bold;
    font-size: 1rem;
    border: none;
    cursor: pointer;
}
"""

with gr.Blocks(css=css) as demo:
    home.app.render()

with demo.route("Result", path="/result"): result.build_result_page()

with demo.route("About", path="/about"):
    about.app.render()

with demo.route("Features", path="/features"):
    features.app.render()

with demo.route("Team", path="/team"):
    team.app.render()

demo.launch(share=True, show_api=False, show_error=True, inbrowser=True)