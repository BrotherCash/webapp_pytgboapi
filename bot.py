import os
import telebot
# from telebot import types

from dotenv import load_dotenv
import keyboards

load_dotenv()

BOT_TOKEN=os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN, parse_mode='html')


@bot.message_handler(commands=['start']) #обрабатываем команду старт
def start_handler(message):
    # отправляем сообщение с нужной клавиатурой
    bot.send_message( message.chat.id, ' 👋 Привет, добро пожаловать в наш магазин!)\nВоспользуйтесь кнопками для выбора 👇.', reply_markup=keyboards.web_app_keyboard())


@bot.message_handler(commands=['help']) #обрабатываем команду старт
def help_handler(message):
    bot.send_message( message.chat.id,'Раздел помощи находится в разработке')


@bot.message_handler(content_types="text")
def any_message_handler(message):
    start_handler(message)


@bot.message_handler(content_types="web_app_data") #получаем отправленные данные 
def answer(webAppMes):
    print(webAppMes) #вся информация о сообщении
    print(webAppMes.web_app_data.data) #конкретно то что мы передали в бота
    bot.send_message(webAppMes.chat.id, f"получили инофрмацию из веб-приложения: {webAppMes.web_app_data.data}")
    #отправляем сообщение в ответ на отправку данных из веб-приложения

if __name__ == '__main__':
    bot.infinity_polling()