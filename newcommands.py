import asyncio
import datetime
import os
import random
import re
import sqlite3
from datetime import timedelta
from random import randint

from LiteSQL import lsql
from aiogram import executor
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, message
from aiogram.utils.markdown import hlink
from langdetect import detect
from meval import meval

from configurator import config
from dispatcher import dp, bot

ADMINS = [1916288033]
af = {}

chatsql = lsql("chats")

try:
    a = chatsql.select_data("1", "id")
except:
    chatsql.create(
        "id, link, text, welcomes, randomais, mats, sms, rules, on_off, re_on, tixiy, arabs, repa, reports, links")
    chatsql.insert_data([(0, 'link', '0', 1, 0, 0, 0, ' ', 1, 0, 4, 1, 1, 1, 1)], 15)
chatsqlall = chatsql.get_all_data()

sql = lsql("test")
try:
    a = sql.select_data("1", "id")
except:
    sql.create("id, balance, username, btc, repa")
    sql.insert_data([(0, 100, '0', 0.0, 0)], 5)

conn = sqlite3.connect("db.db")
cursor = conn.cursor()
sql = lsql("users")

try:
    a = sql.select_data("1", "id")
except:
    sql.create("id, username, repa, warn, admchat, brak, regDate")
    sql.insert_data([(0, '0', 0, 0, 0, 0, '2021')], 7)

slovql = lsql("slovadb")

try:
    a = slovql.select_data("slova", "1")
except:
    slovql.create("slova")
    slovql.insert_data('1', 1)
slovall = slovql.get_all_data()

list_of_user = sql.get_all_data()

stickql = lsql('stickers')
try:
    stickql.select_data("1", 'id')
except:
    stickql.create('id, gey')

stickall = stickql.get_all_data()

for i in range(len(list_of_user)):
    list_of_user[i] = list_of_user[i][0]


async def new_sticker(id, gey):
    stickql.insert_data([(f"{id}", gey)], 2)


async def new_user(user, username):
    if user not in list_of_user:
        sql.insert_data([(int(user), f'{username}', 0, 0, 0, 0, f'{datetime.datetime.now()}')], 7)
        list_of_user.append(user)


async def new_chat(chat, link):
    if chat not in chatsqlall:
        chatsql.insert_data([(int(chat), f'{link}', 'text', 1, 0, 0, 0, ' ', 1, 0, 4, 1, 1, 1, 1)], 15)
        chatsqlall.append(chat)


async def new_slovo(text):
    if text not in slovall:
        slovql.insert_data((str(text)), 1)
        slovall.append(str(text))


async def repafun(user):
    us = sql.select_data(user, 'id')[0]
    sql.edit_data('id', user, 'repa', int(us[2]) + 1)


async def unrepafun(user):
    us = sql.select_data(user, 'id')[0]
    if int(us[2]) <= 0:
        sql.edit_data('id', user, 'repa', 0)
    else:
        sql.edit_data('id', user, 'repa', int(us[2]) - 1)

async def getattrs(message):
    return {"reply": message.reply_to_message,
            "message": message,
            "bot": bot,
            "dp": dp,
            "chat": message.chat}


@dp.message_handler(content_types=['text'])
async def msg(message: types.Message):
	try:
		us = sql.select_data(message.from_user.id, "id")[0]
	except:
		username = message.from_user.username
		await new_user(message.from_user.id, username)
	try:
		chats = chatsql.select_data(message.chat.id, "id")[0]
	except IndexError:
		chats = 0
		link = await message.chat.get_url()
		link = str(link)
		await new_chat(message.chat.id, link)
	us = sql.select_data(message.from_user.id, "id")[0]
	chatsss = chatsql.select_data(message.chat.id, 'id')[0]
	if re.search(r'http\S+', message.text) or re.search(r't.me\S+', message.text) or re.search(r'@\S+', message.text) or re.search(r'//\S+', message.text):
		if chatsss[14] == 1:
			admt = await message.chat.get_member(message.from_user.id)
			if admt.is_chat_admin():
				return
			await message.delete()
