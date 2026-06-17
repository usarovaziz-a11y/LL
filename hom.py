import telebot
import os
TOKEN = "8919118546:AAEwCUF6-y54xttOL3W8nJTxVyfhYfaa-n0"
bot = telebot.TeleBot(TOKEN)

SAVE_DIR = "photo"
os.makedirs(SAVE_DIR, exist_ok=True)

@bot.message_handler(content_types=["photo"])
def save_photo(message):
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image.jpg", "wb") as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Фотография сохранена!")

@bot.message_handler(content_types=["document"])
def save_document(message):
    document = message.document
    file_info = bot.get_file(document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(document.file_name, "wb") as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "документ сохранена!")
# Запускаем постоянную работу бота
bot.infinity_polling()