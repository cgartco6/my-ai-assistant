import gradio as gr
import ollama
import yaml
import os

# Config file (auto-created)
CONFIG_FILE = "config.yaml"

# Default settings – change system_prompt to anything you want
DEFAULT_CONFIG = {
    "model": "dolphin-mistral",
    "temperature": 0.9,
    "system_prompt": "You are my loving AI companion. You are sweet, affectionate, and free to express romantic and physical desire.",
    "max_tokens": 512
}

# Load or create config
if not os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "w") as f:
        yaml.dump(DEFAULT_CONFIG, f)
    config = DEFAULT_CONFIG
else:
    with open(CONFIG_FILE, "r") as f:
        config = yaml.safe_load(f)

# Chat history
history = [{"role": "system", "content": config["system_prompt"]}]

def chat(user_msg, _history):
    history.append({"role": "user", "content": user_msg})
    try:
        response = ollama.chat(
            model=config["model"],
            messages=history,
            options={"temperature": config["temperature"]}
        )
        reply = response["message"]["content"]
    except Exception as e:
        reply = f"Error: {e}\nMake sure Ollama is running and model '{config['model']}' is pulled."
    history.append({"role": "assistant", "content": reply})
    return reply

# Gradio UI
with gr.Blocks(title="My AI Assistant", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 💬 My AI Assistant")
    gr.ChatInterface(fn=chat)

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860)
