import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# --- /start command handler ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💡 Help", callback_data='help')],
        [InlineKeyboardButton("ℹ️ About", callback_data='about')],
        [InlineKeyboardButton("💬 Chat", callback_data='chat')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Hello! I'm your smart AI bot. Choose an option below:",
        reply_markup=reply_markup
    )

# --- Button click handler ---
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

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
