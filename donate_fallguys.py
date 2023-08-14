from telebot import types
from adaptive_help_func_telebot import *
from config import fallguysset
from math import ceil


### Блок Донат -> Fall Guys
def fall_guys(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Нет, не менял", callback_data="donate_fall_guys_noeditmenu")
    btn2 = types.InlineKeyboardButton("Да, менял", callback_data="donate_fall_guys_yeseditmenu")
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton("Как узнать", callback_data="donate_fall_guys_howtofind")
    markup.row(btn3)
    btn4 = types.InlineKeyboardButton("Назад", callback_data="Донат")
    markup.row(btn4)
    img_block(r'src\Donate\fallgays.jpg', message, markup, text="Вы меняли регион за последние 6 месяцев?")


def donate_fall_guys_noeditmenu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Шмяксы", callback_data="shmacks")
    btn2 = types.InlineKeyboardButton("Наборы", callback_data="fall_guys_set")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="fall_guys")
    markup.add(btn1, btn2, btn3)
    img_block(r'src\Donate\fallgays.jpg', message, markup)


def donate_fall_guys_yeseditmenu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Турция", callback_data="donate_fall_guys_noeditmenu")
    btn2 = types.InlineKeyboardButton("Другая", callback_data="Другая")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="fall_guys")
    markup.add(btn1, btn2, btn3)
    img_block(r'src\Donate\fallgays.jpg', message, markup, text="Какая страна стоит?")


def donate_fall_guys_howtofind(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Назад", callback_data="fall_guys")
    markup.add(btn1)
    img_block(r'src\Donate\fallgays.jpg', message, markup, text="Инструкция будет*")


def shmacks(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("1000", callback_data="1000shmacks")
    btn2 = types.InlineKeyboardButton("2800", callback_data="2800shmacks")
    btn3 = types.InlineKeyboardButton("5000", callback_data="5000shmacks")
    btn4 = types.InlineKeyboardButton("13500", callback_data="13500shmacks")
    btn5 = types.InlineKeyboardButton("Назад", callback_data="donate_fall_guys_noeditmenu")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    img_block(r'src\Donate\fg-vbucks.jpg', message, markup)


def fall_guys_set(message):
    markup = types.InlineKeyboardMarkup()
    name_fallguysset = [i for i in fallguysset.keys()]
    count_el_page = len(name_fallguysset)
    if count_el_page % 2 == 0:
        for i in range(0, count_el_page, 2):
            markup.row(types.InlineKeyboardButton(name_fallguysset[i], callback_data=name_fallguysset[i]),
                        types.InlineKeyboardButton(name_fallguysset[i + 1], callback_data=name_fallguysset[i + 1]))
    else:
        for i in range(0, count_el_page, 2):
            try:
                markup.row(types.InlineKeyboardButton(name_fallguysset[i], callback_data=name_fallguysset[i]),
                            types.InlineKeyboardButton(name_fallguysset[i + 1], callback_data=name_fallguysset[i + 1]))
            except:
                markup.row(types.InlineKeyboardButton(name_fallguysset[i], callback_data=name_fallguysset[i]))
    markup.row(types.InlineKeyboardButton('Назад', callback_data='donate_fall_guys_noeditmenu'))
    img_block(r'src\Donate\fallgays.jpg', message, markup)
