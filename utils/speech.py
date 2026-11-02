# utils/speech.py
import speech_recognition as sr

class SpeechRecognizer:
    def __init__(self, model="large"):
        self.recognizer = sr.Recognizer()
        self.model = model

    def listen(self):
        """Escuta o microfone e retorna o texto reconhecido."""
        with sr.Microphone() as source:
            print("🟢 Escutando... (diga algo)")
            audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
        try:
            text = self.recognizer.recognize_whisper(audio, model=self.model)
            print(f"🟡 Você disse: {text}")
            return text
        except sr.UnknownValueError:
            print("⚠️ Não entendi.")
            return None
        except sr.RequestError as e:
            print(f"⚠️ Erro no Whisper: {e}")
            return None
