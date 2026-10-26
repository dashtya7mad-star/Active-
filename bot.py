
import os
import time
import json
import urllib.request
import urllib.parse
import urllib.error

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["5015426926"]

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

while True:
    data = urllib.parse.urlencode({
        "chat_id": CHAT_ID,
        "text": "/start"
    }).encode("utf-8")

    request = urllib.request.Request(
        API_URL,
        data=data,
        method="POST"
    )

    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            result = json.loads(response.read().decode("utf-8"))

            if result.get("ok"):
                print("Message sent successfully")
            else:
                print("Telegram API error:", result)

    except Exception as error:
        print("Error:", error)

    time.sleep(30)
