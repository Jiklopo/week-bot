import os
from datetime import datetime, timedelta
from telebot import TeleBot, types

TOKEN = os.getenv('WEEK_BOT_TOKEN')
SEMESTER_START = datetime.strptime(os.getenv('SEMESTER_START') or '31/08/20 00:00:00', '%d/%m/%y %H:%M:%S')
bot = TeleBot(TOKEN)


def get_current_week():
    d = datetime.today() + timedelta(hours=6) - SEMESTER_START
    return f'Текущая неделя: {d.days // 7 + 1}'


@bot.message_handler(func=lambda msg: True)
def default_handler(message):
    bot.reply_to(message, get_current_week())


@bot.inline_handler(lambda query: True)
def inline_week_number(query):
    r = types.InlineQueryResultArticle(id='1', title='Номер недели',
                                       input_message_content=types.InputTextMessageContent(
                                           message_text=get_current_week()))
    bot.answer_inline_query(query.id, [r])
