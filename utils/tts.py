# utils/tts.py
import pyttsx3

class TTS:
    def __init__(self, voice_id=None, rate=150):
        self.engine = pyttsx3.init()
        if voice_id:
            self.engine.setProperty('voice', voice_id)
        self.engine.setProperty('rate', rate)

    def speak(self, text):
        print(f"🟢 Jarvis diz: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
