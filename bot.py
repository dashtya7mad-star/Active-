import os
import time
import requests

BOT_TOKEN = (os.environ.get("BOT_TOKEN") or "").strip()
CHAT_ID = (os.environ.get("CHAT_ID") or "").strip()

if not BOT_TOKEN or not CHAT_ID:
    raise ValueError("BOT_TOKEN or CHAT_ID is missing from GitHub Secrets")

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

while True:
    try:
        response = requests.post(
            API_URL,
            json={
                "chat_id": CHAT_ID,
                "text": "/start"
            },
            timeout=30
        )

        result = response.json()

        if response.ok and result.get("ok"):
            print("Message sent successfully.")
        else:
            print("Telegram error:", result)

    except requests.RequestException as error:
        print("Connection error:", error)

    time.sleep(10)
