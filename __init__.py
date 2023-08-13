from telebot import types
import threading
from config import bot

from adaptive_help_func_telebot import *

from egsblock_gamedlc import *
from donate_dbd import *
from donate_fallguys import *
from donate_fortnite import *


@bot.message_handler(commands=['start'])
def menu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Магазин 🛒", callback_data="Магазин 🛒")
    btn2 = types.InlineKeyboardButton("Кабинет 👤", callback_data="Кабинет 👤")
    btn3 = types.InlineKeyboardButton("Отзывы 📕", callback_data="Отзывы 📕")
    btn4 = types.InlineKeyboardButton("F.A.Q 📌", callback_data="F.A.Q 📌")
    btn5 = types.InlineKeyboardButton("Поддержка 👨‍💻", url='https://t.me/GameShopARS')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    photo = open(r'src\Menu\menu.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, reply_markup=markup)


def store(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Epic Games", callback_data="Epic Games")
    btn2 = types.InlineKeyboardButton("Steam", callback_data="Steam")
    btn3 = types.InlineKeyboardButton("Origin", callback_data="Origin")
    btn4 = types.InlineKeyboardButton("Ubisoft", callback_data="Ubisoft")
    btn5 = types.InlineKeyboardButton("Blizzard", callback_data="Blizzard")
    btn5 = types.InlineKeyboardButton("Battle.Net", callback_data="Battle.Net")
    btn6 = types.InlineKeyboardButton("Назад", callback_data="BackToMenu")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    img_block(r'src\Store\store.jpg', message, markup)


def office(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Реферальная ссылка", callback_data="Реферальная ссылка")
    btn2 = types.InlineKeyboardButton("Пополнить баланс", callback_data="Пополнить баланс")
    btn3 = types.InlineKeyboardButton("История заказов", callback_data="История заказов")
    btn4 = types.InlineKeyboardButton("Назад", callback_data="BackToMenu")
    markup.add(btn1, btn2, btn3, btn4)
    img_block(r'src\Office\office.jpg', message, markup)


def reviews(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Перейти", url='https://t.me/GameShopARS')
    btn2 = types.InlineKeyboardButton("Назад", callback_data="BackToMenu")
    markup.add(btn1, btn2)
    text_block("Здесь мы собираем отзывы наших клиентов. Вы можете задать любой вопрос участникам, кто ранее у нас делал заказы и убедиться, что всё прозрачно и честно.",
               message,
               markup)


def guide(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Перейти", url='https://t.me/GameShopARS')
    btn2 = types.InlineKeyboardButton("Назад", callback_data="BackToMenu")
    markup.add(btn1, btn2)
    text_block("Здесь мы собрали наиболее актуальные вопросы наших клиентов. Если не найдёте ответ на свой вопрос, то напишите нам в службу поддержки.",
               message,
               markup)

def egsblock(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Донат", callback_data="Донат")
    btn2 = types.InlineKeyboardButton("Покупка игр и DLC", callback_data="Покупка игр и DLC")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="Магазин 🛒")
    markup.add(btn1, btn2, btn3)
    img_block(r'src\EGS\EpicGames.jpg', message, markup)


def donate(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Fortnite", callback_data="Fortnite")
    btn2 = types.InlineKeyboardButton("Fall Guys", callback_data="Fall Guys")
    btn3 = types.InlineKeyboardButton("Dead by daylight", callback_data="Dead by daylight")
    btn4 = types.InlineKeyboardButton("Назад", callback_data="Epic Games")
    markup.add(btn1, btn2, btn3, btn4)
    img_block(r'src\Donate\donate.jpg', message, markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.message:
        if call.data == 'Магазин 🛒':
            store(call.message)

        elif call.data == 'Кабинет 👤':
            office(call.message)

        elif call.data == 'Отзывы 📕':
            reviews(call.message)

        elif call.data == 'F.A.Q 📌':
            guide(call.message)

        elif call.data == 'Epic Games':
            egsblock(call.message)

        elif call.data == 'BackToMenu':
            backtomenu(call.message)
        
        elif call.data == 'Реферальная ссылка':
            pass

        elif call.data == 'Пополнить баланс':
            pass

        elif call.data == 'История заказов':
            pass
        
        elif call.data == "Донат":
            pass

        elif call.data == "Покупка игр и DLC":
            buygamedlc(call.message)

        elif call.data == "Нет, не менял":
            noeditmenu(call.message)

        elif call.data == "Да, менял":
            yeseditmenu(call.message)

        elif call.data == "Как узнать":
            howtofind((call.message))

        elif call.data == "Игры":
            gameegs(call.message)

        elif call.data == "DLC":
            dlcegs(call.message)

        elif call.data == "Другая":
            othercountry(call.message)

        elif call.data == "Dead by daylight" or call.data == "BackDLCToDLCEGS":
            deadbydaylight(call.message)

        elif call.data.split('_')[0].isdigit() and len(call.data.split('_')) > 1:
            if call.data.split('_')[1] == 'pagedlcbuy':
                dlcNpage(call.message, int(call.data.split('_')[0]))

        elif call.data == "BackToOG":
            def function1():
                markup = types.InlineKeyboardMarkup()
                btn1 = types.InlineKeyboardButton("Назад", callback_data="Игры")
                markup.add(btn1)
                text='Зайдите на аккаунт epic games по этим данным:\nЛогин: raroci4898@chotunai.com\nПароль: arsgamestore1\nНайдите игру, которую вы хотите купить и напишите её стоимость, которая вам показана на этом аккаунте, боту в сообщении'
                photo = open(r'src\BuyGameDLC\game.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo, caption=text, reply_markup=markup)
                bot.register_next_step_handler(call.message, get_sum)
            
            def function2():
                bot.delete_message(call.message.chat.id, call.message.message_id)

            thread1 = threading.Thread(target=function1)
            thread2 = threading.Thread(target=function2)

            thread2.start()
            thread1.start()

            thread1.join()
            thread2.join()

        elif call.data == "NextPayGame":
            netxpaygame(call.message)

        

if __name__ == "__main__":
    bot.polling(none_stop=True)
