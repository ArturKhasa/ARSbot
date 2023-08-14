from telebot import types
from adaptive_help_func_telebot import *
from math import ceil
from config import fortnitesets


def fortnite(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Через смену региона Epic Games", callback_data="epicgamesaccount")
    btn2 = types.InlineKeyboardButton("Через учетную запись Xbox", callback_data="xboxaccout")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="Донат")
    markup.add(btn1, btn2, btn3)
    img_block(r'src\Donate\fortnite.jpg', message, markup)


def epicgamesaccount(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Нет, не менял", callback_data="epicgamesaccount_noeditmenu")
    btn2 = types.InlineKeyboardButton("Да, менял", callback_data="epicgamesaccount_yeseditmenu")
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton("Как узнать", callback_data="epicgamesaccount_howtofind")
    markup.row(btn3)
    btn4 = types.InlineKeyboardButton("Назад", callback_data="fortnite")
    markup.row(btn4)
    img_block(r'src\Donate\fortnite_egs.jpg', message, markup, text="Вы меняли регион за последние 6 месяцев?")

  
def epicgamesaccount_noeditmenu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("V-bucks", callback_data="vbucks")
    btn2 = types.InlineKeyboardButton("Наборы", callback_data="sets_egs_xbox")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="epicgamesaccount")
    markup.add(btn1, btn2, btn3)
    img_block(r'src\Donate\vbuck_and_sets_1.jpg', message, markup)


def epicgamesaccount_yeseditmenu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Турция", callback_data="epicgamesaccount_noeditmenu")
    btn2 = types.InlineKeyboardButton("Другая", callback_data="epicgamesaccount_another")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="epicgamesaccount")
    markup.add(btn1, btn2, btn3)
    img_block(r'src\Donate\fortnite_egs.jpg', message, markup, text="Какая страна стоит?")


def epicgamesaccount_howtofind(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Назад", callback_data="epicgamesaccount")
    markup.add(btn1)
    img_block(r'src\Donate\fortnite_egs.jpg', message, markup, text="Инструкция будет*")


def epicgamesaccount_another(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Через учетную запись Xbox", callback_data="xboxaccout")
    btn2 = types.InlineKeyboardButton("Главное меню", callback_data="BackToMenu")
    markup.add(btn1, btn2)
    img_block(r'src\Donate\fortnite_egs.jpg', message, markup, text="К сожалению мы не сможем изменить вам регион, так как за последние 6 месяцев он был изменен.")


def xboxaccout(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Да, привязана", callback_data="xboxaccout_yeslinked")
    btn2 = types.InlineKeyboardButton("Как привязать?", callback_data="xboxaccout_howlinked")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="fortnite")
    markup.add(btn1, btn2, btn3)
    img_block(r'src\Donate\fortnite_xbox.jpg', message, markup, text="У вас привязана учетная запись microsoft xbox к epic games?")


def xboxaccout_yeslinked(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("V-bucks", callback_data="vbucks")
    btn2 = types.InlineKeyboardButton("Наборы", callback_data="sets_egs_xbox")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="fortnite")
    markup.add(btn1, btn2, btn3)
    img_block(r'src\Donate\vbuck_and_sets_2.jpg', message, markup)


def xboxaccout_howlinked(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Назад", callback_data="BackToxboxaccout")
    markup.add(btn1)
    text_block("Инструкция будет*", message, markup)


def vbucks(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("1000", callback_data="1000_vbucks")
    btn2 = types.InlineKeyboardButton("2800", callback_data="2800_vbucks")
    btn3 = types.InlineKeyboardButton("5000", callback_data="5000_vbucks")
    btn4 = types.InlineKeyboardButton("13500", callback_data="13500_vbucks")
    btn5 = types.InlineKeyboardButton("Назад", callback_data="fortnite")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    img_block(r'src\Donate\fortnite_vbucks.jpg', message, markup)


def N_vbucks(message, N):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Купить", callback_data=f"{N}_vbucks_buy")
    btn2 = types.InlineKeyboardButton("Добавить в корзину", callback_data=f"{N}_vbucks_buy")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="vbucks")
    markup.add(btn1, btn2, btn3)
    img_block(f'src\\Donate\\{N}_vbucks.jpg', message, markup)


def sets_egs_xbox(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    for name in fortnitesets:
        markup.row(types.InlineKeyboardButton(name, callback_data=name))
    markup.row(types.InlineKeyboardButton('Назад', callback_data='fortnite'))
    img_block(r'src\Donate\fortnite_sets.jpg', message, markup)