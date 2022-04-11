import os

from telegram.ext import Updater
import logging
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler

import main

from dotenv import load_dotenv

load_dotenv("keys.env")
bot_id = os.environ["telegram_bot_id"]
updater = Updater(token=bot_id, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start_bot():
    updater.start_polling()


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def help1(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="*WELCOME TO CHEAP FLIGHT FINDER*\n" +
             "To find cheap flights write a query in the following format: \n /query FROM_CITY-TO_CITY-MAX_PRICE-MAX_MONTHS"
             + "\n\nFlights leaving in months more than MAX_MONTHS would not be displayed\n\n"
             + "Example: /query New Delhi-Mumbai-6000-3\n"

    )


def get_data(update: Update, context: CallbackContext):
    data = {"from": -1, "to": -1, "price": -1, "months": 3, "from_code": "", "to_code": ""}

    received_string = str("".join(context.args)).replace(" ", "")
    print(received_string)
    received_string = received_string[:-2]
    print(received_string)
    received_data = received_string.split("-")
    data["from"] = received_data[0].title()
    data["to"] = received_data[1].title()
    data["price"] = int(received_data[2])
    if len(received_data) == 4:
        data["months"] = int(received_data[3])
    print(data)
    message = main.process_query(data)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


get_data_handler = CommandHandler('query', get_data)
dispatcher.add_handler(get_data_handler)

help_handler = CommandHandler('help', help1)
dispatcher.add_handler(help_handler)
