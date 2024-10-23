import telebot

bot = telebot.TeleBot(token='')

@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    name = message.from_user.username
    bot.send_message(user_id, f"Добро пожаловать в бот доставки! {name}")
    bot.send_message(user_id, f"Ведите команду /help {name}")

@bot.message_handler(commands=["help"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Справочная информация")



bot.infinity_polling()