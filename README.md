# Voice-Based AI Agent (pyttsx3 + Ollama)

A hands-free assistant: you speak, a local Ollama model answers, and the reply is read aloud.

## How it works

1. `voice.py` - listens (Google Speech Recognition) and speaks (pyttsx3)
2. `brain.py` - sends your question to a local Ollama model
3. `main.py` - the loop; say exit, quit or stop to end
4. `config.py` - model name, voice rate, exit words, system prompt

## Setup

Install [Ollama](https://ollama.com) and pull a model (default: `llama3`), then:

```bash
pip install -r requirements.txt
python main.py
```n
Use `test_mic.py` to check your microphone first.

## Tech stack

Python, SpeechRecognition, pyttsx3, Ollama
