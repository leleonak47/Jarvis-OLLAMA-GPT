# main.py
import os
import uuid
import datetime
import time

from dotenv import load_dotenv
from utils.speech import SpeechRecognizer
from utils.tts import TTS
from utils.llm import LLMClient
from utils.db import Logger
from utils.commands import parse_command, execute as exec_cmd

# --- Configurações iniciais ------------------------------------
os.environ.setdefault("PYTHONIOENCODING", "utf-8")

# Instancia objetos
speech = SpeechRecognizer(model="small")   # Whisper
tts = TTS()                                 # pyttsx3
llm = LLMClient()                           # Ollama
load_dotenv()                               # Carrega as variáveis do arquivo .env
db_logger = Logger()                         # SQL Server

# Cria ID de sessão (útil para rastrear conversas)
session_id = uuid.uuid4()

# Loop principal
def main_loop():
    while True:
        # 1️⃣ Captura áudio
        user_text = speech.listen()
        if not user_text:
            continue

        # 2️⃣ Envia para o LLM
        messages = [
            {"role": "system", "content": "Você é o Jarvis, um assistente pessoal. Responda de forma curta, use 'run: <comando>' quando precisar executar algo no Windows."},
            {"role": "user", "content": user_text}
        ]

        try:
            resp_gen = llm.chat(messages)
            # LLM pode retornar como iterable (streaming) ou como único dict
            assistant_text = ""
            for part in resp_gen:
                assistant_text += part['message']['content']
        except Exception as e:
            assistant_text = f"⚠️ Erro no modelo: {e}"

        # 3️⃣ TTS
        tts.speak(assistant_text)

        # 4️⃣ Parse e execute comando (se houver)
        cmd = parse_command(assistant_text)
        cmd_result = None
        if cmd:
            cmd_result = exec_cmd(cmd)
            if cmd_result:
                tts.speak(f"Resultado: {cmd_result}")

        # 5️⃣ Log
        db_logger.log(session_id, user_text, assistant_text + ("\nResultado: " + cmd_result if cmd_result else ""))

        # 6️⃣ Pausa curta
        time.sleep(0.5)

if __name__ == "__main__":
    try:
        print("🚀 Jarvis iniciando. Pressione Ctrl+C para sair.")
        main_loop()
    except KeyboardInterrupt:
        print("\n👋 Encerrando Jarvis. Até logo!")
