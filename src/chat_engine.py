import ollama
import yaml

class ChatEngine:
    def __init__(self, config_path="config.yaml"):
        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)
        self.model = self.config["model"]
        self.system_prompt = self.config["system_prompt"]
        self.temperature = self.config["temperature"]
        self.history = [{"role": "system", "content": self.system_prompt}]

    def chat(self, user_message):
        self.history.append({"role": "user", "content": user_message})
        response = ollama.chat(
            model=self.model,
            messages=self.history,
            options={"temperature": self.temperature}
        )
        reply = response["message"]["content"]
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def clear_history(self):
        self.history = [{"role": "system", "content": self.system_prompt}]
