from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# keyboards.py
xd = InlineKeyboardButton('News', url='https://t.me/SmokeClown_news')
cmdsbot = InlineKeyboardButton('Commands', callback_data='cmdsbot_callback')
kb_addbot = InlineKeyboardMarkup().add(cmdsbot, xd)
nazad_btn = InlineKeyboardButton('Menu', callback_data='nazad_callback')
nazad = InlineKeyboardMarkup().add(nazad_btn)
