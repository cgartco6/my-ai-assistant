# Optional helper functions (e.g., for saving/loading chat logs)

import json
from datetime import datetime

def save_chat_log(history, filename=None):
    if filename is None:
        filename = f"chat_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(history, f, indent=2)
    return filename

def load_chat_log(filename):
    with open(filename, "r") as f:
        return json.load(f)
