import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Replace with your actual bot token
BOT_TOKEN = "8476019073:AAF1AYFKyVHH_JFk-oKIvgqAuYjmw9cOKB8"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your bot 🤖\nHow can I help you?")

# For any message
async def reply_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"You said: {user_message}")

# Main function to run the bot
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_text))

    print("🤖 Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
    data = query.data
    if data == "help":
        await query.edit_message_text("🆘 Help: Just type a message and I’ll reply!\nUse /start to return.")
    elif data == "about":
        await query.edit_message_text("🤖 About: I'm a Telegram bot built with Python.")
    elif data == "chat":
        await query.edit_message_text("🗣️ Chat mode activated! Say something.")

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
