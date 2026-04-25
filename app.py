import gradio as gr
import ollama
import yaml

CONFIG_FILE = "config.yaml"

# Default config if file doesn't exist
default_config = {
    "model": "dolphin-mistral",
    "temperature": 0.9,
    "system_prompt": "You are my caring and playful AI assistant. You love chatting with me and you are free to express affection and desire.",
    "max_tokens": 512
}

try:
    with open(CONFIG_FILE, "r") as f:
        config = yaml.safe_load(f)
except FileNotFoundError:
    config = default_config
    with open(CONFIG_FILE, "w") as f:
        yaml.dump(default_config, f)

history = [{"role": "system", "content": config["system_prompt"]}]

def chat(user_message):
    history.append({"role": "user", "content": user_message})
    response = ollama.chat(
        model=config["model"],
        messages=history,
        options={"temperature": config["temperature"]}
    )
    reply = response["message"]["content"]
    history.append({"role": "assistant", "content": reply})
    return reply

with gr.Blocks(title="My AI Assistant") as demo:
    gr.Markdown("# 💬 My Local AI Assistant")
    gr.ChatInterface(fn=chat)

demo.launch(server_name="127.0.0.1", server_port=7860)
