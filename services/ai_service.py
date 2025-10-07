import requests
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "your_groq_api_key_here")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

def generate_message(base_text, tone="polite"):
    prompt = f"Yeh zaroorat ko Roman Urdu mein ek short, polite aur natural jumla banao. Tone: {tone}. Text: '{base_text}'"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "Tum sirf Roman Urdu mein jawab dogay, English ya Urdu script nahi."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.7,
        "max_tokens": 60,
    }

    try:
        response = requests.post(GROQ_URL, headers=headers, json=payload)
        data = response.json()
        result = data["choices"][0]["message"]["content"].strip()
        return result
    except Exception as e:
        print("Groq API error:", e)
        return base_text
