import telebot
import sqlite3

connection = sqlite3.connect('e_shop.db')

sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS '
            'users (tg_id INTEGER, name TEXT, phone_number INTEGER, address TEXT, reg_date DATETIME);')
bot = telebot.TeleBot("5919860427:AAFhfzXkv1hJH0a1e0LgcbFAi_0C9A0qLN0")
