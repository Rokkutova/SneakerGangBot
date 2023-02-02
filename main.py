import telebot
from telebot import types


bot = telebot.TeleBot('5934216303:AAFQHW2Px5DfEw40qa00IEePafuuvO-YiRc')

@bot.message_handler(commands = ['start'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Наша группа Вконтакте', url='https://vk.com/sneakergang_tomsk')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на группу ВК", reply_markup = markup)