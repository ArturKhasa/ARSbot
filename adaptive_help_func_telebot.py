import telebot
import threading
from telebot import types
from config import bot
from PIL import Image, ImageFont, ImageDraw
from math import floor, ceil


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


def feedbackc_card(name, text, url_img):
    font1 = ImageFont.truetype("Arial Unicode MS.ttf", 100)
    font2 = ImageFont.truetype("Arial Unicode MS.ttf", 60)
# Нет, это не скам, не обман и так далее. Мы успешно зарекомендовали себя на рынке негативных отзывов у нас нет, как и обманутых клиентов.
    # text_color = (0, 0, 0)
    if ceil(len(text) / 46) > 7:
        width, height = 2430, 800 + (ceil(len(text) / 46 - 7)) * 60
    else:
        width, height = 2430, 800

    if len(text) > 46:
        for i in range(1, floor(len(text) / 46) + 1):
            n = i * 46
            while text[n] != ' ':
                n-=1
            text = text[:n] + '\n' + text[n+1:]

    im = Image.open('background.png')
    image = im.crop((0, 0, width, height))
    draw = ImageDraw.Draw(image)

    img = Image.open(url_img)
    img = img.resize((385,364))
    image.paste(img, (69,66))

    draw.text((550, 66), f"{name}", font=font1)
    draw.text((550, 200), text, font=font2)

    image.save(url_img, dpi=[300,300], quality=80)