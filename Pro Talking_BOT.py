import random
import telebot
import apiai
import json

from telebot import types

bot = telebot.TeleBot("1100038091:AAESXzUtbx39eGW1Vfm25UvQZa9rOmLnO-U")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item2 = types.KeyboardButton("/start")
    item4 = types.KeyboardButton("/help")
    item1 = types.KeyboardButton("/OaR")
    item3 = types.KeyboardButton("/OaR10")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Привет! Давай общаться.'
                     ' Для большей информации нажми на /help',
                     reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Привет данный '
                     'бот разработан для скрашивания время '
                     'препровождения во время карантина.')
    bot.send_message(message.chat.id, 'Что-бы начать '
                     'пользоваться ботом просто напишите ему. '
                     'Так-же есть функция орла и решки(/OaR) '
                     'для решения споров с друзьями)))'
                     '(/OaR10 кинет монету 10 раз)')
    bot.send_message(message.chat.id, 'Создан Фомченковым '
                     'Семёном как проекта Яндекс лицея.')


@bot.message_handler(commands=['OaR'])
def randomf(message):
    if random.randint(0, 1) == 0:
        bot.send_message(message.chat.id, 'Орёл')
    else:
        bot.send_message(message.chat.id, 'Решка')


@bot.message_handler(commands=['OaR10'])
def random10(message):
    for i in range(10):
        if random.randint(0, 1) == 0:
            bot.send_message(message.chat.id, 'Орёл')
        else:
            bot.send_message(message.chat.id, 'Решка')


@bot.message_handler(content_types=['text'])
def textMessage(message):
    request = apiai.ApiAI('c9a720bc0bb041e1bb9273d057eccfde').text_request()
    request.lang = 'ru'
    request.session_id = 'BOTOBHALKIN'
    request.query = message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, 'Я не очень понял тебя.')

bot.polling(none_stop=True)
