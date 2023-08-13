from telebot import types
from adaptive_help_func_telebot import *
from config import dlc
from math import ceil

### Блок Игры и DLC
def buygamedlc(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Нет, не менял", callback_data="Нет, не менял")
    btn2 = types.InlineKeyboardButton("Да, менял", callback_data="Да, менял")
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton("Как узнать", callback_data="Как узнать")
    markup.row(btn3)
    btn4 = types.InlineKeyboardButton("Назад", callback_data="Epic Games")
    markup.row(btn4)
    img_block(r'src\BuyGameDLC\gamedlc.jpg', message, markup, text="Вы меняли регион за последние 6 месяцев?")


def noeditmenu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Игры", callback_data="Игры")
    btn2 = types.InlineKeyboardButton("DLC", callback_data="DLC")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="Покупка игр и DLC")
    markup.add(btn1, btn2, btn3)
    img_block(r'src\BuyGameDLC\gamedlc.jpg', message, markup)


def yeseditmenu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Турция", callback_data="Нет, не менял")
    btn2 = types.InlineKeyboardButton("Другая", callback_data="Другая")
    btn3 = types.InlineKeyboardButton("Назад", callback_data="Покупка игр и DLC")
    markup.add(btn1, btn2, btn3)
    img_block(r'src\BuyGameDLC\gamedlc.jpg', message, markup, text="Какая страна стоит?")


