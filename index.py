import telebot
import secret
import random
import hashlib
import os
import database as db
bot = telebot.TeleBot(secret.bot)


print("Бот запущен")
#Рандомный код 
@bot.message_handler(commands=["code"] )
@bot.message_handler(regexp="Получить код" )
def repeat_all_messages(message): 
    if (db.have(message.from_user.id)==0):
        b = str(random.randint(100,100000))
        ba = secret.a+b+secret.b
        c = hashlib.md5(ba.encode()).hexdigest()
        msg = message.from_user.id
        db.add_to_free(msg,c)
        print(db.have(msg))
        
    else:
        c = "Вы уже получали!"
    bot.send_message(message.chat.id,c)


#Убийство бота
    @bot.message_handler(commands=[secret.kill] )
    def kill(message):
        bot.send_message(message.chat.id, "ИЗвини но иди подальнше ,ладно иду спать!")
        bot.stop_polling()
        os.system("clear||cls")
        print(f"{message.from_user.username} ({message.from_user.id}) убил бота через комманду")
        

#Поддержка
@bot.message_handler(commands=["help"])
@bot.message_handler(regexp="Связь с поддержкой" )
def hiAi(message): 
    bot.send_message(message.chat.id, "@hvpn_help_bot. - Бот поддержки нашего впн сервиса")

#Донат
@bot.message_handler(regexp="Донат" )
def donat(message): 
    keyboard = telebot.types.InlineKeyboardMarkup()
    sbp = telebot.types.InlineKeyboardButton(text="Сбп" ,callback_data="sbp")
    stars = telebot.types.InlineKeyboardButton(text="Звезды" ,callback_data="stars" )
    crypra = telebot.types.InlineKeyboardButton(text="Крипта" ,callback_data="crypta")
    keyboard.add(sbp,stars,crypra)
    bot.send_message(message.chat.id, "Выбери чем вы хотите задонатить?", reply_markup=keyboard)

#Отзывы
@bot.message_handler(regexp="Отзывы" )
def otz(message): 
    if (db.last_otz() !=None):
        bot.send_message(message.chat.id,  f"Последний отзыв:  <blockquote>{db.last_otz()}</blockquote> Данный отзыв не проверялся администацией!", parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, "Отзывов нету!")
    

#Оставить отзыв
@bot.message_handler(regexp="Оставить отзыв" )
def send_otz(message): 
    if (db.have(message.from_user.id)>=1):
        if(db.usersendtext(message.from_user.id)<=0):
            c="Введите ваш отзыв:"
            bot.send_message(message.chat.id, c)
            bot.register_next_step_handler(message, process_name_step)
        else:
            c = "Вы уже отправляли отзыв!"
            bot.send_message(message.chat.id, c)
    else:
        c = "Вы не наш клиент!"
        bot.send_message(message.chat.id, c)

#ожидание что пользователь напишет!
def process_name_step(message):
    db.add_message(message.from_user.id , message.text)
    bot.send_message(message.chat.id, "Спасибо ,за ваш великолепный отзыв!")

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
    

#callback
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "sbp":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, "+79933057642")
        elif call.data == "stars":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, "Киньте на @imyrj")
        elif call.data == "crypta":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, " Кошелек - UQApm4N2sSkbLgqGPHi1bfIgF6O0m-L9h4vW6bNvyuQHmtr2")
        else:
            bot.send_message(call.message.chat.id, "Неверно!")



    #Нон стоп бот!
bot.polling(none_stop=True)