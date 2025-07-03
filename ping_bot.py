import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

message = "⏰ Проверка: бот работает через GitHub Actions!"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
data = {
    "chat_id": CHAT_ID,
    "text": message
}

response = requests.post(url, data=data)
print("Status:", response.status_code)
print("Response:", response.text)
