from telegram.ext import Updater, Dispatcher, CommandHandler, CallbackContext, MessageHandler
from telegram.update import Update
from telegram.ext.filters import Filters
import requests
import settings

updater = Updater(settings.TELEGRAM_TOKEN)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Assalomu Alaykum, davlatlar haqida maʼlumot oluvchi botga xush kelibsiz! Misol: /country Uzbekistan")


def country(update: Update, context: CallbackContext):
    args = context.args

    if len(args) == 0:
        update.message.reply_text("Notug'ri formatdagi so'rov! Misol: /country Uzbekistan")
    else:
        country_text = ' '.join(args)

        response = requests.get(f'https://restcountries.com/v3.1/name/{country_text}')

        result = response.json()

        update.message.reply_text(result[0]['name']['common'])


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('country', country))
dispatcher.add_handler(MessageHandler(Filters.all, start))

updater.start_polling()
updater.idle()
