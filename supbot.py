import telebot
import secret
from openai import OpenAI
import os

print("Запущен хэлпер бот")
bot = telebot.TeleBot(secret.bot_help)

#Убийство бота
@bot.message_handler(commands=[secret.kill] )
def kill(message):
    bot.send_message(message.chat.id, "ИЗвини но  иду спать!")
    bot.stop_polling()
    os.system("clear||cls")
    print(f"{message.from_user.username} ({message.from_user.id}) убил бота через комманду")

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id , f"{message.from_user.username} Привет чем помочь?")

@bot.message_handler(content_types=["text"])
def ai(message):
        print(" ")
        print(message.from_user.username+" : "+ message.text)
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
        print("Ии: "+completion.choices[0].message.content)

    #Нон стоп бот!
bot.polling(none_stop=True)