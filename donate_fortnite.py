from telebot import types
from adaptive_help_func_telebot import *
from config import conn
import requests


def fortnite(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Через смену региона Epic Games", callback_data="epicgamesaccount")
    btn2 = types.InlineKeyboardButton("Через учетную запись Xbox", callback_data="xboxaccout")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="Донат")
    btn4 = types.InlineKeyboardButton("Главное меню", callback_data="BackToMenu")
    markup.add(btn1, btn2, btn3, btn4)
    img_block(r'src\Donate\fortnite.jpg', message, markup)


def epicgamesaccount(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Нет, не менял", callback_data="epicgamesaccountnoeditmenu")
    btn2 = types.InlineKeyboardButton("Да, менял", callback_data="epicgamesaccountyeseditmenu")
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton("Как узнать", callback_data="epicgamesaccounthowtofind")
    markup.row(btn3)
    btn4 = types.InlineKeyboardButton("Назад", callback_data="fortnite")
    btn5 = types.InlineKeyboardButton("Главное меню", callback_data="BackToMenu")
    markup.row(btn4, btn5)
    img_block(r'src\Donate\fortnite_egs.jpg', message, markup, text="Вы меняли регион за последние 6 месяцев?")

  
def epicgamesaccount_noeditmenu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("V-bucks", callback_data="vbucksegs")
    btn2 = types.InlineKeyboardButton("Наборы", callback_data="setsegsxboxegs")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="epicgamesaccount")
    btn4 = types.InlineKeyboardButton("Главное меню", callback_data="BackToMenu")
    markup.add(btn1, btn2, btn3, btn4)
    img_block(r'src\Donate\vbuck_and_sets_1.jpg', message, markup)


def epicgamesaccount_yeseditmenu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Турция", callback_data="epicgamesaccountnoeditmenu")
    btn2 = types.InlineKeyboardButton("Другая", callback_data="epicgamesaccountanother")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="epicgamesaccount")
    btn4 = types.InlineKeyboardButton("Главное меню", callback_data="BackToMenu")
    markup.add(btn1, btn2, btn3, btn4)
    img_block(r'src\Donate\fortnite_egs.jpg', message, markup, text="Какая страна стоит?")


def epicgamesaccount_howtofind(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Назад", callback_data="epicgamesaccount")
    btn2 = types.InlineKeyboardButton("Главное меню", callback_data="BackToMenu")
    markup.add(btn1, btn2)
    img_block(r'src\Donate\fortnite_egs.jpg', message, markup, text="Инструкция будет*")


def epicgamesaccount_another(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Через учетную запись Xbox", callback_data="xboxaccout")
    btn2 = types.InlineKeyboardButton("Главное меню", callback_data="BackToMenu")
    markup.add(btn1, btn2)
    img_block(r'src\Donate\fortnite_egs.jpg', message, markup, text="К сожалению мы не сможем изменить вам регион, так как за последние 6 месяцев он был изменен.")


def xboxaccout(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Да, привязана", callback_data="xboxaccoutyeslinked")
    btn2 = types.InlineKeyboardButton("Как привязать?", callback_data="xboxaccouthowlinked")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="fortnite")
    btn4 = types.InlineKeyboardButton("Главное меню", callback_data="BackToMenu")
    markup.add(btn1, btn2, btn3, btn4)
    img_block(r'src\Donate\fortnite_xbox.jpg', message, markup, text="У вас привязана учетная запись microsoft xbox к epic games?")


def xboxaccout_yeslinked(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("V-bucks", callback_data="vbucksxbox")
    btn2 = types.InlineKeyboardButton("Наборы", callback_data="setsegsxboxxbox")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="fortnite")
    btn4 = types.InlineKeyboardButton("Главное меню", callback_data="BackToMenu")
    markup.add(btn1, btn2, btn3, btn4)
    img_block(r'src\Donate\vbuck_and_sets_2.jpg', message, markup)


def xboxaccout_howlinked(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Назад", callback_data="BackToxboxaccout")
    btn2 = types.InlineKeyboardButton("Главное меню", callback_data="BackToMenu")
    markup.add(btn1, btn2)
    text_block("Инструкция будет*", message, markup)


def vbucks(message, back):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("1000", callback_data="1000_vbucks"+"_"+back)
    btn2 = types.InlineKeyboardButton("2800", callback_data="2800_vbucks"+"_"+back)
    btn3 = types.InlineKeyboardButton("5000", callback_data="5000_vbucks"+"_"+back)
    btn4 = types.InlineKeyboardButton("13500", callback_data="13500_vbucks"+"_"+back)
    btn5 = types.InlineKeyboardButton("Назад", callback_data=back)
    btn6 = types.InlineKeyboardButton("Главное меню", callback_data="BackToMenu")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    img_block(r'src\Donate\fortnite_vbucks.jpg', message, markup)


def N_vbucks(message, N, back):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Купить", callback_data=f"{N}_vbucks_buy")
    btn2 = types.InlineKeyboardButton("Добавить в корзину", callback_data=f"{N}_vbucks_buy")
    btn3 = types.InlineKeyboardButton("Назад", callback_data=back)
    btn4 = types.InlineKeyboardButton("Главное меню", callback_data="BackToMenu")
    markup.add(btn1, btn2, btn3, btn4)
    img_block(f'src\\Donate\\{N}_vbucks.jpg', message, markup)


def sets_egs_xbox(message, back):
    markup = types.InlineKeyboardMarkup()
    cur = conn.cursor()
    cur.execute("SELECT * FROM kits LEFT JOIN kits_description ON kits.id = kits_description.kit_id")
    rows = cur.fetchall()
    fortnitesets = [[row[2], row[6]] for row in rows]
    for name in fortnitesets:
        name_callback = 'setsfortnite_'+ name[0] + "_" + back
        markup.row(types.InlineKeyboardButton(name[0], callback_data=name_callback))
    markup.row(types.InlineKeyboardButton('Назад', callback_data=back), types.InlineKeyboardButton("Главное меню", callback_data="BackToMenu"))
    img_block('src\\Donate\\fortnite_sets.jpg', message, markup)


def name_sets_egs_xbox(message, name, back):
    # conn = sqlite3.connect('DataBase\\database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kits LEFT JOIN kits_description ON kits.id = kits_description.kit_id WHERE name = %s", (name, ))
    rows = cursor.fetchall()
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Купить", callback_data=f"{rows[0][2]}_buy")
    btn2 = types.InlineKeyboardButton("Добавить в корзину", callback_data=f"{rows[0][2]}_buy")
    btn3 = types.InlineKeyboardButton("Назад", callback_data=back)
    btn4 = types.InlineKeyboardButton("Главное меню", callback_data="BackToMenu")
    markup.add(btn1, btn2, btn3, btn4)
    img_block(f'src\\Donate\\{name}.jpg', message, markup, rows[0][6])