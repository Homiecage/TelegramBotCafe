
import telebot

bot = telebot.TeleBot("592432380:AAEfyxiX1sRE0yPiX3gFBLjwnhrgQgnjHkM")

print(bot.get_me())

def log(message,answer):
    print("/n ------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print(answer)


@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('Выбрать кофе', 'Помощь')
    bot.send_message(message.from_user.id, 'Добро пожаловать', reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Выбрать кофе":
        user_markup = telebot.types.ReplyKeyboardMarkup()
        user_markup.row('Латте', 'Капучино', 'Американо')
        bot.send_message(message.from_user.id, 'Выберите кофе', reply_markup=user_markup)
    elif message.text == "Латте" or message.text == "Капучино" or message.text == "Американо":
        user_markup = telebot.types.ReplyKeyboardMarkup()
        user_markup.row('0,2', '0,3', '0,5')
        bot.send_message(message.from_user.id, 'Выберите объем', reply_markup=user_markup)
    elif message.text == "0,2" or message.text == "0,3" or message.text == "0,5":
        user_markup = telebot.types.ReplyKeyboardMarkup()
        user_markup.row('Да, оплатить заказ', 'Нет, хочу поменять заказ')
        bot.send_message(message.from_user.id, 'Все правильно?', reply_markup=user_markup)
    elif message.text == "Да, оплатить заказ":
        user_markup = telebot.types.ReplyKeyboardMarkup()
        user_markup.row('Оплата')
        bot.send_message(message.from_user.id, 'Okey', reply_markup=user_markup)
    elif message.text == "Нет, хочу поменять заказ":
        user_markup = telebot.types.ReplyKeyboardMarkup()
        user_markup.row('Выбрать кофе')
        bot.send_message(message.from_user.id, 'Выберите объем', reply_markup=user_markup)
    else:
        print("Ваш запрос не распознан")


bot.polling(none_stop=True, interval=0)
