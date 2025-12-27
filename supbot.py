import telebot
import secret
from openai import OpenAI
import os
import datetime
import logging

bot = telebot.TeleBot(secret.bot_help)

logging.basicConfig(level=logging.ERROR, filename="bot.log",filemode="w",
                    format="%(asctime)s  %(message)s")

st ="Запущен хэлпер бот\n"
print(st)
logging.error(st)



#Убийство бота
@bot.message_handler(commands=[secret.kill] )
def kill(message):
    bot.send_message(message.chat.id, "ИЗвини но  иду спать!")
    bot.stop_polling()
    a = f"\n\n{message.from_user.username} ({message.from_user.id}) убил бота через комманду"
    print(a)
    logging.error(a)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id , f"{message.from_user.username} Привет чем помочь?")


@bot.message_handler(content_types=["text"])
def ai(message):
        print(" ")    
        
        user = f"{message.from_user.username} :  {message.text}"
        print(user)
        logging.error(user)

        #ии бот приветствие 
        client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=secret.api,
        )
                # First API call with reasoning
        response = client.chat.completions.create(
        model="mistralai/devstral-2512:free",
        messages=[
                {
                    "role": "system",
                    "content": secret.prompt
                },
                {
                    "role": "user",
                    "content": message.text
                }
                ],
        extra_body={"reasoning": {"enabled": True}}
        )

        bot.send_message(message.chat.id, response.choices[0].message.content)
        ai = "Ии: "+response.choices[0].message.content+ f" (ответ для @{message.from_user.username})"+"\n"
        
        print(ai)
        logging.error(ai)

bot.polling(none_stop=True)