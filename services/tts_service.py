from gtts import gTTS
import os
import uuid

def text_to_speech(text):
    """Converts text to Urdu voice using gTTS."""
    try:
        filename = f"tts_{uuid.uuid4().hex}.mp3"
        filepath = os.path.join("static", filename)

        tts = gTTS(text=text, lang="ur", slow=False)
        tts.save(filepath)

        return filepath
    except Exception as e:
        print("TTS error:", e)
        return None
