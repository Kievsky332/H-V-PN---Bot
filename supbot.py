import telebot
import secret
from openai import OpenAI
import os
import datetime


bot = telebot.TeleBot(secret.bot_help)
st ="Запущен хэлпер бот\n"
x =  f"\n{datetime.datetime.now() .strftime("%d.%m.%Y %H:%M:%S ")}"
print(x+st)
file = open("C:\github\H-V-PN---Bot\log.txt", "w",encoding='utf-8')
file.write(x+st)
file.close



#Убийство бота
@bot.message_handler(commands=[secret.kill] )
def kill(message):
    bot.send_message(message.chat.id, "ИЗвини но  иду спать!")
    bot.stop_polling()
    a = f"\n\n{message.from_user.username} ({message.from_user.id}) убил бота через комманду"
    file = open("C:\github\H-V-PN---Bot\log.txt", "w",encoding='utf-8')
    print(x+a)
    file.write(x+a)
    file.close()
    


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id , f"{message.from_user.username} Привет чем помочь?")


@bot.message_handler(content_types=["text"])
def ai(message):
        print(" ")
        file = open("C:\github\H-V-PN---Bot\log.txt", "w",encoding='utf-8')
        file.write("\n\n")        
        
        user = f"\n{message.from_user.username} :  {message.text}"
        print(x+user)
        file.write(x+user)
        file.close
        #ии бот приветствие 
        client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=secret.api,
        )
        completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
            "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
        },
        extra_body={},
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
        ]
        )
        bot.send_message(message.chat.id, completion.choices[0].message.content)
        ai = "\nИи: "+completion.choices[0].message.content
        
        print(x+ai)
        file = open("C:\github\H-V-PN---Bot\log.txt", "w",encoding='utf-8')
        file.write(x+ai)
        file.close

bot.polling(none_stop=True)