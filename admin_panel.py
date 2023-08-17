from telebot import types
from adaptive_help_func_telebot import *
import sqlite3
from config import conn


def admfortnite(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Добавить набор", callback_data="addsetsfortnite")
    btn2 = types.InlineKeyboardButton("Удалить набор", callback_data='delsetsfortnite')
    btn3 = types.InlineKeyboardButton("Назад", callback_data='backtoadmpanel')
    markup.add(btn1, btn2, btn3)
    text_block("Вы можете изменить информацию о наборах, добавить новые наборы, а также удалить не нужные.", message, markup)


def addsetsfortnite(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Назад", callback_data="admfortnite")
    markup.add(btn1)
    text_block("Напишите название нового набора:", message, markup)
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    name = message.text
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Назад", callback_data="admfortnite")
    markup.add(btn1)
    bot.send_message(message.chat.id, 
               text="Напишите описание нового набора:".format(message.from_user), 
               reply_markup=markup)
    bot.register_next_step_handler(message, get_description, [name])


def get_description(message, l):
    description = message.text
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Назад", callback_data="admfortnite")
    markup.add(btn1)
    bot.send_message(message.chat.id, 
               text="Напишите стоимость нового набора:".format(message.from_user), 
               reply_markup=markup)
    l += [description]
    bot.register_next_step_handler(message, get_price, l)


def get_price(message, l):
    price = message.text
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Назад", callback_data="admfortnite")
    markup.add(btn1)
    bot.send_message(message.chat.id, 
               text="Отправьте фото набора:".format(message.from_user), 
               reply_markup=markup)
    l += [price]
    bot.register_next_step_handler(message, get_photo, l)


def get_photo(message, l):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Назад", callback_data="admfortnite")
    markup.add(btn1)
    bot.send_message(message.chat.id, 
               text="Готово".format(message.from_user), 
               reply_markup=markup)
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    save_path = f'src\\Donate\\{l[0]}.jpg'
    with open(save_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO kits (type, name) VALUES(%s, %s)', ('fortnite', l[0]))
    conn.commit()
    cursor.execute("SELECT id FROM kits WHERE name = %s", (l[0], ))
    rows = cursor.fetchall()
    cursor.execute('INSERT INTO kits_description (kit_id, image_link, description) VALUES(%s, %s, %s)', (rows[0][0], save_path, l[1]))
    conn.commit()


def delsetsfortnite(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    cur = conn.cursor()
    cur.execute("SELECT * FROM kits LEFT JOIN kits_description ON kits.id = kits_description.kit_id")
    rows = cur.fetchall()
    fortnitesets = [[row[2], row[6]] for row in rows]
    for name in fortnitesets:
        markup.row(types.InlineKeyboardButton(name[0], callback_data='delsetsfortnite_'+name[0]))
    markup.row(types.InlineKeyboardButton('Назад', callback_data='admfortnite'))
    text_block("Выберите набор, который хотите удалить.", message, markup)
    