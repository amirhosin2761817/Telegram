from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

REPLY_TEXT = """
💸 قیمت ساعتی:
🚗 تو ماشین: ۵۰۰
🏨 هتل: ۱ تومن
🏠 خونه: ۲ تومن

🌙 قیمت یه شب کامل:
🚗 تو ماشین: ۳ تومن
🏨 هتل: ۶ تومن
🏠 خونه: ۱۰ تومن
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من فعال‌ام 😎")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return
    text = update.message.text.lower()
    if "میلاد" in text:
        await update.message.reply_text(REPLY_TEXT)

app = ApplicationBuilder().token("توکن_ربات_تو_اینجا_بذار").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
token("8210753392:AAF8Y_lps0OkktfseLPJfSrbbm_AR7xdkgU")
