import requests
DEEPGRAM_API_KEY = "5ba46f4a73516222984a543facd3236801016006"

def transcribe(file):
    with open(file, "rb") as audio:
        response = requests.post(
            "https://api.deepgram.com/v1/listen?model=nova-2",
            headers={"Authorization": f"Token {DEEPGRAM_API_KEY}"},
            data=audio
        )
    return response.json().get("results", [{}])[0].get("alternatives", [{}])[0].get("transcript", "")

transcript = transcribe("audio_chunks/sample.wav")
print(transcript)
