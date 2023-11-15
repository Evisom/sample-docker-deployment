import telebot
import os
from SampleClass import SampleClass

TOKEN = os.environ.get('TOKEN', 'null')
print(TOKEN)
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def handle_start(message):
    point1 = SampleClass(1,2)
    point2 = SampleClass(1,2)
    point3 = point1+point2
    bot.send_message(message.chat.id, "Hello World!")
    bot.send_message(message.chat.id, f'Point: {point3.x}, {point3.y}')

if __name__ == "__main__":
    bot.polling(none_stop=True)