from telebot import types
from adaptive_help_func_telebot import *


### Блок Донат -> Fall Guys
def fall_guys(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Нет, не менял", callback_data="Нет, не менял DBD")
    btn2 = types.InlineKeyboardButton("Да, менял", callback_data="Да, менял")
    btn3 = types.InlineKeyboardButton("Как узнать", callback_data="Как узнать")
    btn4 = types.InlineKeyboardButton("Назад", callback_data="Донат")
    markup.add(btn1, btn2, btn3, btn4)
    img_block(r'src\BuyGameDLC\gamedlc.jpg', message, markup)


def donate_fall_guys_noeditmenu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Золотые клетки", callback_data="Золотые клетки")
    btn2 = types.InlineKeyboardButton("Назад", callback_data="Dead by daylight")
    markup.add(btn1, btn2)
    img_block(r'src\BuyGameDLC\gamedlc.jpg', message, markup)


def donate_fall_guys_yeseditmenu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Турция", callback_data="Турция")
    btn2 = types.InlineKeyboardButton("Другая", callback_data="Другая")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="Dead by daylight")
    markup.add(btn1, btn2, btn3)
    img_block(r'src\BuyGameDLC\gamedlc.jpg', message, markup, text="Какая страна стоит?")


def donate_fall_guys_howtofind(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Назад", callback_data="Dead by daylight")
    markup.add(btn1)
    img_block(r'src\BuyGameDLC\gamedlc.jpg', message, markup, text="Инструкция будет*")