import telebot
from telebot import types
import multiprocessing

TOKEN = '6668402751:AAHvjdKsykwnhN_tnMbIwgscZLbW71lCQR4'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def menu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Магазин 🛒", callback_data="Магазин 🛒")
    btn2 = types.InlineKeyboardButton("Кабинет 👤", callback_data="Кабинет 👤")
    btn3 = types.InlineKeyboardButton("Отзывы 📕", callback_data="Отзывы 📕")
    btn4 = types.InlineKeyboardButton("F.A.Q 📌", callback_data="F.A.Q 📌")
    btn5 = types.InlineKeyboardButton("Поддержка 👨‍💻", callback_data="Поддержка 👨‍💻")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    photo = open(r'src\Menu\menu.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, caption='ㅤ', reply_markup=markup)


def store(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Epic Games", callback_data="Epic Games")
    btn2 = types.InlineKeyboardButton("Steam", callback_data="Steam")
    btn3 = types.InlineKeyboardButton("Origin", callback_data="Origin")
    btn4 = types.InlineKeyboardButton("Ubisoft", callback_data="Ubisoft")
    btn5 = types.InlineKeyboardButton("Blizzard", callback_data="Blizzard")
    btn5 = types.InlineKeyboardButton("Battle.Net", callback_data="Battle.Net")
    btn6 = types.InlineKeyboardButton("Назад", callback_data="BackStoreToMenu")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    with open(r'src\Store\store.jpg', 'rb') as updated_photo:
        bot.edit_message_media(media=telebot.types.InputMediaPhoto(updated_photo),
                               chat_id=message.chat.id,
                               message_id=message.message_id,
                               reply_markup=markup)


def office(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Реферальная ссылка", callback_data="Реферальная ссылка")
    btn2 = types.InlineKeyboardButton("Пополнить баланс", callback_data="Пополнить баланс")
    btn3 = types.InlineKeyboardButton("История заказов", callback_data="История заказов")
    btn4 = types.InlineKeyboardButton("Назад", callback_data="BackOfficeToMenu")
    markup.add(btn1, btn2, btn3, btn4)
    with open(r'src\Office\office.jpg', 'rb') as updated_photo:
        bot.edit_message_media(media=telebot.types.InputMediaPhoto(updated_photo),
                               chat_id=message.chat.id,
                               message_id=message.message_id,
                               reply_markup=markup)


def reviews(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Перейти", callback_data="TransitionReviews")
    btn2 = types.InlineKeyboardButton("Назад", callback_data="BackToMenu")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 
                     text="Здесь мы собираем отзывы наших клиентов. Вы можете задать любой вопрос участникам, кто ранее у нас делал заказы и убедиться, что всё прозрачно и честно.".format(message.from_user), 
                     reply_markup=markup)
    bot.delete_message(message.chat.id, 
                       message.message_id)


def guide(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Перейти", callback_data="TransitionGuide")
    btn2 = types.InlineKeyboardButton("Назад", callback_data="BackToMenu")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 
                     text="Здесь мы собрали наиболее актуальные вопросы наших клиентов.\nЕсли не найдёте ответ на свой вопрос, то напишите нам в службу поддержки.".format(message.from_user), 
                     reply_markup=markup)
    bot.delete_message(message.chat.id, 
                       message.message_id)
    
  
def support(message):
    pass


def egsblock(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Донат", callback_data="Донат")
    btn2 = types.InlineKeyboardButton("Покупка игр и DLC", callback_data="Покупка игр и DLC")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="BackEGSBlockToStore")
    markup.add(btn1, btn2, btn3)
    with open(r'src\EGS\EpicGames.jpg', 'rb') as updated_photo:
        bot.edit_message_media(media=telebot.types.InputMediaPhoto(updated_photo),
                               chat_id=message.chat.id,
                               message_id=message.message_id,
                               reply_markup=markup)


def buygamedlc(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Нет, не менял", callback_data="Нет, не менял")
    btn2 = types.InlineKeyboardButton("Да, менял", callback_data="Да, менял")
    btn3 = types.InlineKeyboardButton("Как узнать", callback_data="Как узнать")
    btn4 = types.InlineKeyboardButton("Назад", callback_data="BackBGDToEGSBlock")
    markup.add(btn1, btn2, btn3, btn4)
    with open(r'src\BuyGameDLC\gamedlc.jpg', 'rb') as updated_photo:
        bot.edit_message_media(media=telebot.types.InputMediaPhoto(updated_photo),
                               chat_id=message.chat.id,
                               message_id=message.message_id,
                               reply_markup=markup)


def noeditmenu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Игры", callback_data="Игры")
    btn2 = types.InlineKeyboardButton("DLC", callback_data="DLC")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="BackNEMToBGD")
    markup.add(btn1, btn2, btn3)
    with open(r'src\BuyGameDLC\gamedlc.jpg', 'rb') as updated_photo:
        bot.edit_message_media(media=telebot.types.InputMediaPhoto(updated_photo),
                               chat_id=message.chat.id,
                               message_id=message.message_id,
                               reply_markup=markup)


# @bot.message_handler(commands=['yeseditmenu'])
def yeseditmenu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Турция", callback_data="Турция")
    btn2 = types.InlineKeyboardButton("Другая", callback_data="Другая")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="BackYEMToBGD")
    markup.add(btn1, btn2, btn3)
    with open(r'src\BuyGameDLC\gamedlc.jpg', 'rb') as updated_photo:
        bot.edit_message_media(media=telebot.types.InputMediaPhoto(updated_photo),
                               chat_id=message.chat.id,
                               message_id=message.message_id,
                               reply_markup=markup)


# @bot.message_handler(commands=['howtofind'])
def howtofind(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Назад", callback_data="BackHTFToBGD")
    markup.add(btn1)
    bot.edit_message_caption(caption="Инструкция будет*".format(message.from_user),
                             chat_id=message.chat.id,
                             message_id=message.message_id,
                             reply_markup=markup)
  

# @bot.message_handler(commands=['othercountry'])
def othercountry(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Главное меню", callback_data="BackMain")
    markup.add(btn1)
    bot.send_message(message.chat.id, 
                     text="К сожалению мы не сможем изменить вам регион, так как за последние 6 месяцев он был изменен.".format(message.from_user), 
                     reply_markup=markup)
    bot.delete_message(message.chat.id, message.message_id)


# @bot.message_handler(commands=['gameegs'])
def gameegs(message):
    pass


# @bot.message_handler(commands=['dlcegs'])
def dlcegs(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Dead by daylight", callback_data="Dead by daylight")
    btn2 = types.InlineKeyboardButton("Назад", callback_data="BackDLCToNEM")
    markup.add(btn1, btn2)
    photo = open(r'src\BuyGameDLC\dlc.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, reply_markup=markup)


# @bot.message_handler(commands=['dlconepage'])
def dlconepage(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Resident evil: PROJECT W", callback_data="Resident evil: PROJECT W")
    btn2 = types.InlineKeyboardButton("Roots of Dread", callback_data="Roots of Dread")
    btn3 = types.InlineKeyboardButton("Sadako Rising", callback_data="Sadako Rising")
    btn4 = types.InlineKeyboardButton("Portrait of a murder", callback_data="Portrait of a murder")
    btn5 = types.InlineKeyboardButton("Hellraiser", callback_data="Hellraiser")
    btn6 = types.InlineKeyboardButton("Charity Case", callback_data="Charity Case")
    btn7 = types.InlineKeyboardButton("Прервавшийся род", callback_data="Прервавшийся род")
    btn8 = types.InlineKeyboardButton("Halloween", callback_data="Halloween")
    btn9 = types.InlineKeyboardButton("Chains of hate", callback_data="Chains of hate")
    btn10 = types.InlineKeyboardButton("Cursed legacy", callback_data="Cursed legacy")
    btn11 = types.InlineKeyboardButton("Resident evil", callback_data="Resident evil")
    btn12 = types.InlineKeyboardButton("Назад", callback_data="BackDLCToDLCEGS")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)
    photo = open(r'src\BuyGameDLC\dlc1.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, reply_markup=markup)


# @bot.message_handler(commands=['dlctwopage'])
def dlctwopage(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Desend Beyond", callback_data="Desend Beyond")
    btn2 = types.InlineKeyboardButton("Nightmare on ELM Street", callback_data="Nightmare on ELM Street")
    btn3 = types.InlineKeyboardButton("Silent hill", callback_data="Silent hill")
    btn4 = types.InlineKeyboardButton("Ghost Face", callback_data="Ghost Face")
    btn5 = types.InlineKeyboardButton("Killer Expansion Pack", callback_data="Killer Expansion Pack")
    btn6 = types.InlineKeyboardButton("Survivor Expansion Pack", callback_data="Survivor Expansion Pack")
    btn7 = types.InlineKeyboardButton("The 80's Suitcase", callback_data="The 80's Suitcase")
    btn8 = types.InlineKeyboardButton("Ash vs Evil Dead", callback_data="Ash vs Evil Dead")
    btn9 = types.InlineKeyboardButton("Demise of the Faithful", callback_data="Demise of the Faithful")
    btn10 = types.InlineKeyboardButton("Hour of the Witch", callback_data="Hour of the Witch")
    btn11 = types.InlineKeyboardButton("All-kill", callback_data="All-kill")
    btn12 = types.InlineKeyboardButton("Flesh and Mud", callback_data="Flesh and Mud")
    btn13 = types.InlineKeyboardButton("Назад", callback_data="BackDLCToDLCEGS")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)
    photo = open(r'src\BuyGameDLC\dlc2.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, reply_markup=markup)


# @bot.message_handler(commands=['dlcthreepage'])
def dlcthreepage(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("SAW", callback_data="SAW")
    btn2 = types.InlineKeyboardButton("A Binding of Kin", callback_data="A Binding of Kin")
    btn3 = types.InlineKeyboardButton("Head Case", callback_data="Head Case")
    btn4 = types.InlineKeyboardButton("Darkness Among Us", callback_data="Darkness Among Us")
    btn5 = types.InlineKeyboardButton("LEATHERFACE", callback_data="LEATHERFACE")
    btn6 = types.InlineKeyboardButton("Curatain", callback_data="Curatain")
    btn7 = types.InlineKeyboardButton("Spark of Madness", callback_data="Spark of Madness")
    btn8 = types.InlineKeyboardButton("Bloodstained Sack", callback_data="Bloodstained Sack")
    btn9 = types.InlineKeyboardButton("Назад", callback_data="BackDLCToDLCEGS")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
    photo = open(r'src\BuyGameDLC\dlc3.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, reply_markup=markup)


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

        elif call.data == 'Поддержка 👨‍💻':
            support(call.message)

        elif call.data == 'Epic Games':
            egsblock(call.message)

        elif call.data == 'BackStoreToMenu':
            menu(call.message)

        elif call.data == 'Реферальная ссылка':
            pass

        elif call.data == 'Пополнить баланс':
            pass

        elif call.data == 'История заказов':
            pass

        elif call.data == 'BackOfficeToMenu':
            menu(call.message)

        elif call.data == 'TransitionReviews':
            pass

        elif call.data == 'BackToMenu':
            menu(call.message)
            bot.delete_message(call.message.chat.id, call.message.message_id)

        elif call.data == 'TransitionGuide':
            pass


bot.polling(none_stop=True)
