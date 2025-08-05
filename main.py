import logging
import os
import openai
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Set your tokens (use env vars on Render)
BOT_TOKEN = os.environ.get("8476019073:AAF1AYFKyVHH_JFk-oKIvgqAuYjmw9cOKB8")  # Telegram bot token
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")  # OpenAI API key

openai.api_key = OPENAI_API_KEY

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I am your AI chatbot 🤖. Ask me anything!")

# AI response handler
async def ai_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            messages=[{"role": "user", "content": user_msg}],
        )
        reply = response.choices[0].message.content.strip()
        await update.message.reply_text(reply)
    except Exception as e:
        logging.error(e)
        await update.message.reply_text("⚠️ Sorry, something went wrong.")

# Main function
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ai_chat))

    print("Bot started...")
    app.run_polling()
# --- Echo message handler ---
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🔁 You said: {update.message.text}")

# --- Main bot setup ---
if __name__ == "__main__":
    app = ApplicationBuilder().token("8476019073:AAF1AYFKyVHH_JFk-oKIvgqAuYjmw9cOKB8").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ Bot is running...")
    app.run_polling()
# Run the bot
app = ApplicationBuilder().token("8476019073:AAF1AYFKyVHH_JFk-oKIvgqAuYjmw9cOKB8").build()

# Add handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_text))
app.add_handler(MessageHandler(filters.UpdateType.CALLBACK_QUERY, button_handler))

# Run the bot
app.run_polling()
