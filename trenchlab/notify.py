"""Optional Telegram alerts. Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID env vars."""
import os

from .http import post_json


def telegram(text):
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat:
        return False
    try:
        post_json(f"https://api.telegram.org/bot{token}/sendMessage",
                  {"chat_id": chat, "text": text, "disable_web_page_preview": True})
        return True
    except Exception as e:  # alerts must never crash the scanner
        print(f"[telegram] failed: {e}")
        return False
