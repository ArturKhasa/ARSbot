import telebot
from telebot import types
import threading

TOKEN = '6668402751:AAHvjdKsykwnhN_tnMbIwgscZLbW71lCQR4'

bot = telebot.TeleBot(TOKEN)


def img_block(src, message, markup, text='ㅤ'):
    with open(src, 'rb') as updated_photo:
        bot.edit_message_media(media=telebot.types.InputMediaPhoto(updated_photo),
                               chat_id=message.chat.id,
                               message_id=message.message_id,
                               reply_markup=markup)
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
        menu(message)
    
    def function2():
        bot.delete_message(message.chat.id, message.message_id)

    thread1 = threading.Thread(target=function1)
    thread2 = threading.Thread(target=function2)

    thread2.start()
    thread1.start()

    thread1.join()
    thread2.join()


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
    bot.send_photo(message.chat.id, photo, caption='ㅤ', reply_markup=markup)


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
    markup = types.InlineKeyboardMarkup(row_width=2)
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
    btn3 = types.InlineKeyboardButton("Назад", callback_data="BackEGSBlockToStore")
    markup.add(btn1, btn2, btn3)
    img_block(r'src\EGS\EpicGames.jpg', message, markup)


def buygamedlc(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Нет, не менял", callback_data="Нет, не менял")
    btn2 = types.InlineKeyboardButton("Да, менял", callback_data="Да, менял")
    btn3 = types.InlineKeyboardButton("Как узнать", callback_data="Как узнать")
    btn4 = types.InlineKeyboardButton("Назад", callback_data="BackBGDToEGSBlock")
    markup.add(btn1, btn2, btn3, btn4)
    img_block(r'src\BuyGameDLC\gamedlc.jpg', message, markup)


def noeditmenu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Игры", callback_data="Игры")
    btn2 = types.InlineKeyboardButton("DLC", callback_data="DLC")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="BackToBGD")
    markup.add(btn1, btn2, btn3)
    img_block(r'src\BuyGameDLC\gamedlc.jpg', message, markup)


def yeseditmenu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Турция", callback_data="Турция")
    btn2 = types.InlineKeyboardButton("Другая", callback_data="Другая")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="BackToBGD")
    markup.add(btn1, btn2, btn3)
    img_block(r'src\BuyGameDLC\gamedlc.jpg', message, markup, text="Какая страна стоит?")


