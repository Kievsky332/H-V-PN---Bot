import telebot
import secret
import random
import hashlib
import os
from openai import OpenAI
bot = telebot.TeleBot(secret.bot)


print("Бот запущен")
#Рандомный код 
@bot.message_handler(commands=["code"] )
@bot.message_handler(regexp="Получить код" )
def repeat_all_messages(message): 
    b = str(random.randint(100,100000))
    ba = secret.a+b+secret.b
    c = hashlib.md5(ba.encode()).hexdigest()
    bot.send_message(message.chat.id, c)


#Убийство бота
@bot.message_handler(commands=[secret.kill] )
def kill(message):
    bot.send_message(message.chat.id, "ИЗвини но иди подальнше ,ладно иду спать!")
    bot.stop_polling()
    os.system("clear||cls")
    print("Бот убит через комманду")

#Поддержка
@bot.message_handler(commands=["help"])
@bot.message_handler(regexp="Связь с поддержкой" )
def hiAi(message): 
    bot.send_message(message.chat.id, "@hvpn_help_bot. - Бот поддержки нашего впн сервиса")

#Донат
@bot.message_handler(regexp="Донат" )
def hiAi(message): 
    bot.send_message(message.chat.id, "Донат")

#Отзывы
@bot.message_handler(regexp="Отзывы" )
def hiAi(message): 
    bot.send_message(message.chat.id, "Отзывы")

#Оставить отзыв
@bot.message_handler(regexp="Оставить отзыв" )
def hiAi(message): 
    bot.send_message(message.chat.id, "отставьте отзыв")


#Кнопки
@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=2)
    kod = telebot.types.KeyboardButton(text="Получить код" )
    help = telebot.types.KeyboardButton(text="Связь с поддержкой" )

    sendotz = telebot.types.KeyboardButton(text="Оставить отзыв")
    otz = telebot.types.KeyboardButton(text="Отзывы")

    dnt = telebot.types.KeyboardButton(text="Донат")
    keyboard.add(kod, help,sendotz,otz,dnt)
    bot.send_message(chat_id,
                     'Привет это оффициальный бот h vpn - howdy vpn. Здесь ты можешь получить код. \n Мы принимаем в оплату в крипте ,и звездами ,сбп.',
                     reply_markup=keyboard)
    

    #Нон стоп бот!
bot.polling(none_stop=True)