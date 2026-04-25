import gradio as gr
import ollama
import yaml
import os

CONFIG_FILE = "config.yaml"

if not os.path.exists(CONFIG_FILE):
    print("ERROR: config.yaml not found. Please ensure it exists.")
    exit(1)

with open(CONFIG_FILE, "r") as f:
    config = yaml.safe_load(f)

model = config["model"]
temperature = config["temperature"]
system_prompt = config["system_prompt"]
max_tokens = config["max_tokens"]

history = [{"role": "system", "content": system_prompt}]

def chat(user_message, _history):
    history.append({"role": "user", "content": user_message})
    try:
        response = ollama.chat(
            model=model,
            messages=history,
            options={"temperature": temperature, "num_predict": max_tokens}
        )
        reply = response["message"]["content"]
    except Exception as e:
        reply = f"Error: {e}\n\nMake sure Ollama is running and the model '{model}' is pulled (ollama pull {model})"
    history.append({"role": "assistant", "content": reply})
    return reply

with gr.Blocks(title="My AI Assistant", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 💬 My AI Assistant - Local & Uncensored")
    gr.ChatInterface(fn=chat)

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860)
