import telebot
from config import token
import keyboard as kb
from message_parser import parse_msg

bot = telebot.TeleBot(token)


# первый запуск, начало работы
@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.send_photo(message.chat.id, open('./menu.jpg', 'rb'), 'Scout Bot - поможет Вам следить за '
                                                              'сообщениями связанными с вашими интересами 💬\n\n'
                                                              'Нахожу сообщения и тут же отправляю их тебе 🔥',
                   reply_markup=kb.menu)


# меню
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'parse':
        parse_msg()
    else:
        pass


bot.infinity_polling(none_stop=True)

