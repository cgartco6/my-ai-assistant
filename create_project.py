import os

def create_project():
    base = "my-ai-assistant"
    os.makedirs(base, exist_ok=True)
    os.makedirs(os.path.join(base, "src"), exist_ok=True)
    os.makedirs(os.path.join(base, "examples"), exist_ok=True)

    files = {
        "README.md": '''# My Local AI Assistant

Runs an uncensored LLM locally using Ollama. No cloud API, no censorship.

## Requirements
- Install [Ollama](https://ollama.com/)
- Pull an uncensored model, e.g.:  
  `ollama pull dolphin-mistral` or `ollama pull nous-hermes`
- Python 3.9+

## Setup
```bash
git clone <your-repo-url>
cd my-ai-assistant
pip install -r requirements.txt
