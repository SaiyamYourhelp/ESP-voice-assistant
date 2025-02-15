import requests
import json

GEMINI_API_KEY = "AIzaSyAybJGr8rkGekB8uexzw2tOjDxJLnFYkZw"

with open("transcription.txt", "r") as f:
    user_question = f.read().strip()

data = {
    "contents": [{"parts": [{"text": user_question}]}]
}

response = requests.post(
    f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}",
    json=data
)

gemini_response = response.json().get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")

with open("gemini_response.txt", "w") as f:
    f.write(gemini_response)
