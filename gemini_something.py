import requests

api_key = "AIzaSyCTAVIe53wK-Q2wEmgJEOmy3Gaz_hHPdIk"
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
