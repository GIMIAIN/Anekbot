from env import TG_API_KEY
from anekdot_ru_hook import getTg
from anekdot_ru_hook import getTgImg
from anekdot_ru_hook import getTgVideo
from telebot import *
from fake_useragent import UserAgent
import requests
import random

TG_API_KEY=TG_API_KEY()

bot = telebot.TeleBot(TG_API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🤡 Анекдот")
    markup.add(btn1)
    bot.send_message(message.chat.id, text='Рад тебя видеть! Я могу рассказать случайный анекдот, так что кликай на кнопку "🤡 Анекдот"'.format(message.from_user), reply_markup=markup)
    bot.register_next_step_handler(message, func)

@bot.message_handler(content_types=['text'])
def func(message):

        if(message.text == "🤡 Анекдот"):
            user_id = str(message.from_user.id)
            url = "https://t.me/baneksru/"
            messageNumber=random.randint(7, 2500)
            #messageNumber=1175
            urlLstPart="?embed=1"
            url = url+str(messageNumber)+urlLstPart
            print("Waiting. URL: "+url+" UserID: "+user_id)
            #if getTgVideo(url)!="None":
                #video = open(getTgVideo(url), 'rb')
                #print(getTgVideo(url))
                #bot.send_video(message.chat.id, video)
            """if getTgImg(url)!="[b'']":
                if getTg(url)!="None":
                    bot.send_photo(message.chat.id, photo=getTgImg(url), caption=getTg(url))
                else:
                    bot.send_photo(message.chat.id, photo=getTgImg(url), caption="")
            elif getTg(url)!="None":
                 bot.send_message(message.chat.id, text=getTg.format(message.from_user))
            else:
                bot.register_next_step_handler(message, func)"""
            response = requests.get(url, headers={'User-Agent': UserAgent().chrome})
            if getTg(response)!="None" and getTgImg(response)!="None":
                bot.send_photo(message.chat.id, photo=getTgImg(response), caption=getTg(response))
            elif getTgImg(response)!="None":
                bot.send_photo(message.chat.id, photo=getTgImg(response), caption="")
            elif getTg(response)!="None":
                bot.send_message(message.chat.id, text=getTg(response))
            elif getTgVideo(response)!="None":
                video = open(getTgVideo(response), 'rb')
                print(getTgVideo(response))
                bot.send_video(message.chat.id, video)
            else:
                 bot.register_next_step_handler(message, func)

            print ("URL: "+url+" UserID: "+user_id)
bot.infinity_polling(timeout=10, long_polling_timeout = 5)
