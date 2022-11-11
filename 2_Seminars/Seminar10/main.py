import requests
import logging
from config import TOKEN
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)


API_URL = 'https://7015.deeppavlov.ai/model'


def start(update, _):
    reply_keyboard = [['Операции с рациональными числами', 'Настроение', 'Операции с комплесными числами', 'Cancel'], [
        'Операции с рациональными числами', 'Настроение', 'Операции с комплесными числами', 'Cancel']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Добро пожаловать в калькулятор.', reply_markup=markup_key)
    return CHOICE


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def rational(update, context):
    data = {'x': [update.message.text]}
    res = requests.post(API_URL, json=data).json()
    santiment = res[0][0]
    print(res[0][0])
    print(res)
    update.message.reply_text(res[0][0])
    return start(update, context)


def rational_two(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел число: %s: %s",
                user.first_name, update.message.text)
    get_rational = update.message.text
    if get_rational.isdigit():
        get_rational = float(get_rational)
        context.user_data['rational_two'] = get_rational
        reply_keyboard = [['+', '-', '*', '/']]
        markup_key = ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True)
        update.message.reply_text(
            'Выберите операцию с числами', reply_markup=markup_key)
        return OPERATIONS_RATIONAL


API_URL = 'https://7012.deeppavlov.ai/model'

data = {'question_raw':  [question]}
res = requests.post(API_URL, json=data, verify=False).json()
