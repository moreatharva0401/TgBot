from telegram.ext import Application, CommandHandler, MessageHandler, filters

BOT_TOKEN = "8527720491:AAHRksNVK0k6Biw1kqem_U8UYSyJGpSkBl4"

async def start(update, context):
    await update.message.reply_text("Hi there ✨ You’ve stepped into the Blue Aura…💙 a calm, comforting space. How can I brighten your day?")

async def echo(update, context):
    await update.message.reply_text(update.message.text)

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, echo))

app.run_polling()
