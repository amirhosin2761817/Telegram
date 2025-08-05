from telegram.ext import Updater, MessageHandler, Filters

def reply(update, context):
    if 'میلاد' in update.message.text:
        update.message.reply_text(
            'قیمت ساعتی:\n'
            'تو ماشین ۵۰۰\n'
            'هتل ۱ تومن\n'
            'خونه ۲ تومن\n'
            'قیمت یه شب کامل:\n'
            'تو ماشین ۳ تومن\n'
            'هتل ۶ تومن\n'
            'خونه ۱۰ تومن'
        )

def main():
    updater = Updater("8210753392:AAF8Y_lps0OkktfseLPJfSrbbm_AR7xdkgU", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
