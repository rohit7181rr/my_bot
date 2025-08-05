import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your AI bot 🤖")

# Main bot setup
async def main():
    app = ApplicationBuilder().token("8476019073:AAF1AYFKyVHH_JFk-oKIvgqAuYjmw9cOKB8").build()

    app.add_handler(CommandHandler("start", start))

    print("🤖 AI Bot is running...")
    await app.run_polling()

# Entry point
if __name__ == "__main__":
    asyncio.run(main())
