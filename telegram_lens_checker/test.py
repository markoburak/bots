import telebot
from telebot import types
import random

from config import TOKEN
from parse_lens import get_rozetka

bot = telebot.TeleBot(TOKEN)


# reply for command start
@bot.message_handler(commands=['start'])
def start(message):
    print(message.text)
    print(message.from_user.first_name)
    print()

    # send sticker
    sticker = open('./static/gordon.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)
    bot.send_message(message.chat.id,
                     "Привіт " + message.chat.first_name + ", мене звати " + bot.get_me().username + "\nЯ допоможу знайти тобі ціни на лінзи")


# reply for command check
@bot.message_handler(commands=['check'])
def checker(message):
    print(message.text)
    print(message.from_user.first_name)
    print()

    # create an inline keyboard
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("rozetka", callback_data="rozetka")
    item2 = types.InlineKeyboardButton("amazon", callback_data='amazon')
    item3 = types.InlineKeyboardButton("best buy", callback_data='best_buy')
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Оберіть магазин лінз: ", reply_markup=markup)


# answers for inline keyboard
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'rozetka':
                bot.send_message(call.message.chat.id, str(get_rozetka()))
            elif call.data == 'amazon':
                bot.send_message(call.message.chat.id, "35")
            elif call.data == 'best_buy':
                bot.send_message(call.message.chat.id, "85")

    except Exception as e:
        print(repr(e))


# answer for a sticker
@bot.message_handler(content_types=['sticker'])
def answer(message):
    print(message.text)
    print(message.from_user.first_name)
    print()
    bot.send_message(message.chat.id, "Ого, маєш класний стікер")


# reply for any other text
@bot.message_handler(content_types=['text'])
def answer(message):
    print(message.text)
    print(message.from_user.first_name)
    print()
    if message.text == 'hi':
        bot.send_message(message.chat.id, "Привіт")
    elif message.text == "marko":
        bot.send_message(message.chat.id, "Крутий")
    elif message.text == "bot givno":
        stickerok = open('./static/AnimatedSticker.tgs', 'rb')
        bot.send_sticker(message.chat.id, stickerok)
    else:
        bot.send_message(message.chat.id, "Я не розумію")


# always polling
bot.polling(none_stop=True)
