@echo off
title My AI Assistant
echo =======================================
echo  My AI Assistant - Local Installer
echo =======================================
echo.
echo Step 1: Installing Python packages...
pip install gradio ollama pyyaml
if errorlevel 1 (
    echo Failed to install packages. Make sure Python is installed.
    pause
    exit /b 1
)
echo.
echo Step 2: Checking Ollama...
where ollama >nul 2>nul
if errorlevel 1 (
    echo Ollama not found. Please install from https://ollama.com
    pause
    exit /b 1
)
echo.
echo Step 3: Pulling uncensored model (first time may take a few minutes)...
ollama pull dolphin-mistral
echo.
echo Step 4: Starting AI Assistant...
echo.
echo After the server starts, open http://127.0.0.1:7860 in your browser.
echo Press Ctrl+C in this window to stop the server.
echo.
python app.py
pause