def howtofind(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Назад", callback_data="Покупка игр и DLC")
    markup.add(btn1)
    img_block(r'src\BuyGameDLC\gamedlc.jpg', message, markup, text="Инструкция будет*")
  

def othercountry(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Главное меню", callback_data="BackToMenu")
    markup.add(btn1)
    text_block("К сожалению мы не сможем изменить вам регион, так как за последние 6 месяцев он был изменен.", message, markup)


def gameegs(message, text=''):
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
    btn8 = types.InlineKeyboardButton("Назад", callback_data="Нет, не менял")
    btn9 = types.InlineKeyboardButton("Другие игры", callback_data="Другие игры")
    markup.row(btn8, btn9)
    img_block(r'src\BuyGameDLC\game.jpg', message, markup, text=text)


def othergamesegs(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Назад", callback_data="Игры")
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
    btn2 = types.InlineKeyboardButton("Назад", callback_data="Нет, не менял")
    markup.add(btn1, btn2)
    img_block(r'src\BuyGameDLC\dlc.jpg', message, markup, text='')


def deadbydaylight(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Купить", callback_data="1_pagedlcbuy")
    btn2 = types.InlineKeyboardButton("Назад", callback_data="DLC")
    btn3 = types.InlineKeyboardButton("Меню", callback_data="BackToMenu")
    markup.add(btn1, btn2, btn3)
    img_block(r'src\BuyGameDLC\dlc.jpg', message, markup, text="")


def dlcNpage(message, number_page):
    count_el_page = 12
    markup = types.InlineKeyboardMarkup()
    name_dlc = [i for i in dlc.keys()]
    cout_page = ceil(len(name_dlc) / count_el_page)
    if len(name_dlc[(int(number_page) - 1) * count_el_page:int(number_page) * count_el_page]) == count_el_page:
        for i in range((int(number_page) - 1) * count_el_page, int(number_page) * count_el_page, 2):
            markup.row(types.InlineKeyboardButton(name_dlc[i], callback_data=name_dlc[i]), 
                       types.InlineKeyboardButton(name_dlc[i + 1], callback_data=name_dlc[i + 1]))
    else:
        if len(name_dlc) % 2 == 0:
            for i in range((int(number_page) - 1) * count_el_page, len(name_dlc), 2):
                markup.row(types.InlineKeyboardButton(name_dlc[i], callback_data=name_dlc[i]),
                           types.InlineKeyboardButton(name_dlc[i + 1], callback_data=name_dlc[i + 1]))
        else:
            for i in range((int(number_page) - 1) * count_el_page, len(name_dlc), 2):
                try:
                    markup.row(types.InlineKeyboardButton(name_dlc[i], callback_data=name_dlc[i]),
                               types.InlineKeyboardButton(name_dlc[i + 1], callback_data=name_dlc[i + 1]))
                except:
                    markup.row(types.InlineKeyboardButton(name_dlc[i], callback_data=name_dlc[i]))
    markup.row(*[types.InlineKeyboardButton(str(i), callback_data=f"{i}_pagedlcbuy") for i in range(1, cout_page + 1)])
    markup.row(types.InlineKeyboardButton('Назад', callback_data='BackDLCToDLCEGS'))
    img_block(f'src\\BuyGameDLC\\dlc{number_page}.jpg', message, markup, text="Инструкция будет*")


# def dlconepage(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton("Forged in Fog", callback_data="Forged in Fog")
#     markup.row(btn1)
#     btn1 = types.InlineKeyboardButton("Resident evil: PROJECT W", callback_data="Resident evil: PROJECT W")
#     markup.row(btn1) 
#     btn2 = types.InlineKeyboardButton("Roots of Dread", callback_data="Roots of Dread")
#     btn3 = types.InlineKeyboardButton("Sadako Rising", callback_data="Sadako Rising")
#     markup.row(btn2, btn3) 
#     btn4 = types.InlineKeyboardButton("Portrait of a murder", callback_data="Portrait of a murder")
#     markup.row(btn4) 
#     btn5 = types.InlineKeyboardButton("Hellraiser", callback_data="Hellraiser")
#     btn6 = types.InlineKeyboardButton("Charity Case", callback_data="Charity Case")
#     markup.row(btn5, btn6) 
#     btn7 = types.InlineKeyboardButton("Прервавшийся род", callback_data="Прервавшийся род")
#     btn8 = types.InlineKeyboardButton("Halloween", callback_data="Halloween")
#     markup.row(btn7, btn8) 
#     btn9 = types.InlineKeyboardButton("Chains of hate", callback_data="Chains of hate")
#     btn10 = types.InlineKeyboardButton("Cursed legacy", callback_data="Cursed legacy")
#     markup.row(btn9, btn10)
#     btn11 = types.InlineKeyboardButton("Resident evil", callback_data="Resident evil")
#     markup.row(btn11)
#     btn12 = types.InlineKeyboardButton("1", callback_data="DlcOnePage")
#     btn13 = types.InlineKeyboardButton("2", callback_data="DlcTwoPage")
#     btn14 = types.InlineKeyboardButton("3", callback_data="DlcThreePage")
#     btn15 = types.InlineKeyboardButton("Назад", callback_data="BackDLCToDLCEGS")
#     markup.row(btn12, btn13, btn14, btn15)
#     img_block(r'src\BuyGameDLC\dlc1.jpg', message, markup, text="Инструкция будет*")


# def dlctwopage(message):
#     markup = types.InlineKeyboardMarkup(row_width=2)
#     btn1 = types.InlineKeyboardButton("Desend Beyond", callback_data="Desend Beyond")
#     btn2 = types.InlineKeyboardButton("Nightmare on ELM Street", callback_data="Nightmare on ELM Street")
#     markup.row(btn1, btn2)
#     btn3 = types.InlineKeyboardButton("Silent hill", callback_data="Silent hill")
#     btn4 = types.InlineKeyboardButton("Ghost Face", callback_data="Ghost Face")
#     markup.row(btn3, btn4)
#     btn5 = types.InlineKeyboardButton("Killer Expansion Pack", callback_data="Killer Expansion Pack")
#     btn6 = types.InlineKeyboardButton("Survivor Expansion Pack", callback_data="Survivor Expansion Pack")
#     markup.row(btn5, btn6)
#     btn7 = types.InlineKeyboardButton("The 80's Suitcase", callback_data="The 80's Suitcase")
#     btn8 = types.InlineKeyboardButton("Ash vs Evil Dead", callback_data="Ash vs Evil Dead")
#     markup.row(btn7, btn8)
#     btn9 = types.InlineKeyboardButton("Demise of the Faithful", callback_data="Demise of the Faithful")
#     btn10 = types.InlineKeyboardButton("Hour of the Witch", callback_data="Hour of the Witch")
#     markup.row(btn9, btn10)
#     btn11 = types.InlineKeyboardButton("All-kill", callback_data="All-kill")
#     btn12 = types.InlineKeyboardButton("Flesh and Mud", callback_data="Flesh and Mud")
#     markup.row(btn11, btn12)
#     btn13 = types.InlineKeyboardButton("1", callback_data="DlcOnePage")
#     btn14 = types.InlineKeyboardButton("2", callback_data="DlcTwoPage")
#     btn15 = types.InlineKeyboardButton("3", callback_data="DlcThreePage")
#     btn16 = types.InlineKeyboardButton("Назад", callback_data="BackDLCToDLCEGS")
#     markup.row(btn13, btn14, btn15, btn16)
#     img_block(r'src\BuyGameDLC\dlc2.jpg', message, markup, text="Инструкция будет*")


# def dlcthreepage(message):
#     markup = types.InlineKeyboardMarkup(row_width=2)
#     btn1 = types.InlineKeyboardButton("SAW", callback_data="SAW")
#     btn2 = types.InlineKeyboardButton("A Binding of Kin", callback_data="A Binding of Kin")
#     markup.row(btn1, btn2)
#     btn3 = types.InlineKeyboardButton("Head Case", callback_data="Head Case")
#     btn4 = types.InlineKeyboardButton("Darkness Among Us", callback_data="Darkness Among Us")
#     markup.row(btn3, btn4)
#     btn5 = types.InlineKeyboardButton("LEATHERFACE", callback_data="LEATHERFACE")
#     btn6 = types.InlineKeyboardButton("Curatain", callback_data="Curatain")
#     markup.row(btn5, btn6)
#     btn7 = types.InlineKeyboardButton("Spark of Madness", callback_data="Spark of Madness")
#     btn8 = types.InlineKeyboardButton("Bloodstained Sack", callback_data="Bloodstained Sack")
#     markup.row(btn7, btn8)
#     btn9 = types.InlineKeyboardButton("1", callback_data="DlcOnePage")
#     btn10 = types.InlineKeyboardButton("2", callback_data="DlcTwoPage")
#     btn11 = types.InlineKeyboardButton("3", callback_data="DlcThreePage")
#     btn12 = types.InlineKeyboardButton("Назад", callback_data="BackDLCToDLCEGS")
#     markup.row(btn9, btn10, btn11, btn12)
#     img_block(r'src\BuyGameDLC\dlc3.jpg', message, markup)