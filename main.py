from telegram.ext import Updater, Dispatcher, CommandHandler, CallbackContext
from telegram.update import Update
import settings

updater = Updater(settings.TELEGRAM_TOKEN)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Salom!")


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
