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

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


CHOICE, NUMBER1, NUMBER2, OPERATION = range(4)


def start(update, _):
    # reply_keyboard = [['7', '8', '9', '/'], ['4', '5', '6', '*'], ['1', '2', '3', '-'],
    #                   ['+/-', '0', '.', '+'], ['x^2', 'Sqrt(x)', 'x^y', '='],
    #                   ]
    reply_keyboard = [['ADD', 'SUBTRACT', 'MULTIPLY'],
                      ['DIVIDE', 'POWER', 'END']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard)
    update.message.reply_text(
        'Choose operation.', reply_markup=markup_key)
    return CHOICE


def choice(update, context):
    user = update.message.from_user
    logger.info('Operation choice: %s: %s',
                user.first_name, update.message.text)
    user_choice = update.message.text
    context.user_data['user_choice'] = user_choice
    if user_choice == 'END':
        return cancel(update, context)
    else:
        update.message.reply_text('Enter the first number.')
        return NUMBER1


def number1(update, context):
    user = update.message.from_user
    logger.info('User has entered a number: %s: %s',
                user.first_name, update.message.text)
    number1 = update.message.text
    operation = context.user_data.get('user_choice')
    if number1.isdigit():
        number1 = int(number1)
        context.user_data['number1'] = number1
        update.message.reply_text('Enter the second number.')
        return NUMBER2
    else:
        update.message.reply_text('This is not a number.')


def number2(update, context):
    user = update.message.from_user
    logger.info('User has entered a number: %s: %s',
                user.first_name, update.message.text)
    number2 = update.message.text
    if number2.isdigit():
        number2 = int(number2)
        context.user_data['number2'] = number2
        update.message.reply_text('Press "=" key to get the result.')
        return OPERATION
    else:
        update.message.reply_text('This is not a number.')


def operation(update, context):
    user = update.message.from_user
    logger.info('User typed a key to get the result.: %s: %s',
                user.first_name, update.message.text)

    number1 = context.user_data.get('number1')
    number2 = context.user_data.get('number2')
    user_choice = context.user_data.get('user_choice')

    if user_choice == 'ADD':
        operator = '+'
        result = number1 + number2
    if user_choice == 'SUBTRACT':
        operator = '-'
        result = number1 - number2
    if user_choice == 'MULTIPLY':
        operator = 'x'
        result = number1 * number2
    if user_choice == 'DIVIDE':
        operator = '/'
        try:
            result = number1 / number2
        except:
            update.message.reply_text('Cannot divide by zero.')
    if user_choice == 'POWER':
        operator = '^'
        result = number1 ** number2

    update.message.reply_text(
        f'Результат: {number1} {operator} {number2} = {result}')
    return start(update, context)


def cancel(update, _):
    user = update.message.from_user
    logger.info('User %s ended the work.', user.first_name)
    update.message.reply_text('Bye')
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOICE: [MessageHandler(Filters.text, choice)],
            NUMBER1: [MessageHandler(Filters.text, number1)],
            NUMBER2: [MessageHandler(Filters.text, number2)],
            OPERATION: [MessageHandler(Filters.text, operation)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conversation_handler)

    print('server started')
    updater.start_polling()
    updater.idle()
