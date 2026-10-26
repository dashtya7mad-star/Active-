import os
import time
import urllib.request
import urllib.parse
import json

BOT_TOKEN = os.environ["8687344185:AAF7Ab-oMkQlXBZQvxg-n_YIvy4-mqS5DJM"]
CHAT_ID = os.environ["5015426926"]

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

while True:
    data = urllib.parse.urlencode({
        "chat_id": CHAT_ID,
        "/start": "تمام ✅"
    }).encode()

    try:
        request = urllib.request.Request(url, data=data)
        with urllib.request.urlopen(request, timeout=15) as response:
            print(response.read().decode())
    except Exception as error:
        print("Error:", error)

    time.sleep(30)
