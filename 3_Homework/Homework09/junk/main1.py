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
    Dispatcher
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# CHOICE, NUMBER1, NUMBER2, OPERATION = range(4)
ENTRY_CHECK1, ENTRY_CHECK2, ENTRY_CHECK_SUBS_1, ENTRY_CHECK_SUBS_2, \
    NUMBER1_AND_OPERATOR, NUMBER2, CANCEL = range(7)


def start(update, _):
    reply_keyboard = [['7', '8', '9', '/'], ['4', '5', '6', '*'], ['1', '2', '3', '-'],
                      ['+/-', '0', '.', '+'], ['x^2', 'Sqrt(x)', 'x^y', '='],
                      ]
    # reply_keyboard = [['ADD', 'SUBTRACT', 'MULTIPLY'],
    #                   ['DIVIDE', 'POWER', 'END']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard)
    update.message.reply_text(
        'Type the operation.', reply_markup=markup_key)
    return ENTRY_CHECK1

# Check correctness of the first symbol entry:
# The first symbol of operation is either '-' or a digit


# def entry_check1(update, context):
#     user = update.message.from_user
#     logger.info('Operation choice: %s: %s',
#                 user.first_name, update.message.text)
#     is_OK = False
#     while not is_OK:
#         try:
#             entry = update.message.text
#             context.user_data['entry'] = entry
#             # entry = input('Enter: ')
#             if entry.isdigit() or entry == '-':
#                 is_OK = True
#             else:
#                 print('Only digit or "-" sign are accepted at this point.')
#         except:
#             print('How did you manage to get here?')
#     print(entry)
#     return ENTRY_CHECK2

def entry_check1(update, context):
    user = update.message.from_user
    logger.info('Operation choice: %s: %s',
                user.first_name, update.message.text)
    # entry1 = update.message.text
    # context.user_data['entry1'] = entry1
    is_OK = False
    while not is_OK:
        try:
            entry1 = update.message.text
            context.user_data['entry1'] = entry1
            # entry = input('Enter: ')
            if entry1.isdigit() or entry1 == '-':
                is_OK = True
            else:
                update.message.reply_text(
                    'Only digit or "-" sign are accepted at this point.')
                # print('Only digit or "-" sign are accepted at this point.')
        except:
            print('How did you manage to get here?')
    print(1, entry1)
    return ENTRY_CHECK2

# Check correctness of the second symbol entry:
# IF the first symbol was '-', ONLY a digit can the the second,
# ELSE either 1) a digit or 2) '.' or 3) any of simple math operators (+, -, *, /)
# can the second


def entry_check2(update, context):
    user = update.message.from_user
    logger.info('Operation choice: %s: %s',
                user.first_name, update.message.text)
    entry1 = context.user_data.get('entry1')
    # entry2 = update.message.text
    math_signs = '+-*/'
    is_OK = False
    while not is_OK:
        if entry1 == '-':
            try:
                entry2 = update.message.text
                if entry2.isdigit():
                    is_OK = True
                else:
                    update.message.reply_text(
                        'Only digit entry is accepted at this point.')
                    # start(update, _)
                    # print('Only digit entry is accepted at this point.')
            except:
                print('How did you manage to get here?')
        else:
            try:
                entry2 = update.message.text
                if entry2.isdigit() or entry2 == '.' or entry2 in math_signs:
                    is_OK = True
                else:
                    print(
                        'Only digit, "." or math operators are accepted at this point.')
            except:
                print('How did you manage to get here?')
    entry2 = entry1+entry2
    print(entry2)
    context.user_data['entry2'] = entry2
    print(entry2)

    # print(2, entry1, entry2)
    return NUMBER1_AND_OPERATOR


# Check correctness of the third and subsequent entries until a math operator:
# IF the previous symbol was '.', ONLY a digit can be the next;
# IF the previous symbol was not '.', but '.' was earlier, 1) a digit or 2) a math
# operator can be the next;
# IF '.' was not entered previously, 1) a digit or 2) '.' or 3) a math operator
# can be the next;
def entry_check_subs_1(update, context, previous):
    user = update.message.from_user
    logger.info('Operation choice: %s: %s',
                user.first_name, update.message.text)
    math_signs = '+-*/'
    is_OK = False
    while not is_OK:
        if previous[-1] == '.':
            try:
                entry_sub = update.message.text
                if entry_sub.isdigit():
                    is_OK = True
                else:
                    print('Only digit entry is accepted at this point.')
            except:
                print('How did you manage to get here?')
        elif '.' in previous and previous[-1] != '.':
            try:
                entry_sub = update.message.text
                if entry_sub.isdigit() or entry_sub in math_signs:
                    is_OK = True
                else:
                    print('Only digit or math operators are accepted at this point.')
            except:
                print('How did you manage to get here?')
        else:
            try:
                entry_sub = update.message.text
                if entry_sub.isdigit() or entry_sub == '.' or entry_sub in math_signs:
                    is_OK = True
                else:
                    print(
                        'Only digit, "." or math operators are accepted at this point.')
            except:
                print('How did you manage to get here?')
    context.user_data['entry_sub'] = entry_sub
    print(entry_sub)
    print(type(entry_sub))
    return entry_sub


