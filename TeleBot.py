import telebot

bot = telebot.TeleBot("6523437791:AAFEf3OQuxpAaAGw4lBRwAyMuYM5e9_0xeg")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id, message.text)
# bot.reply_to(message, message.text)


bot.infinity_polling(none_stop=True)
