import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Your bot's command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your AI bot.")

# Build the bot app
app = ApplicationBuilder().token("8476019073:AAF1AYFKyVHH_JFk-oKIvgqAuYjmw9cOKB8").build()
app.add_handler(CommandHandler("start", start))

# Start the bot
app.run_polling()
