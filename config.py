import telebot
import psycopg2
import sqlite3

TOKEN = '6668402751:AAHvjdKsykwnhN_tnMbIwgscZLbW71lCQR4'

bot = telebot.TeleBot(TOKEN)

dbname = 'testDataBase'
user = 'studentsuserdb'
password = 'Gesg6Gesg6564tJOI564tJOI'
host = 'rc1a-8vbl7plj2e5k8djt.mdb.yandexcloud.net'
port = '6432'

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)


admin_list = [217084766,
         ]

feedback_id_group = -1001960643500

dlc = {
    "Forged in Fog": 999,
    "Resident evil: PROJECT W": 999,
    "Roots of Dread": 999,
    "Sadako Rising": 999,
    "Portrait of a murder": 999,
    "Hellraiser": 999,
    "Charity Case": 999,
    "Прервавшийся род": 999,
    "Halloween": 999,
    "Chains of hate": 999,
    "Cursed legacy": 999,
    "Resident evil": 999,
    "Desend Beyond": 999,
    "Nightmare on ELM Street": 999,
    "Silent hill": 999,
    "Ghost Face": 999,
    "Killer Expansion Pack": 999,
    "Survivor Expansion Pack": 999,
    "The 80's Suitcase": 999,
    "Ash vs Evil Dead": 999,
    "Demise of the Faithful": 999,
    "Hour of the Witch": 999,
    "ll-kill": 999,
    "Flesh and Mud": 999,
    "SAW": 999,
    "A Binding of Kin": 999,
    "Head Case": 999,
    "Darkness Among Us": 999,
    "LEATHERFACE": 999,
    "Curatain": 999,
    "Spark of Madness": 999,
    "Bloodstained Sack": 999
    }


game = {
    "MARVEL Человек-Паук: Майлз Моралес": 999,
    "Red Dead Redemption 2": 999,
    "Dying Light 2: Stay Human": 999,
    "Far Cry® 6": 999,
    "It takes two": 999,
    "FIFA 23 «Standard»": 999
    }


golden_cage = {
    "500_goldencage": 999,
    "1100_goldencage": 999,
    "2250_goldencage": 999,
    "4025_goldencage": 999,
    "6000_goldencage": 999,
    "12500_goldencage": 999
    }


shmacks = {
    "1000_shmacks": 999,
    "2800_shmacks": 999,
    "5000_shmacks": 999,
    "13500_shmacks": 999
    }


fallguysset = {
    "Пушистая Радость+": 999,
    "Огненный боксер+": 999,
    "Сезонный набор+": 999,
    "Кратерный Король+": 999,
    "Пингвинья вечеринка": 999,
    "Доктор Рукавицын": 999,
    "Плюшевая лиса": 999,
    "Стартовый набор 2": 999,
    "Ржание+": 999,
    "Ворон": 999
    }


vbucks = {
    "1000_vbucks": 999,
    "2800_vbucks": 999,
    "5000_vbucks": 999,
    "13500_vbucks": 999
    }
