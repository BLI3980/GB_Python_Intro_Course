from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from pathlib import Path


def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open(Path.cwd() / '3_Homework\Homework09\calc\db.csv', 'a')
    file.write(
        f'{update.effective_user.first_name}, {update.effective_user.id}. {update.message.text}\n')
    file.close()
