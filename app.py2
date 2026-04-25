import gradio as gr
from src.chat_engine import ChatEngine

engine = ChatEngine()

def respond(message, history):
    return engine.chat(message)

with gr.Blocks(title="My AI Assistant", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 💬 My Local AI Assistant")
    gr.ChatInterface(
        fn=respond,
        title="Talk freely - no filters",
        description="Be respectful. The model is uncensored, but you control it locally."
    )

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860)
