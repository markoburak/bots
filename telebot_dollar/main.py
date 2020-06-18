import telebot
from telebot import types

from config import TOKEN
from selenium import webdriver

dollar_buy = 'None'
dollar_black = 'None'
euro_buy = 'None'
euro_black = 'None'


def get_currency():
    global dollar_buy
    global dollar_black
    global euro_buy
    global euro_black
    url = 'https://minfin.com.ua/ua/currency/'
    chrome_path = r'./web_driver/83/chromedriver.exe'

    driver = webdriver.Chrome(chrome_path)

    driver.get(url)
    # dollar
    dollar_buy = driver.find_element_by_xpath(
        '/html/body/main/div/div/div[1]/div/section[2]/div/table[1]/tbody/tr[1]/td[3]/span').text
    dollar_black = driver.find_element_by_xpath(
        '/html/body/main/div[2]/div/div[1]/div/section[2]/div/table[1]/tbody/tr[1]/td[4]').text.replace('\n', ' ')

    # euro
    euro_buy = driver.find_element_by_xpath(
        '/html/body/main/div[2]/div/div[1]/div/section[2]/div/table[1]/tbody/tr[2]/td[3]/span').text
    euro_black = driver.find_element_by_xpath(
        '/html/body/main/div[2]/div/div[1]/div/section[2]/div/table[1]/tbody/tr[2]/td[4]').text.replace('\n', ' ')

    driver.quit()


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['check'])
def check(message):
    global markup
    print(message.text)
    print(message.from_user.first_name)
    print()
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("dollar", callback_data='dollar')
    item2 = types.InlineKeyboardButton("euro", callback_data='euro')
    # item3 = types.InlineKeyboardButton("pound", callback_data='pound')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Оберіть валюту:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global dollar_buy
    global euro_buy

    markup_up = markup
    local_euro_buy = euro_buy
    loc_dollar_buy = dollar_buy
    try:
        if call.message:
            if call.data == 'dollar':
                if loc_dollar_buy == "None":
                    get_currency()
                    bot.send_message(call.message.chat.id, "Долар\nНБУ :\n" + dollar_buy[0:5] + "₴")
                    bot.send_message(call.message.chat.id, "Чорний ринок\nКупівля / Продаж : \n" + dollar_black)
                    bot.send_message(call.message.chat.id, "Оберіть валюту:", reply_markup=markup_up)

                    dollar_buy = "None"

                    print('done')
                else:
                    bot.send_message(call.message.chat.id, "Долар\nНБУ :\n" + dollar_buy[0:5] + "₴")
                    bot.send_message(call.message.chat.id, "Чорний ринок\nКупівля / Продаж : \n" + dollar_black)
                    bot.send_message(call.message.chat.id, "Оберіть валюту:", reply_markup=markup_up)
                    dollar_buy = "None"

            elif call.data == 'euro':
                if local_euro_buy == "None":
                    get_currency()
                    bot.send_message(call.message.chat.id, "Євро\nНБУ :\n" + euro_buy[0:5] + "₴")
                    bot.send_message(call.message.chat.id, "Чорний ринок\nКупівля / Продаж : \n" + euro_black)
                    bot.send_message(call.message.chat.id, "Оберіть валюту:", reply_markup=markup_up)
                    euro_buy = "None"

                    print('done')
                else:
                    bot.send_message(call.message.chat.id, "Євро\nНБУ :\n" + euro_buy[0:5] + "₴")
                    bot.send_message(call.message.chat.id, "Чорний ринок\nКупівля / Продаж : \n" + euro_black)
                    bot.send_message(call.message.chat.id, "Оберіть валюту:", reply_markup=markup_up)
                    euro_buy = "None"

    except Exception as e:
        print(repr(e))


@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.chat.id, "Я не розумію")


bot.polling(none_stop=True)
