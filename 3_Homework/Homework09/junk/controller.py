import model_sum as sum
import model_sub as sub
import model_mult as mult
import model_sqrt as sqrt
import view


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token(
    "5571491845:AAFTek__yjvDFQ1sJvJL90J_OHnGWtYgqdg").build()


print('server start')
# app.add_handler(CommandHandler("hi", hi_command))
# app.add_handler(CommandHandler("time", time_command))
# app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("sub", sub_command))
app.add_handler(CommandHandler("mult", mult_command))
app.add_handler(CommandHandler("sqrt", sqrt_command))

app.run_polling()


# def button_click():
#     choice = view.get_operation()
#     # next = 'y'
#     while choice != 5:
#         if choice == 1:
#             value_a = view.get_value()
#             value_b = view.get_value()
#             sub.init(value_a, value_b)
#             result = sub.calc()
#         elif choice == 2:
#             value_a = view.get_value()
#             value_b = view.get_value()
#             sum.init(value_a, value_b)
#             result = sum.calc()
#         elif choice == 3:
#             value_a = view.get_value()
#             value_b = view.get_value()
#             mult.init(value_a, value_b)
#             result = mult.calc()
#         elif choice == 4:
#             value_a = view.get_value()
#             sqrt.init(value_a)
#             result = sqrt.calc()
#         view.view_data('result', result)
#         # next = view.ask_if_continue()
#         choice = view.get_operation()
