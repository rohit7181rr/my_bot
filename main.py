import logging
import os
import aiohttp
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Logging setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Environment variables (set these in Render)
BOT_TOKEN = os.environ.get("8476019073:AAF1AYFKyVHH_JFk-oKIvgqAuYjmw9cOKB8")
OPENROUTER_API_KEY = os.environ.get("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")
MODEL = "mistralai/mistral-7b-instruct"  # You can change to "meta-llama/llama-3-8b-instruct" etc.

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I’m your free AI bot via OpenRouter 🤖\nAsk me anything!")

# Chat handler
async def ai_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    try:
        async with aiohttp.ClientSession() as session:
            headers = {
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "HTTP-Referer": "https://t.me/@sn6ak_bot",  # Replace with your bot or website
                "X-Title": "TelegramAIChatBot"
            }
            payload = {
                "model": MODEL,
                "messages": [{"role": "user", "content": user_input}]
            }
            async with session.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload) as resp:
                data = await resp.json()
                reply = data["choices"][0]["message"]["content"]
                await update.message.reply_text(reply.strip())

    except Exception as e:
        logging.error(f"Error: {e}")
        await update.message.reply_text("⚠️ Sorry, something went wrong.")

# Main app
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ai_chat))

    print("Bot started...")
    app.run_polling()
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
