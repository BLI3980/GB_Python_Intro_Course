
import telegram
from telegram.ext import Updater
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# bot = telegram.Bot(token='5571491845:AAFTek__yjvDFQ1sJvJL90J_OHnGWtYgqdg')

# print(bot.getMe())
# updates = bot.get_updates()
# print(updates[0])

# bot.send_message(text='Whats up!', chat_id=452635171)

updater = Updater(
    token='5571491845:AAFTek__yjvDFQ1sJvJL90J_OHnGWtYgqdg')
dispatcher = updater.dispatcher
