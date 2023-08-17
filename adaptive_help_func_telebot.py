import telebot
import threading
from telebot import types
from config import bot

def img_block(src, message, markup, text=''):
    with open(src, 'rb') as updated_photo:
        bot.edit_message_media(
            media=telebot.types.InputMediaPhoto(updated_photo),
            chat_id=message.chat.id,
                               message_id=message.message_id,
                               reply_markup=markup)
    if text != '':
        bot.edit_message_caption(caption=text,
                                chat_id=message.chat.id,
                                message_id=message.message_id,
                                reply_markup=markup)


def text_block(text, message, markup):
    def function1():
        bot.send_message(message.chat.id, 
                     text=text.format(message.from_user), 
                     reply_markup=markup)

    def function2():
        bot.delete_message(message.chat.id, 
                       message.message_id)
    
    thread1 = threading.Thread(target=function1)
    thread2 = threading.Thread(target=function2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


def backtomenu(message):
    def function1():
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Магазин 🛒", callback_data="Магазин 🛒")
        btn2 = types.InlineKeyboardButton("Кабинет 👤", callback_data="Кабинет 👤")
        btn3 = types.InlineKeyboardButton("Отзывы 📕", callback_data="Отзывы 📕")
        btn4 = types.InlineKeyboardButton("F.A.Q 📌", callback_data="F.A.Q 📌")
        btn5 = types.InlineKeyboardButton("Поддержка 👨‍💻", url='https://t.me/GameShopARS')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        photo = open(r'src\Menu\menu.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, reply_markup=markup)
    
    def function2():
        bot.delete_message(message.chat.id, message.message_id)

    thread1 = threading.Thread(target=function1)
    thread2 = threading.Thread(target=function2)

    thread2.start()
    thread1.start()

    thread1.join()
    thread2.join()


def backtoadmpanel(message):
    def function1():
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("Fortnite", callback_data="admfortnite")
        btn2 = types.InlineKeyboardButton("Выйти с админ панели", callback_data='BackToMenu')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, 
                        text="Выберите блок, с которым будете работать.", 
                        reply_markup=markup)
    
    def function2():
        bot.delete_message(message.chat.id, message.message_id)

    thread1 = threading.Thread(target=function1)
    thread2 = threading.Thread(target=function2)

    thread2.start()
    thread1.start()

    thread1.join()
    thread2.join()
