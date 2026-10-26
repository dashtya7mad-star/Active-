
import os
import requests
from datetime import datetime, timezone

# Read GitHub Actions Secrets
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

# Check configuration
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing from GitHub Secrets")

if not CHAT_ID:
    raise ValueError("CHAT_ID is missing from GitHub Secrets")

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


def send_message(message):
    try:
        response = requests.post(
            API_URL,
            json={
                "chat_id": CHAT_ID,
                "text": message
            },
            timeout=30
        )

        response.raise_for_status()
        result = response.json()

        if not result.get("ok"):
            print("Telegram error:", result)
            return False

        print("Message sent successfully.")
        return True

    except requests.RequestException as error:
        print(f"Failed to send message: {error}")
        return False


if __name__ == "__main__":
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    message = f"🤖 البوت يعمل بنجاح!\nوقت التشغيل: {now}"

    if not send_message(message):
        raise SystemExit(1)
