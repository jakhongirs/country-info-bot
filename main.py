from telegram.ext import Updater, Dispatcher, CommandHandler, CallbackContext, MessageHandler
from telegram.update import Update
from telegram.ext.filters import Filters
import requests
import settings

updater = Updater(settings.TELEGRAM_TOKEN)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Assalomu Alaykum, davlatlar haqida maΚΌlumot oluvchi botga xush kelibsiz! Misol: /country Uzbekistan")


def country(update: Update, context: CallbackContext):
    args = context.args

    if len(args) == 0:
        update.message.reply_text("Notug'ri formatdagi so'rov! Misol: /country Uzbekistan")
    else:
        try:
            country_text = ' '.join(args)

            response = requests.get(f'https://restcountries.com/v3.1/name/{country_text}')

            result = response.json()

            update.message.reply_text(
                f"π Davlat: {result[0]['name']['common']}\n"
                f"π Joylashuvi: {result[0]['subregion']}\n"
                f"π Poytaxt: {result[0]['capital'][0]}\n"
                f"π£ Davlat tili: {list(result[0]['languages'].values())[0]}\n"
                f"π± Pul birligi: {list(result[0]['currencies'].values())[0]['name']}\n"
                f"πΊ Maydoni: {result[0]['area']}\n"
                f"π¨βπ©βπ§ Aholi soni: {result[0]['population']}")
        except:
            update.message.reply_text("Davlat nomini to'g'ri kiriting!")


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('country', country))
dispatcher.add_handler(MessageHandler(Filters.all, start))

updater.start_polling()
updater.idle()
