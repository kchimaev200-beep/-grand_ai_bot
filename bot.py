import os
import telebot
from telebot import types

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2
    )

    markup.add(
        types.KeyboardButton("🎁 Новые промокоды"),
        types.KeyboardButton("📰 Новости"),
        types.KeyboardButton("🤖 Спросить AI"),
        types.KeyboardButton("📜 Правила сервера"),
        types.KeyboardButton("🔎 Найти правило"),
        types.KeyboardButton("🔔 Уведомления"),
        types.KeyboardButton("🎉 Ивенты")
    )

    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в Grand Mobile TJK Bot!\n\n"
        "Здесь ты сможешь получать промокоды, новости "
        "и задавать вопросы по правилам сервера. 🚀",
        reply_markup=markup
    )


@bot.message_handler(func=lambda message: True)
def messages(message):

    if message.text == "🎁 Новые промокоды":
        bot.send_message(
            message.chat.id,
            "🎁 Новые промокоды\n\n"
            "Пока новых промокодов нет.\n"
            "🔔 Я автоматически сообщу, когда появится новый промокод."
        )

    elif message.text == "📰 Новости":
        bot.send_message(
            message.chat.id,
            "📰 Новости Grand Mobile\n\n"
            "Пока новых новостей нет."
        )

    elif message.text == "🤖 Спросить AI":
        bot.send_message(
            message.chat.id,
            "🤖 Напиши свой вопрос по Grand Mobile.\n\n"
            "Например:\n"
            "• Что такое ДМ?\n"
            "• За сколько считается AFK?\n"
            "• Можно ли нарушать RP?"
        )

    elif message.text == "📜 Правила сервера":
        bot.send_message(
            message.chat.id,
            "📜 Правила сервера\n\n"
            "Раздел находится в разработке."
        )

    elif message.text == "🔎 Найти правило":
        bot.send_message(
            message.chat.id,
            "🔎 Напиши ключевое слово.\n"
            "Например: ДМ, ТК, AFK, RP."
        )

    elif message.text == "🔔 Уведомления":
        bot.send_message(
            message.chat.id,
            "🔔 Уведомления\n\n"
            "🎁 Промокоды — включены\n"
            "📰 Новости — включены\n"
            "🎉 Ивенты — включены"
        )

    elif message.text == "🎉 Ивенты":
        bot.send_message(
            message.chat.id,
            "🎉 Ивенты Grand Mobile\n\n"
            "Пока активных ивентов нет."
        )

    else:
        bot.send_message(
            message.chat.id,
            "🤖 Я пока не понял этот запрос.\n"
            "Используй кнопки меню 👇"
        )


print("Grand Mobile TJK Bot запущен!")

bot.infinity_polling()
