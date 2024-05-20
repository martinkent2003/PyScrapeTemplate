import gradio as gr

def greet(name):
    return f"Hello {name}!"
demo = gr.Interface(fn=greet, inputs=gr.Textbox(lines=2, placeholder="name here"), outputs="text")

demo.launch()