import telebot
from anekdot_ru_hook import getTg
from telebot import types

bot = telebot.TeleBot("5246671614:AAE2cTjj4g_V2KqNZQP28F-srrnu_t_umUQ")

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
        bot.send_message(message.chat.id, getTg().format(message.from_user))
bot.polling(none_stop=True)