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
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


CHOICE_OP, CHOICE_MATH, NUMBER1, NUMBER2, OPERATION,\
    COMPLEX1, COMPLEX2, OPERATION_COMPLEX = range(8)


def start(update, _):
    reply_keyboard = [['INTEGER OR RATIONAL NUMBERS',
                       'COMPLEX NUMBERS', 'CANCEL'], ]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        '\nChoose operation by pressing corresponding button.\n', reply_markup=markup_key)
    return CHOICE_OP


def choice_op(update, context):
    user = update.message.from_user
    logger.info('Operation choice: %s: %s',
                user.first_name, update.message.text)
    user_choice = update.message.text
    if user_choice == 'INTEGER OR RATIONAL NUMBERS':
        reply_keyboard = [['ADD', 'SUBTRACT'],
                          ['DIVIDE', 'MULTIPLY']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard)
        update.message.reply_text(
            'Choose math operation.', reply_markup=markup_key)

        return CHOICE_MATH

    if user_choice == 'COMPLEX NUMBERS':
        context.bot.send_message(
            update.effective_chat.id, 'Enter Real and Imaginary parts of number separated by SPACE: ')

        return COMPLEX1

    if user_choice == 'CANCEL':
        return cancel(update, context)


def choice_math(update, context):
    user = update.message.from_user
    logger.info('Math operation choice: %s: %s',
                user.first_name, update.message.text)
    math_choice = update.message.text
    context.user_data['math_choice'] = math_choice
    update.message.reply_text('Enter the first number.')
    return NUMBER1


def number1(update, context):
    user = update.message.from_user
    logger.info('User has entered a number: %s: %s',
                user.first_name, update.message.text)
    number1 = update.message.text
    temp1 = number1.replace('-', '')
    temp2 = temp1.replace('.', '')
    if temp1.find('.') != -1 and temp2.isdigit():
        number1 = float(number1)
        print(type(number1))
        context.user_data['number1'] = number1
        update.message.reply_text('Enter the second number.')
        return NUMBER2
    elif number1.isdigit():
        number1 = int(number1)
        print(type(number1))
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
    temp1 = number2.replace('-', '')
    temp2 = temp1.replace('.', '')
    if temp1.find('.') != -1 and temp2.isdigit():
        number2 = float(number2)
        context.user_data['number2'] = number2
        update.message.reply_text('Press any key to get the result.')
        return OPERATION
    elif number2.isdigit():
        number2 = int(number2)
        context.user_data['number2'] = number2
        update.message.reply_text('Press any key to get the result.')
        return OPERATION
    else:
        update.message.reply_text('This is not a number.')


def operation(update, context):
    user = update.message.from_user
    logger.info('User typed a key to get the result.: %s: %s',
                user.first_name, update.message.text)

    number1 = context.user_data.get('number1')
    number2 = context.user_data.get('number2')
    math_choice = context.user_data.get('math_choice')

    if math_choice == 'ADD':
        operator = '+'
        result = number1 + number2
    if math_choice == 'SUBTRACT':
        operator = '-'
        result = number1 - number2
    if math_choice == 'MULTIPLY':
        operator = 'x'
        result = number1 * number2
    if math_choice == 'DIVIDE':
        operator = '/'
        try:
            result = number1 / number2
        except:
            update.message.reply_text('Cannot divide by zero.')

    update.message.reply_text(
        f'Результат: {number1} {operator} {number2} = {result}')
    return start(update, context)


def complex1(update, context):
    user = update.message.from_user
    logger.info('User has entered the first complex number: %s: %s',
                user.first_name, update.message.text)
    user_choice = update.message.text
    test = user_choice.replace('-', '')
    if ' ' in test and (test.replace(' ', '')).isdigit():
        user_choice = user_choice.split(' ')
        complex1 = complex(int(user_choice[0]), int(user_choice[1]))
        context.user_data['complex1'] = complex1
        update.message.reply_text(
            f'The first number {complex1}, Enter Real and Imaginary parts of the second number separated by SPACE: ')
        return COMPLEX2
    else:
        update.message.reply_text(
            'Incorrect entry. Enter Real and Imaginary parts of the number separated by SPACE: ')


def complex2(update, context):
    user = update.message.from_user
    logger.info('User has entered the second complex number: %s: %s',
                user.first_name, update.message.text)
    user_choice = update.message.text
    test = user_choice.replace('-', '')
    if ' ' in test and (test.replace(' ', '')).isdigit():
        user_choice = user_choice.split(' ')
        complex2 = complex(int(user_choice[0]), int(user_choice[1]))
        context.user_data['complex2'] = complex2
        update.message.reply_text(f'The second number is {complex2}')

        reply_keyboard = [['ADD', 'SUBTRACT'],
                          ['DIVIDE', 'MULTIPLY']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard)
        update.message.reply_text(
            'Choose math operation.', reply_markup=markup_key)

        return OPERATION_COMPLEX
    else:
        update.message.reply_text(
            'Incorrect entry. Enter Real and Imaginary parts of the number separated by SPACE: ')


def operation_complex(update, context):
    user = update.message.from_user
    logger.info('User has chosen operation: %s: %s',
                user.first_name, update.message.text)
    complex1 = context.user_data.get('complex1')
    complex2 = context.user_data.get('complex2')
    user_choice = update.message.text
    if user_choice == 'ADD':
        result = complex1 + complex2
        operator = '+'
    if user_choice == 'SUBTRACT':
        result = complex1 - complex2
        operator = '-'
    if user_choice == 'MULTIPLY':
        result = complex1 * complex2
        operator = 'x'
    if user_choice == 'DIVIDE':
        try:
            result = complex1 / complex2
            operator = '/'
        except:
            update.message.reply_text('Cannot divide by zero')
    update.message.reply_text(
        f'Result is: {complex1} {operator} {complex2} = {result}')
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
            CHOICE_OP: [MessageHandler(Filters.text, choice_op)],
            CHOICE_MATH: [MessageHandler(Filters.text, choice_math)],
            NUMBER1: [MessageHandler(Filters.text, number1)],
            NUMBER2: [MessageHandler(Filters.text, number2)],
            COMPLEX1: [MessageHandler(Filters.text, complex1)],
            COMPLEX2: [MessageHandler(Filters.text, complex2)],
            OPERATION: [MessageHandler(Filters.text, operation)],
            OPERATION_COMPLEX: [MessageHandler(Filters.text, operation_complex)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conversation_handler)

    print('server started')
    updater.start_polling()
    updater.idle()
