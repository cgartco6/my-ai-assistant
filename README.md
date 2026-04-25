VOICE AI ASSISTANT FOR WINDOWS

How to use:
1. Double-click run.bat
2. When the web page opens, allow microphone access.
3. To speak: click the microphone icon, speak, then click "Send Voice". She will answer aloud.
4. To type: type in the text box, press "Send Text". She will also speak the answer if voice is enabled.

Requirements:
- Windows 10/11
- Python 3.9+ installed (with "Add to PATH")
- Ollama installed from https://ollama.com

First run downloads the dolphin-mistral model (~4GB). Subsequent runs are instant.

Troubleshooting:
- If no voice output: check your speakers, or edit config.yaml: voice_enabled: true
- If speech recognition fails: speak clearly, check microphone, or use text input instead.
- To change her personality: edit config.yaml (system_prompt)