# Check correctness of the third and subsequent entries until a '=' sign':
# Same logic as in the method above, except '=' is the stop trigger.
def entry_check_subs_2(previous, math_signs):
    is_OK = False
    while not is_OK:
        if previous[-1] == '.':
            try:
                entry = input('Enter: ')
                if entry.isdigit():
                    is_OK = True
                else:
                    print('Only digit entry is accepted at this point.')
            except:
                print('How did you manage to get here?')
        elif '.' in previous and previous[-1] != '.':
            try:
                entry = input('Enter: ')
                if entry.isdigit() or entry in math_signs:
                    is_OK = True
                else:
                    print('Only digit or "=" sign are accepted at this point.')
            except:
                print('How did you manage to get here?')
        else:
            try:
                entry = input('Enter: ')
                if entry.isdigit() or entry == '.' or entry in math_signs:
                    is_OK = True
                else:
                    print('Only digit, "." or "=" sign are accepted at this point.')
            except:
                print('How did you manage to get here?')
    return entry


# Handling the entry of the first number and math operator
def number1_and_operator(update, context):
    global operators
    # print(3, operators)
    # entry1 = entry_check1(update, context)
    # context.user_data['entry1'] = entry1
    # reply_keyboard = [['7', '8', '9', '/'], ['4', '5', '6', '*'], ['1', '2', '3', '-'],
    #                   ['+/-', '0', '.', '+'], ['x^2', 'Sqrt(x)', 'x^y', '='],
    #                   ]
    # markup_key = ReplyKeyboardMarkup(reply_keyboard)
    # update.message.reply_text(
    #     'Type the next digit, symbol or math operator.', reply_markup=markup_key)

    # entry2 = update.message.text
    # context.user_data['entry2'] = entry2
    # # entry2 = entry_check2(update, context)
    # print(4, entry1, entry2)
    # return ConversationHandler.END
    # entry1 = context.user_data.get('entry1')
    entry2 = context.user_data.get('entry2')
    print(entry2)
    print(type(entry2))
    while entry2[-1] not in operators:
        entry2 += entry_check_subs_1(update, context, entry2)
        print('entry2', entry2)

    if '.' in entry2:
        operand1 = float(entry2[:-1])
    else:
        operand1 = int(entry2[:-1])
    operator = entry2[-1]
    print(operand1)
    print(operator)
    # return (operand1, operator)
    return ConversationHandler.END


# Handling the entry of the second number until equal sign
def number2():
    global equal
    entry1 = entry_check1()
    entry2 = entry_check2(entry1, equal)
    while entry2[-1] not in equal:
        entry2 += entry_check_subs_2(entry2, equal)

    if '.' in entry2:
        operand2 = float(entry2[:-1])
    else:
        operand2 = int(entry2[:-1])
    # operator = entry2[-1]
    # print(operand2)
    # print(operator)
    return (operand2)

# Performing the actual math operation and giving the result


def operation(operand1, operator, operand2):
    if operator == '+':
        result = operand1 + operand2
    if operator == '-':
        result = operand1 - operand2
    if operator == '*':
        result = operand1 * operand2
    if operator == '/':
        result = operand1 / operand2
    print(f'{operand1} {operator} {operand2} = {result}')
    return result

# End of operation


def cancel(update, _):
    user = update.message.from_user
    logger.info('User %s ended the work.', user.first_name)
    update.message.reply_text('Bye')
    return ConversationHandler.END


operators = '+-*/'
equal = '='

# operand1, operator = number1_and_operator()
# operand2 = number2()
# print(operand1)
# print(operator)
# print(operand2)
# operation(operand1, operator, operand2)

if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            ENTRY_CHECK1: [MessageHandler(Filters.text, entry_check1)],
            ENTRY_CHECK2: [MessageHandler(Filters.text, entry_check2)],
            ENTRY_CHECK_SUBS_1: [MessageHandler(Filters.text, entry_check_subs_1)],
            ENTRY_CHECK_SUBS_2: [MessageHandler(Filters.text, entry_check_subs_2)],
            NUMBER1_AND_OPERATOR: [MessageHandler(Filters.text, number1_and_operator)],
            NUMBER2: [MessageHandler(Filters.text, number2)],
            # CHOICE: [MessageHandler(Filters.text, choice)],
            # NUMBER1: [MessageHandler(Filters.text, number1)],
            # NUMBER2: [MessageHandler(Filters.text, number2)],
            # OPERATION: [MessageHandler(Filters.text, operation)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conversation_handler)

    print('server started')
    updater.start_polling()
    updater.idle()
