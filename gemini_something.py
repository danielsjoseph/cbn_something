import requests
import os 
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/text-bison-001:generateText?key={api_key}"

payload = {
    "prompt": {
        "text": "Who is Donald Trump?"
    }
}

headers = {"Content-Type": "application/json"}
response = requests.post(url, json=payload, headers=headers)
data = response.json()

if "candidates" in data:
    print(data["candidates"][0]["output"])
else:
    print("Error:", data)
