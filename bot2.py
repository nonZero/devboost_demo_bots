import logging

import telebot

import bot_secrets

logging.basicConfig(
    format="[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

bot = telebot.TeleBot(bot_secrets.BOT_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: telebot.types.Message):
    chat_id = message.chat.id
    username = message.from_user.username
    logger.info(f"> Start chat #{chat_id}. username: {username}")
    bot.reply_to(message, """❤️ TELEBOT Welcome! ❤️""")
    # bot.send_message(message, """❤️ TELEBOT Welcome! ❤️""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message: telebot.types.Message):
    chat_id = message.chat.id
    username = message.from_user.username
    text = message.text

    logger.info(f"= Got on chat #{chat_id}/{username!r}: {text!r}")
    response = text.replace("7", "🌸")

    bot.reply_to(message, response)


logger.info("* Start polling...")
bot.infinity_polling()
logger.info("* Bye!")
