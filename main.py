import telebot
import datetime

token = "2012912815:AAHzmucHfxpWJVtDtuCjKFSxbq-InJvYk7Y"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Добрый день. Для уточнения информации /help')

@bot.message_handler(commands=['week'])
def week(message):
    today = datetime.datetime.today().strftime("%W")
    if int(today) % 2 == 0:
        bot.send_message(message.chat.id, 'Сегодня чётная неделя.')
    else:
        bot.send_message(message.chat.id, 'Сегодня нечётная неделя.')

@bot.message_handler(commands=['mtuci'])
def mtuci(message):
    bot.send_message(message.chat.id, 'Официальный сайт МТУСИ: https://mtuci.ru/')

@bot.message_handler(commands=['timetable'])
def timetable(message):
    bot.send_message(message.chat.id, 'https://mtuci.ru/time-table/')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Добрый день. Вот список, что я умею: \n'
                                      '/start - Приветствие \n'
                                      '/week - Четность недели \n'
                                      '/mtuci - Сайт МТУСИ \n'
                                      '/timetable - Расписание\n')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text == "расписание":
        bot.send_message(message.chat.id, 'https://mtuci.ru/time-table/')
    elif message.text == "сайт":
        bot.send_message(message.chat.id, 'https://mtuci.ru/')
    elif message.text == "неделя":
        bot.send_message(message.chat.id, '/week')
    else:
        bot.send_message(message.chat.id, 'Я вас не понял, нажмите /help')

bot.infinity_polling()