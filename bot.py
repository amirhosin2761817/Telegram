from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8210753392:AAF8Y_lps0OkktfseLPJfSrbbm_AR7xdkgU"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "میلاد" in text:
        reply_text = (
            "قیمت ساعتی:\n"
            "تو ماشین ۵۰۰\n"
            "هتل ۱ تومن\n"
            "خونه ۲ تومن\n\n"
            "قیمت یه شب کامل:\n"
            "تو ماشین ۳ تومن\n"
            "هتل ۶ تومن\n"
            "خونه ۱۰ تومن"
        )
        await update.message.reply_text(reply_text)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)
    app.add_handler(message_handler)

    print("ربات داره کار می‌کنه...")
    app.run_polling()
