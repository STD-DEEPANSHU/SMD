import os
from telegram.ext import ApplicationBuilder
from handlers import register_handlers

# Bot token from environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

def main():
    if not BOT_TOKEN:
        raise ValueError("❌ BOT_TOKEN not found! Please set it in environment variables.")

    # Create bot application
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register all handlers (from handlers.py)
    register_handlers(app)

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
