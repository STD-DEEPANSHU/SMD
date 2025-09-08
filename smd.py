import os
from telegram.ext import Updater
from handlers import register_handlers

BOT_TOKEN = os.getenv("BOT_TOKEN")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Register all handlers
    register_handlers(dp)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
