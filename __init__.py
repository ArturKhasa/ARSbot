from telebot import types
import threading
from config import bot, game, admin_list
import os

from adaptive_help_func_telebot import *

from egsblock_gamedlc import *
from donate_dbd import *
from donate_fallguys import *
from donate_fortnite import *
from admin_panel import *
from PIL import Image


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


@bot.message_handler(commands=['admin'])
def admin(message):
    user_id = message.from_user.id
    if user_id in admin_list:
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("Fortnite", callback_data="admfortnite")
        # btn2 = types.InlineKeyboardButton("Fall Guys", callback_data="admfallguys")
        # btn3 = types.InlineKeyboardButton("Dead by daylight", callback_data="admdeadbydaylight")
        btn4 = types.InlineKeyboardButton("Выйти с админ панели", callback_data='BackToMenu')
        markup.add(btn1, btn4)
        bot.send_message(message.chat.id, 
                        text="Выберите блок, который нужно изменить.", 
                        reply_markup=markup)
    else:
        pass


@bot.message_handler(commands=['photo'])
def send_feedback_message(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Назад", callback_data="Отзывы 📕")
    markup.add(btn1)
    chat_id = message.chat.id
    photos = bot.get_user_profile_photos(chat_id)
    photo_id = photos.photos[0][-1].file_id
    file_info = bot.get_file(photo_id)
    file = bot.download_file(file_info.file_path)
    with open(f'time_src_ava\\{message.chat.id}.png', 'wb') as f:
        f.write(file)
    bot.send_message(message.chat.id, 
               text="Напишите Ваш отзыв:".format(message.from_user), 
               reply_markup=markup)
    bot.register_next_step_handler(message, get_feedback, [f'time_src_ava\\{message.chat.id}.png'])


def get_feedback(message, l):
    feedback = message.text
    feedbackc_card(message.chat.first_name, feedback, l[0])
    photo = open(l[0], 'rb')
    bot.send_photo(message.chat.id, photo)
    photo.close()
    os.remove(l[0])
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Назад", callback_data="Отзывы 📕")
    markup.add(btn1)
    bot.send_message(message.chat.id, 
               text="Спасибо за отзыв!".format(message.from_user), 
               reply_markup=markup)
    

def store(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Epic Games", callback_data="Epic Games")
    btn2 = types.InlineKeyboardButton("Steam", callback_data="Steam")
    btn3 = types.InlineKeyboardButton("Origin", callback_data="Origin")
    btn4 = types.InlineKeyboardButton("Ubisoft", callback_data="Ubisoft")
    btn5 = types.InlineKeyboardButton("Blizzard", callback_data="Blizzard")
    btn6 = types.InlineKeyboardButton("Battle.Net", callback_data="Battle.Net")
    btn7 = types.InlineKeyboardButton("Назад", callback_data="BackToMenu")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
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
    img_block(r"src\Menu\feedback.jpg", message, markup, "Здесь мы собираем отзывы наших клиентов. Вы можете задать любой вопрос участникам, кто ранее у нас делал заказы и убедиться, что всё прозрачно и честно.")


def guide(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Перейти", url='https://t.me/GameShopARS')
    btn2 = types.InlineKeyboardButton("Назад", callback_data="BackToMenu")
    markup.add(btn1, btn2)
    img_block(r"src\Menu\faq.jpg", message, markup, "Здесь мы собрали наиболее актуальные вопросы наших клиентов. Если не найдёте ответ на свой вопрос, то напишите нам в службу поддержки.")
    

def egsblock(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Донат", callback_data="Донат")
    btn2 = types.InlineKeyboardButton("Покупка игр и DLC", callback_data="Покупка игр и DLC")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="Магазин 🛒")
    markup.add(btn1, btn2, btn3)
    img_block(r'src\EGS\EpicGames.jpg', message, markup)


def donate(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Fortnite", callback_data="fortnite")
    btn2 = types.InlineKeyboardButton("Fall Guys", callback_data="fallguys")
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton("Dead by daylight", callback_data="deadbydaylight")
    markup.row(btn3)
    btn4 = types.InlineKeyboardButton("Назад", callback_data="Epic Games")
    markup.row(btn4)
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
            donate(call.message)

        elif call.data == "Покупка игр и DLC":
            buygamedlc(call.message)

        elif call.data == "buygamedlcnoeditmenu":
            buygamedlc_noeditmenu(call.message)

        elif call.data == "buygamedlcyeseditmenu":
            buygamedlc_yeseditmenu(call.message)

        elif call.data == "buygamedlchowtofind":
            buygamedlc_howtofind((call.message))

        elif call.data == "Игры":
            gameegs(call.message)

        elif call.data == "DLC":
            dlcegs(call.message)

        elif call.data == "othercountry":
            othercountry(call.message)

        elif call.data == "DLCBUY":
            dlcbuy(call.message)

        elif call.data.split('_')[0].isdigit() and len(call.data.split('_')) > 1:
            if call.data.split('_')[1] == 'pagedlcbuy':
                dlcNpage(call.message, int(call.data.split('_')[0]))

            elif call.data.split('_')[1] == 'vbucks':
                pass

        elif len(call.data.split('_')) > 1:
            if call.data.split('_')[0] == 'setsfortnite':
                name_sets_egs_xbox(call.message, call.data.split('_')[1])
            
            elif call.data.split('_')[0] == 'delsetsfortnite':
                os.remove(f"src\\Donate\\{call.data.split('_')[1]}.jpg")
                cursor = conn.cursor()
                cursor.execute("SELECT id FROM kits WHERE name = %s", (call.data.split('_')[1], ))
                rows = cursor.fetchall()
                cursor.execute("DELETE FROM kits_description WHERE kit_id = %s", (rows[0][0], ))
                conn.commit()
                cursor.execute("DELETE FROM kits WHERE name = %s", (call.data.split('_')[1], ))
                conn.commit()
                delsetsfortnite(call.message)

        elif call.data == "othergamesegs":
            othergamesegs(call.message)

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

        elif call.data == "deadbydaylight":
            dead_by_daylight(call.message)

        elif call.data == "donatedeadbydaylightnoeditmenu":
            donate_dead_by_daylight_noeditmenu(call.message)

        elif call.data == "donatedeadbydaylightyeseditmenu":
            donate_dead_by_daylight_yeseditmenu(call.message)

        elif call.data == "donatedeadbydaylighthowtofind":
            donate_dead_by_daylight_howtofind(call.message)

        elif call.data == "goldencage":
            golden_cage(call.message)

        elif call.data == "fallguys":
            fall_guys(call.message)

        elif call.data == "donatefallguysnoeditmenu":
            donate_fall_guys_noeditmenu(call.message)

        elif call.data == "donatefallguysyeseditmenu":
            donate_fall_guys_yeseditmenu(call.message)

        elif call.data == "donatefallguyshowtofind":
            donate_fall_guys_howtofind(call.message)

        elif call.data == "shmacks":
            shmacks(call.message)

        elif call.data == "fallguysset":
            fall_guys_set(call.message)

        elif call.data == "fortnite":
            fortnite(call.message)

        elif call.data == "epicgamesaccount":
            epicgamesaccount(call.message)

        elif call.data == "xboxaccout":
            xboxaccout(call.message)

        elif call.data == "epicgamesaccountnoeditmenu":
            epicgamesaccount_noeditmenu(call.message)

        elif call.data == "epicgamesaccountyeseditmenu":
            epicgamesaccount_yeseditmenu(call.message)

        elif call.data == "epicgamesaccounthowtofind":
            epicgamesaccount_howtofind(call.message)

        elif call.data == "epicgamesaccountanother":
            epicgamesaccount_another(call.message)

        elif call.data == "vbucks":
            vbucks(call.message)

        elif call.data == "setsegsxbox":
            sets_egs_xbox(call.message)

        elif call.data == "xboxaccoutyeslinked":
            xboxaccout_yeslinked(call.message)

        elif call.data == "xboxaccouthowlinked":
            xboxaccout_howlinked(call.message)

        elif call.data == "BackToxboxaccout":
            def function1():
                markup = types.InlineKeyboardMarkup(row_width=1)
                btn1 = types.InlineKeyboardButton("Да, привязана", callback_data="xboxaccoutyeslinked")
                btn2 = types.InlineKeyboardButton("Как привязать?", callback_data="xboxaccouthowlinked")
                btn3 = types.InlineKeyboardButton("Назад", callback_data="epicgamesaccount")
                markup.add(btn1, btn2, btn3)
                photo = open(r'src\Donate\fortnite_xbox.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo, caption="У вас привязана учетная запись microsoft xbox к epic games?", reply_markup=markup)
            
            def function2():
                bot.delete_message(call.message.chat.id, call.message.message_id)

            thread1 = threading.Thread(target=function1)
            thread2 = threading.Thread(target=function2)

            thread2.start()
            thread1.start()

            thread1.join()
            thread2.join()
        
        elif call.data == "admfortnite":
            admfortnite(call.message)

        elif call.data == "addsetsfortnite":
            addsetsfortnite(call.message)

        elif call.data == "delsetsfortnite":
            delsetsfortnite(call.message)

        elif call.data == "backtoadmpanel":
            backtoadmpanel(call.message)


if __name__ == "__main__":
    bot.polling(none_stop=True)