def howtofind(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Назад", callback_data="BackToBGD")
    markup.add(btn1)
    img_block(r'src\BuyGameDLC\gamedlc.jpg', message, markup, text="Инструкция будет*")
  

def othercountry(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Главное меню", callback_data="BackToMenu")
    markup.add(btn1)
    text_block("К сожалению мы не сможем изменить вам регион, так как за последние 6 месяцев он был изменен.", message, markup)


def gameegs(message, text='ㅤ'):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("MARVEL Человек-Паук: Майлз Моралес", callback_data="MARVEL Человек-Паук: Майлз Моралес")
    btn2 = types.InlineKeyboardButton("Red Dead Redemption 2", callback_data="Red Dead Redemption 2")
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton("Dying Light 2 ", callback_data="Dying Light 2 ")
    btn4 = types.InlineKeyboardButton("Stay Human", callback_data="Stay Human")
    markup.row(btn3, btn4)
    btn5 = types.InlineKeyboardButton("Far Cry® 6", callback_data="Far Cry® 6")
    btn6 = types.InlineKeyboardButton("It takes two", callback_data="It takes two")
    markup.row(btn5, btn6)
    btn7 = types.InlineKeyboardButton("FIFA 23 «Standard»", callback_data="FIFA 23 «Standard»")
    markup.row(btn7)
    btn8 = types.InlineKeyboardButton("Назад", callback_data="BackDLCToNEM")
    btn9 = types.InlineKeyboardButton("Другие игры", callback_data="Другие игры")
    markup.row(btn8, btn9)
    img_block(r'src\BuyGameDLC\game.jpg', message, markup, text=text)


def othergamesegs(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Назад", callback_data="BackToGameEGS")
    markup.add(btn1)
    img_block(r'src\BuyGameDLC\game.jpg', 
              message, 
              markup, 
              text='''Зайдите на аккаунт epic games по этим данным:\nЛогин: raroci4898@chotunai.com\nПароль: arsgamestore1\nНайдите игру, которую вы хотите купить и напишите её стоимость, которая вам показана на этом аккаунте, боту в сообщении''')
    bot.register_next_step_handler(message, get_sum)


def get_sum(message):
    suma = message.text
    if suma.isdigit() == True:
        suma = int(suma)
        if suma < 250:
            rublzn = (suma * 4.1) + 150
        elif suma >= 250 and suma < 500:
            rublzn = suma * 4.5
        elif suma >= 500 and suma < 800:
            rublzn = suma * 4.4
        elif suma >= 800:
            rublzn = suma * 4.3
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Продолжить", callback_data="NextPayGame")
        btn2 = types.InlineKeyboardButton("Назад", callback_data="BackToOG")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, 
                     text=f"К оплате {rublzn} руб.".format(message.from_user), 
                     reply_markup=markup)
    else:
        gameegs(message, "Неправильно введено значение, повторите операцию.")


def netxpaygame(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Назад", callback_data="BackToOG")
    markup.add(btn1)
    bot.send_message(message.chat.id, 
                     text="Напишите полное название игры, как написано в Epic Games.".format(message.from_user), 
                     reply_markup=markup)
    bot.register_next_step_handler(message, get_namegame)


def get_namegame(message):
    namegame = message.text
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Назад", callback_data="BackToOG")
    markup.add(btn1)
    bot.send_message(message.chat.id, 
                     text="Напишите вашу почту.".format(message.from_user), 
                     reply_markup=markup)
    bot.register_next_step_handler(message, get_sendemail)


def get_sendemail(message):
    nameemail = message.text
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Назад", callback_data="BackToOG")
    markup.add(btn1)
    bot.send_message(message.chat.id, 
                     text="Напишите ваш логин.".format(message.from_user), 
                     reply_markup=markup)
    bot.register_next_step_handler(message, get_sendlogin)


def get_sendlogin(message):
    namelogin = message.text
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Назад", callback_data="BackToOG")
    markup.add(btn1)
    bot.send_message(message.chat.id, 
                     text="Оплатите...".format(message.from_user), 
                     reply_markup=markup)


def dlcegs(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Dead by daylight", callback_data="Dead by daylight")
    btn2 = types.InlineKeyboardButton("Назад", callback_data="BackDLCToNEM")
    markup.add(btn1, btn2)
    img_block(r'src\BuyGameDLC\game.jpg', message, markup, text='Если вашей игры нет в списке, нажмите "другие игры"')


def deadbydaylight(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Купить", callback_data="BuyOnePage")
    btn2 = types.InlineKeyboardButton("Назад", callback_data="DLC")
    btn3 = types.InlineKeyboardButton("Меню", callback_data="BackToMenu")
    markup.add(btn1, btn2, btn3)
    img_block(r'src\BuyGameDLC\dlc.jpg', message, markup, text="Инструкция будет*")


def dlconepage(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Resident evil: PROJECT W", callback_data="Resident evil: PROJECT W")
    btn2 = types.InlineKeyboardButton("Roots of Dread", callback_data="Roots of Dread")
    markup.row(btn1, btn2) 
    btn3 = types.InlineKeyboardButton("Sadako Rising", callback_data="Sadako Rising")
    btn4 = types.InlineKeyboardButton("Portrait of a murder", callback_data="Portrait of a murder")
    markup.row(btn3, btn4) 
    btn5 = types.InlineKeyboardButton("Hellraiser", callback_data="Hellraiser")
    btn6 = types.InlineKeyboardButton("Charity Case", callback_data="Charity Case")
    markup.row(btn5, btn6) 
    btn7 = types.InlineKeyboardButton("Прервавшийся род", callback_data="Прервавшийся род")
    btn8 = types.InlineKeyboardButton("Halloween", callback_data="Halloween")
    markup.row(btn7, btn8) 
    btn9 = types.InlineKeyboardButton("Chains of hate", callback_data="Chains of hate")
    btn10 = types.InlineKeyboardButton("Cursed legacy", callback_data="Cursed legacy")
    markup.row(btn9, btn10)
    btn11 = types.InlineKeyboardButton("Resident evil", callback_data="Resident evil")
    markup.row(btn11)
    btn12 = types.InlineKeyboardButton("1", callback_data="DlcOnePage")
    btn13 = types.InlineKeyboardButton("2", callback_data="DlcTwoPage")
    btn14 = types.InlineKeyboardButton("3", callback_data="DlcThreePage")
    btn15 = types.InlineKeyboardButton("Назад", callback_data="BackDLCToDLCEGS")
    markup.row(btn12, btn13, btn14, btn15)
    img_block(r'src\BuyGameDLC\dlc1.jpg', message, markup, text="Инструкция будет*")


def dlctwopage(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Desend Beyond", callback_data="Desend Beyond")
    btn2 = types.InlineKeyboardButton("Nightmare on ELM Street", callback_data="Nightmare on ELM Street")
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton("Silent hill", callback_data="Silent hill")
    btn4 = types.InlineKeyboardButton("Ghost Face", callback_data="Ghost Face")
    markup.row(btn3, btn4)
    btn5 = types.InlineKeyboardButton("Killer Expansion Pack", callback_data="Killer Expansion Pack")
    btn6 = types.InlineKeyboardButton("Survivor Expansion Pack", callback_data="Survivor Expansion Pack")
    markup.row(btn5, btn6)
    btn7 = types.InlineKeyboardButton("The 80's Suitcase", callback_data="The 80's Suitcase")
    btn8 = types.InlineKeyboardButton("Ash vs Evil Dead", callback_data="Ash vs Evil Dead")
    markup.row(btn7, btn8)
    btn9 = types.InlineKeyboardButton("Demise of the Faithful", callback_data="Demise of the Faithful")
    btn10 = types.InlineKeyboardButton("Hour of the Witch", callback_data="Hour of the Witch")
    markup.row(btn9, btn10)
    btn11 = types.InlineKeyboardButton("All-kill", callback_data="All-kill")
    btn12 = types.InlineKeyboardButton("Flesh and Mud", callback_data="Flesh and Mud")
    markup.row(btn11, btn12)
    btn13 = types.InlineKeyboardButton("1", callback_data="DlcOnePage")
    btn14 = types.InlineKeyboardButton("2", callback_data="DlcTwoPage")
    btn15 = types.InlineKeyboardButton("3", callback_data="DlcThreePage")
    btn16 = types.InlineKeyboardButton("Назад", callback_data="BackDLCToDLCEGS")
    markup.row(btn13, btn14, btn15, btn16)
    img_block(r'src\BuyGameDLC\dlc2.jpg', message, markup, text="Инструкция будет*")


def dlcthreepage(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("SAW", callback_data="SAW")
    btn2 = types.InlineKeyboardButton("A Binding of Kin", callback_data="A Binding of Kin")
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton("Head Case", callback_data="Head Case")
    btn4 = types.InlineKeyboardButton("Darkness Among Us", callback_data="Darkness Among Us")
    markup.row(btn3, btn4)
    btn5 = types.InlineKeyboardButton("LEATHERFACE", callback_data="LEATHERFACE")
    btn6 = types.InlineKeyboardButton("Curatain", callback_data="Curatain")
    markup.row(btn5, btn6)
    btn7 = types.InlineKeyboardButton("Spark of Madness", callback_data="Spark of Madness")
    btn8 = types.InlineKeyboardButton("Bloodstained Sack", callback_data="Bloodstained Sack")
    markup.row(btn7, btn8)
    btn9 = types.InlineKeyboardButton("1", callback_data="DlcOnePage")
    btn10 = types.InlineKeyboardButton("2", callback_data="DlcTwoPage")
    btn11 = types.InlineKeyboardButton("3", callback_data="DlcThreePage")
    btn12 = types.InlineKeyboardButton("Назад", callback_data="BackDLCToDLCEGS")
    markup.row(btn9, btn10, btn11, btn12)
    img_block(r'src\BuyGameDLC\dlc3.jpg', message, markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.message:
        if call.data == 'Магазин 🛒' or call.data == "BackEGSBlockToStore":
            store(call.message)

        elif call.data == 'Кабинет 👤':
            office(call.message)

        elif call.data == 'Отзывы 📕':
            reviews(call.message)

        elif call.data == 'F.A.Q 📌':
            guide(call.message)

        elif call.data == 'Epic Games' or call.data == "BackBGDToEGSBlock":
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

        elif call.data == "Покупка игр и DLC" or call.data == "BackToBGD":
            buygamedlc(call.message)

        elif call.data == "Нет, не менял" or call.data == "Турция" or call.data == "BackDLCToNEM":
            noeditmenu(call.message)

        elif call.data == "Да, менял":
            yeseditmenu(call.message)

        elif call.data == "Как узнать":
            howtofind((call.message))

        elif call.data == "Игры" or call.data == "BackToGameEGS":
            gameegs(call.message)

        elif call.data == "DLC":
            dlcegs(call.message)

        elif call.data == "Другая":
            othercountry(call.message)

        elif call.data == "Dead by daylight" or call.data == "BackDLCToDLCEGS":
            deadbydaylight(call.message)

        elif call.data == "BuyOnePage":
            dlconepage(call.message)

        elif call.data == "DlcTwoPage":
            dlctwopage(call.message)

        elif call.data == "DlcThreePage":
            dlcthreepage(call.message)

        elif call.data == "Resident evil: PROJECT W":
            pass

        elif call.data == "Roots of Dread":
            pass

        elif call.data == "Sadako Rising":
            pass

        elif call.data == "Portrait of a murder":
            pass

        elif call.data == "Hellraiser":
            pass

        elif call.data == "Charity Case":
            pass

        elif call.data == "Прервавшийся род":
            pass

        elif call.data == "Halloween":
            pass

        elif call.data == "Chains of hate":
            pass

        elif call.data == "Cursed legacy":
            pass

        elif call.data == "Resident evil":
            pass

        elif call.data == "Desend Beyond":
            pass

        elif call.data == "Nightmare on ELM Street":
            pass

        elif call.data == "Silent hill":
            pass

        elif call.data == "Ghost Face":
            pass

        elif call.data == "Killer Expansion Pack":
            pass

        elif call.data == "Survivor Expansion Pack":
            pass

        elif call.data == "The 80's Suitcase":
            pass

        elif call.data == "Ash vs Evil Dead":
            pass

        elif call.data == "Demise of the Faithful":
            pass

        elif call.data == "Hour of the Witch":
            pass

        elif call.data == "All-kill":
            pass

        elif call.data == "Flesh and Mud":
            pass

        elif call.data == "SAW":
            pass

        elif call.data == "A Binding of Kin":
            pass

        elif call.data == "Head Case":
            pass

        elif call.data == "Darkness Among Us":
            pass

        elif call.data == "LEATHERFACE":
            pass

        elif call.data == "Curatain":
            pass

        elif call.data == "Spark of Madness":
            pass

        elif call.data == "Bloodstained Sack":
            pass

        elif call.data == "Red Dead Redemption 2":
            pass

        elif call.data == "MARVEL Человек-Паук: Майлз Моралес":
            pass

        elif call.data == "Dying Light 2":
            pass

        elif call.data == "Stay Human":
            pass

        elif call.data == "Far Cry® 6":
            pass

        elif call.data == "It takes two":
            pass

        elif call.data == "FIFA 23 «Standard»":
            pass

        elif call.data == "Другие игры":
            othergamesegs(call.message)

        elif call.data == "BackToOG":
            def function1():
                markup = types.InlineKeyboardMarkup()
                btn1 = types.InlineKeyboardButton("Назад", callback_data="BackToGameEGS")
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

        


bot.polling(none_stop=True)
