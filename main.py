import telebot
from dataclasses import dataclass
from typing import Optional
import uuid
from PIL import Image, ImageDraw, ImageFont
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import sovetfc24, topigroki, perks

Bot = telebot.TeleBot("6415922964:AAFs_kBIPud-PnsdHzmwUjtDQiEaAErJ8Tg")




@Bot.message_handler(content_types=["photo"])
def photo_from_user(message):
    Bot.send_message(message.chat.id,
                      '😂')






@Bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Советы по фк24", callback_data='sovetfc24'))
    keyboard.add(InlineKeyboardButton("Топ игроков для начала игры", callback_data='topigroki'),
                 InlineKeyboardButton("Перки", callback_data='perks'), )
    Bot.send_message(chat_id=message.chat.id, text='Чем я могу Вам помочь?', reply_markup=keyboard)


@Bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'sovetfc24':
        pass # Советы по фк24
    elif call.data == 'topigroki':
        pass # Топ игроки для начала игры
    elif call.data == 'perks':
        pass # Перки


Bot.polling(none_stop=True)