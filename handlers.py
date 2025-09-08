from telegram.ext import CommandHandler, MessageHandler, Filters
from downloader import download_and_send

def start(update, context):
    update.message.reply_text("👋 Send me any social media video link, I'll download it for you!")

def video_handler(update, context):
    url = update.message.text.strip()
    download_and_send(url, update)

def register_handlers(dp):
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, video_handler))
