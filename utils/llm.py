# utils/llm.py
import os
from ollama import Client

class LLMClient:
    def __init__(self, model=None, host=None):
        self.model = model or os.getenv("LLM_MODEL", "gpt-oss:20b")
        self.host = host or os.getenv("OLLAMA_HOST", "http://localhost:11434")
        self.client = Client(host=self.host)

    def chat(self, messages, stream=False):
        """Return full response (blocking)."""
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": stream
        }
        if stream:
            return self.client.chat_stream(**payload)
        else:
            response = self.client.chat(**payload)
            return [response]  # Normalizar para iterável

# Exemplo de uso:
# llm = LLMClient()
# resp = llm.chat([{'role': 'user', 'content': 'Olá'}])[0]['message']['content']
