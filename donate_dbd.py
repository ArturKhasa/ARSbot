from telebot import types
from adaptive_help_func_telebot import *


### Блок Донат -> Dead By Daylight
def dead_by_daylight(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Нет, не менял", callback_data="donatedeadbydaylightnoeditmenu")
    btn2 = types.InlineKeyboardButton("Да, менял", callback_data="donatedeadbydaylightyeseditmenu")
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton("Как узнать", callback_data="donatedeadbydaylighthowtofind")
    markup.row(btn3)
    btn4 = types.InlineKeyboardButton("Назад", callback_data="Донат")
    btn5 = types.InlineKeyboardButton("Главное меню", callback_data="BackToMenu")
    markup.row(btn4, btn5)
    img_block(r'src\Donate\deadbydaylight.jpg', message, markup, text="Вы меняли регион за последние 6 месяцев?")


def donate_dead_by_daylight_noeditmenu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Золотые клетки", callback_data="goldencage")
    btn2 = types.InlineKeyboardButton("Назад", callback_data="deadbydaylight")
    btn3 = types.InlineKeyboardButton("Главное меню", callback_data="BackToMenu")
    markup.add(btn1, btn2, btn3)
    img_block(r'src\Donate\deadbydaylight.jpg', message, markup)


def donate_dead_by_daylight_yeseditmenu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Турция", callback_data="donatedeadbydaylightnoeditmenu")
    btn2 = types.InlineKeyboardButton("Другая", callback_data="othercountry")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="deadbydaylight")
    btn4 = types.InlineKeyboardButton("Главное меню", callback_data="BackToMenu")
    markup.add(btn1, btn2, btn3, btn4)
    img_block(r'src\Donate\deadbydaylight.jpg', message, markup, text="Какая страна стоит?")


def donate_dead_by_daylight_howtofind(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Назад", callback_data="deadbydaylight")
    btn2 = types.InlineKeyboardButton("Главное меню", callback_data="BackToMenu")
    markup.add(btn1, btn2)
    img_block(r'src\Donate\deadbydaylight.jpg', message, markup, text="Инструкция будет*")


def golden_cage(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("500", callback_data="500goldencage")
    btn2 = types.InlineKeyboardButton("1100", callback_data="11000goldencage")
    btn3 = types.InlineKeyboardButton("2250", callback_data="2250goldencage")
    btn4 = types.InlineKeyboardButton("4025", callback_data="4025goldencage")
    btn5 = types.InlineKeyboardButton("6000", callback_data="6000goldencage")
    btn6 = types.InlineKeyboardButton("12500", callback_data="12500goldencage")
    btn7 = types.InlineKeyboardButton("Назад", callback_data="donatedeadbydaylightnoeditmenu")
    btn8 = types.InlineKeyboardButton("Главное меню", callback_data="BackToMenu")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    img_block(r'src\Donate\dbd-golden_cage.jpg', message, markup)