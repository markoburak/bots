import random

import telebot
from telebot import types
from config import TOKEN

# init variables for number and edges
number = 0
margin1 = 0
margin2 = 10
bot = telebot.TeleBot(TOKEN)


# reply for command start
@bot.message_handler(commands=['start'])
def start(message):
    print(message.text)
    print(message.from_user.first_name)
    print()

    # create a keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲Random Number🎲")
    item2 = types.KeyboardButton("🎰Show random")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "hi there", reply_markup=markup)


# reply for any text
@bot.message_handler(content_types=['text'])
def check(message):
    print(message.text)
    print(message.from_user.first_name)
    print()
    global number
    global margin1
    global margin2

    # check for reply from keyboard
    if message.chat.type == 'private':
        if message.text == "🎲Random Number🎲":
            # rand number within edges
            number = random.randint(margin1, margin2)
            bot.send_message(message.chat.id, "Вгадай число від 1 до 10")
        elif message.text.find("Межа1") != -1:
            # set first edge
            text = message.text.split(' ')

            margin1 = int(text[1])
            print(margin1)
        elif message.text.find("Межа2") != -1:
            # set second edge
            text = message.text.split(' ')

            margin2 = int(text[1])
            print(margin2)
        elif message.text == '🎰Show random':
            # just rand number within margin1 and margin2
            bot.send_message(message.chat.id, random.randint(margin1, margin2))
        elif int(message.text) == number:
            # if guess then cool
            bot.send_message(message.chat.id, "Правильно!!!🎉✨")
        elif int(message.text) != number:
            # else not cool)
            bot.send_message(message.chat.id, "Неправильно 😔")
        else:
            # default
            bot.send_message(message.chat.id, "Я не розумію")


bot.polling(none_stop=True)
