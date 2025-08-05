from telegram.ext import Updater, CommandHandler

# Function to handle /start command
def start(update, context):
    update.message.reply_text("Hello! I'm your AI bot.")

def main():
    # Replace with your actual bot token
    TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

    # Create updater and dispatcher
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Register command handler
    dp.add_handler(CommandHandler("start", start))

    # Start the bot
    print("🤖 Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
