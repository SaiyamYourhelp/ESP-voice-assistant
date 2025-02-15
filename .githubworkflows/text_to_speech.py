import requests

with open("gemini_response.txt", "r") as f:
    text = f.read().strip()

AUDIO_OUTPUT = "response_audio/output.mp3"
GOOGLE_TTS_URL = f"https://translate.google.com/translate_tts?ie=UTF-8&q={text}&tl=en&client=tw-ob"

response = requests.get(GOOGLE_TTS_URL)

with open(AUDIO_OUTPUT, "wb") as f:
    f.write(response.content)
