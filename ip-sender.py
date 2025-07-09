import requests

# تنظیمات ربات تلگرام
TELEGRAM_TOKEN = "7945542630:AAHTTsEVof5Y5HoaqcPaBXff5aqITo4n0uQ"  # توکن ربات رو از BotFather بگیر
CHAT_ID = "7179154341"  # چت آیدی رو از @userinfobot بگیر
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

# تابع برای گرفتن IP عمومی
def get_public_ip():
    try:
        # درخواست به API ipify برای گرفتن IP عمومی
        response = requests.get("https://api.ipify.org")
        public_ip = response.text
        return public_ip
    except Exception as e:
        return f"خطا: {e}"

# تابع برای ارسال پیام به تلگرام
def send_to_telegram(message):
    try:
        payload = {"chat_id": CHAT_ID, "text": message}
        response = requests.post(TELEGRAM_API_URL, data=payload)
        if response.status_code == 200:
            print("پیام با موفقیت به تلگرام ارسال شد!")
        else:
            print(f"خطا در ارسال به تلگرام: {response.text}")
    except Exception as e:
        print(f"خطا در اتصال به تلگرام: {e}")

# اجرا
if __name__ == "__main__":
    # گرفتن IP عمومی
    ip = get_public_ip()
    message = f"آدرس IP عمومی گوشی: {ip}"
    
    # چاپ در کنسول
    print(message)
    
    # ارسال به تلگرام
    send_to_telegram(message)
