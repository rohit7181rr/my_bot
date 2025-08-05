import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Enable logging
logging.basicConfig(level=logging.INFO)

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💡 Help", callback_data='help')],
        [InlineKeyboardButton("ℹ️ About", callback_data='about')],
        [InlineKeyboardButton("💬 Chat", callback_data='chat')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Hello! I'm your smart AI bot. Choose an option below:", reply_markup=reply_markup
    )

# Handles inline button presses
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "help":
        await query.edit_message_text("🆘 Send any message and I'll reply back!\nUse /start to return.")
    elif query.data == "about":
        await query.edit_message_text("🤖 I'm a Telegram bot built with love and Python.")
    elif query.data == "chat":
        await query.edit_message_text("🗣️ Sure! Just type your message and I'll echo it.")

# Replies to normal text messages
async def reply_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    await update.message.reply_text(f"🔁 You said: {user_msg}")

# Run the bot
app = ApplicationBuilder().token("YOUR_BOT_TOKEN_HERE").build()

# Add handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_text))
app.add_handler(MessageHandler(filters.UpdateType.CALLBACK_QUERY, button_handler))

# Run the bot
app.run_polling()
