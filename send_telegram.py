import os
import requests

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
FILE_PATH = "all_servers.txt" # فایل اصلی خروجی این پروژه

def send_to_telegram():
    if not os.path.exists(FILE_PATH):
        print("فایل کانفیگ‌ها پیدا نشد!")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    with open(FILE_PATH, 'rb') as f:
        files = {'document': f}
        data = {
            'chat_id': CHAT_ID,
            'caption': '🔄 آپدیت جدید کانفیگ‌های V2Ray\n@YourChannel' # به جای YourChannel آیدی کانالتان را بنویسید
        }
        response = requests.post(url, data=data, files=files)
        if response.status_code == 200:
            print("با موفقیت به تلگرام ارسال شد!")
        else:
            print(f"خطا در ارسال: {response.text}")

if __name__ == "__main__":
    send_to_telegram()
