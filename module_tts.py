from pyrogram import Client, filters
from gtts import gTTS
import os

with open("userbot.info", "r") as file:
    lines = file.readlines()
    prefix_userbot = lines[2].strip()

cinfo = f"🗣`{prefix_userbot}tts`"
ccomand = " Озвучивает текст."


def command_tts(app):
    @app.on_message(filters.command("tts", prefixes=prefix_userbot))
    def tts(client, message):
        if message.reply_to_message and message.reply_to_message.text:
            text = message.reply_to_message.text
            tts = gTTS(text=text, lang='ru')
            tts.save("tts.mp3")
            client.send_voice(message.chat.id, voice="tts.mp3", reply_to_message_id=message.reply_to_message.id)
            os.remove("tts.mp3")
        elif len(message.text.split("tts", maxsplit=1)[1]) > 4:
            text = message.text.split("tts", maxsplit=1)[1]
            tts = gTTS(text=text, lang='ru')
            tts.save("tts.mp3")
            client.send_voice(message.chat.id, voice="tts.mp3", reply_to_message_id=message.id)
            os.remove("tts.mp3")
        else:
            message.edit("**⛔Команду надо писать в ответ на сообщение или писать текст после команды**")

print("Модуль tts загружен!")
