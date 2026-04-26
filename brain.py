import subprocess
from config import OLLAMA_MODEL,SYSTEM_PROMPT

def ask_ollama(prompt):
    full_prompt = f"{SYSTEM_PROMPT}\n\n{prompt}\n\n"
    
    result=subprocess.run(
        ["ollama", "ask", OLLAMA_MODEL, full_prompt],
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()