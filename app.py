import gradio as gr

def saludar(nombre):
    return f"Hola, {nombre}!"

demo = gr.Interface(
    fn=saludar,
    inputs="text",
    outputs="text",
    title="App basic con Gradio",
    description="Escribi tu nombre y la app te saluda."
)

demo.launch()