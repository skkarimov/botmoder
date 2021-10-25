"""@ʟᴏʀᴅ_ᴄᴏᴅᴇ
ʜᴛᴛᴘs://ᴛ.ᴍᴇ/ʟᴏʀᴅ_ᴄᴏᴅᴇ"""

import random, time, re, asyncio
from datetime import timedelta
import datetime
from langdetect import detect
from aiogram import Bot, Dispatcher, executor, types, md
from LiteSQL import lsql
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.markdown import hlink
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os, config
import keyboards as kb
from ping3 import ping, verbose_ping
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton




bot = Bot('1808197957:AAEAH2esf1qCS5wLOM4fF0eicWd55ujJlfU', parse_mode='html')

dp = Dispatcher(bot, storage=MemoryStorage())

ADMINS = [816209498]

settings = {
	'ref1st': 0.5,
	'ref2st': 0.3,
	'ref3st': 0.1,
	'ref4st': 0.1,
	'ref5st': 0.1,
	'ref6st': 0.1,
	'ref7st': 0.1,
	'ref8st': 0.1,
	'ref9st': 0.1,
	'ref10st': 0.1}

sql = lsql("refbot")

try:
    a = sql.select_data("1", "id")
except:
    sql.create("id, outbalance, name, bhivebalance, fc, ref, regDate, deposit, payout, fetuses, menu, ban, refCount, ref2Count, ref3Count, ref4Count, ref5Count, ref6Count, ref7Count, ref8Count, ref9Count, ref10Count, wb_profits, nott, prize, spinsToday, data, last_bonus")
    sql.insert_data([(0, 0.0, '0', 0.0, 0, 0, '0', 0.0, 0.0, 0, 'main', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '0', '0')], 28)
list_of_user = sql.get_all_data()


async def new_user(user, username, date):
    if user not in list_of_user:
        sql.insert_data([(int(user), 0.0, f'{username}', 0.0, 0, 0, f'{date}', 0.0, 0.0, 0, 'main', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '0', '0')], 28)
        list_of_user.append(user)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	try:
		us = sql.select_data(message.from_user.id, "id")[0]
	except:
		username = message.from_user.username
		await new_user(message.from_user.id, username, message.date)
		try:
			ref = message.text.split()[1]
			reffer = sql.select_data(ref, 'id')[0]
			reff = sql.select_data(reffer2[5], 'id')[0]
			reffer3 = sql.select_data(reff[0], 'id')[0]
			slq.edit_data('id', reffer[0], 'outbalance', (reffer[1]+settings.ref1st))
			sql.edit_data('id', reffer[0], 'refCount', (reffer[12]+1))
			await bot.send_message(reffer.id, f'🔔 Вы пригласили {(hlink("реферала", "tg://user?id={message.from_user.id}"))} 1 уровня и вы получили {settings.ref1st}')
			sql.edit_data('id', reff[0], 'outbalance', reff[2]+settings.ref2st)
			sql.edit_data('id', reffer2[0], 'ref2Count', (reffer2[12]+1))
			await bot.send_message(reffer2[5], f"💸 У Вас новый {(hlink('реферал', 'tg://user?id={message.from_user.id}'))} на 2 уровне и вы получили {settings.ref2st}")
			bonus3 = sql.select_data(reffer3[5], 'id')[0]
			sql.edit_data('id', bonus3[0], 'outbalance', bonus3[1]+settings.ref3st)
			sql.edit_data('id', reffer3[0], 'ref3Count', reffer3[12]+1)
			await bot.send_message(reffer3[5], f"💸 У Вас новый {(hlink('реферал', 'tg://user?id={message.from_user.id}'))} на 3 уровне и вы получили {settings.ref3st}")
		
			reffer4 = sql.select_data(bonus3[0], 'id')[0]
			bonus4 = sql.select_data(reffer4[5], 'id')[0]
			sql.edit_data('id', bonus4[0], 'outbalance', bonus4[1]+settings.ref4st)
			sql.edit_data('id', reffer4[0], 'ref4Count', reffer4[12]+1)
			bot.send_message(reffer4[5], f"💸 У Вас новый {(hlink('реферал', 'tg://user?id={message.from_user.id}'))} на 4 уровне и вы получили {settings.ref4st}")
		
			reffer5 = sql.select_data(bonus4[0], 'id')[0]
			bonus5 = sql.select_data(reffer5[5], 'id')[0]
			sql.edit_data('id', bonus5[0], 'outbalance', bonus5[1]+settings.ref5st)
			sql.edit_data('id', reffer5[0], 'ref5Count', reffer5[12]+1)
			await bot.send_message(reffer5[5], f"💸 У Вас новый {(hlink('реферал', 'tg://user?id={message.from_user.id}'))} на 5 уровне и вы получили {settings.ref5st}")
		
			reffer6 = sql.select_data(bonus5[0], 'id')[0]
			bonus6 = sql.select_data(reffer6[5], 'id')[0]
			sql.edit_data('id', bonus6[0], 'outbalance', bonus6[1]+settings.ref6st)
			sql.edit_data('id', reffer6[0], 'ref6Count', reffer6[12]+1)
			await bot.send_message(reffer6[5], f"💸 У Вас новый {(hlink('реферал', 'tg://user?id={message.from_user.id}'))} на 6 уровне и вы получили {settings.ref6st}")
		
			reffer7 = sql.select_data(bonus6[0], 'id')[0]
			bonus7 = sql.select_data(reffer7[5], 'id')[0]
			sql.edit_data('id', bonus7[0], 'outbalance', bonus7[1]+settings.ref7st)
			sql.edit_data('id', reffer7[0], 'ref7Count', reffer7[12]+1)
			await bot.send_message(reffer7[5], f"💸 У Вас новый {(hlink('реферал', 'tg://user?id={message.from_user.id}'))} на 7 уровне и вы получили {settings.ref7st}")
		
			reffer8 = sql.select_data(bonus7[0], 'id')[0]
			bonus8 = sql.select_data(reffer8[5], 'id')[0]
			sql.edit_data('id', bonus8[0], 'outbalance', bonus8[1]+settings.ref8st)
			sql.edit_data('id', reffer8[0], 'ref8Count', reffer8[12]+1)
			await bot.send_message(reffer8[5], f"💸 У Вас новый {(hlink('реферал', 'tg://user?id={message.from_user.id}'))} на 8 уровне и вы получили {settings.ref8st}")
		
			reffer9 = sql.select_data(bonus8[0], 'id')[0]
			bonus9 = sql.select_data(reffer9[5], 'id')[0]
			sql.edit_data('id', bonus9[0], 'outbalance', bonus9[1]+settings.ref9st)
			sql.edit_data('id', reffer9[0], 'ref9Count', reffer9[12]+1)
			await bot.send_message(reffer9[5], f"💸 У Вас новый {(hlink('реферал', 'tg://user?id={message.from_user.id}'))} на 9 уровне и вы получили {settings.ref9st}")
		
			reffer10 = sql.select_data(bonus9[0], 'id')[0]
			bonus10 = sql.select_data(reffer10[5], 'id')[0]
			sql.edit_data('id', bonus10[0], 'outbalance', bonus10[1]+settings.ref10st)
			sql.edit_data('id', reffer10[0], 'ref10Count', reffer10[12]+1)
			await bot.send_message(reffer10[5], f"💸 У Вас новый {(hlink('реферал', 'tg://user?id={message.from_user.id}'))} на 10 уровне и вы получили {settings.ref10st}")
		except:
			ahajgxhdhshshshshddhshahshshsywysshsusys=1
	uid = message.from_user.id
	us = sql.select_data(message.from_user.id, 'id')[0]
	CHAT_LIST = [-1001424856456, -1001342223740, -1001182837702, -1001214551467]
	suka = [(await bot.get_chat_member(i, uid)).status for i in CHAT_LIST]
	print(suka)
	if "left" in suka:
		print('srabotalo')
		sub = InlineKeyboardButton('Новости', url='t.me/lordref_news')
		sub2 = InlineKeyboardButton('Чат', url='t.me/lordref_chat')
		sub3 = InlineKeyboardButton('Выплаты', url='t.me/lordrefs')
		sub4 = InlineKeyboardButton('Спонсор', url='t.me/lordpromo')
		sub_kb = InlineKeyboardMarkup().add(sub, sub2, sub3, sub4)
		await message.answer('❕ <b>Для использования бота пожалуйста, подпишитесь на наши каналы:</b>', reply_markup=sub_kb)
		print('complete "left proverka')
	else:
		if us[11] == 1:
			print('us[11]')
			return
		if us[2] == '0' or us[2] != message.from_user.username:
			sql.edit_data('id', message.from_user.id, 'name', message.from_user.username)
			print('us[2] srabotalo')
			return
		if message.from_user.id in ADMINS:
			print('ADMINS srabotalo')
			admin_kb = types.ReplyKeyboardMarkup()
			adm_btn = types.KeyboardButton(text='🅰️дминка', resizable=False)
			admin_kb.add(n_1, n_2, n_3, n_4, n_5, n_6, adm_btn)
			await message.answer('Привет, ты админ.', reply_markup=admin_kb)
		else:
			print('else')
			await message.answer('✌️ <b>Привет, ${message.from_user.first_name}</b>\n10-ти уровневая реферальная система💫\n📝 Цель проекта:\n├─Приглашаем рефералов🤘\n├─Получаем доход от рефералов 🧙‍♂ \n└─Выводим💰 \n🌃 Чат → @lordref_chat\n💫 Выплаты →  @lordrefs\n💡 Новости → @lordref_news\n❕ <b>Минимальный вывод от 10₽</b>', reply_markup=main_kb)
			print('else')


@dp.message_handler(content_types=['text'])
async def msg(message: types.Message):
#	try:
#		us = sql.select_data(message.from_user.id, "id")[0]
#	except:
#		username = message.from_user.username
#		await new_user(message.from_user.id, username, 0, message.date)
	uid = message.from_user.id
	if message.chat.id == message.from_user.id:
		await bot.send_message(-1001322323027, f'[{message.date}] Пользователь {uid} отправил: {message.text}')
		us = sql.select_data(message.from_user.id, 'id')[0]
		if us[11] == 1:
		   return
		if us[2] == '0' or us[2] != message.from_user.username:
			sql.edit_data('id', message.from_user.id, 'name', message.from_user.username)
			return
		CHAT_LIST = [-1001424856456, -1001342223740, -1001182837702, -1001214551467]
		suka = [(await bot.get_chat_member(i, uid)).status for i in CHAT_LIST]
		if "left" in suka:
			sub = InlineKeyboardButton('Новости', url='t.me/lordref_news')
			sub2 = InlineKeyboardButton('Чат', url='t.me/lordref_chat')
			sub3 = InlineKeyboardButton('Выплаты', url='t.me/lordrefs')
			sub4 = InlineKeyboardButton('Спонсор', url='t.me/lordpromo')
			sub_kb = InlineKeyboardMarkup().add(sub, sub2, sub3, sub4)
			await message.answer('❕ <b>Для использования бота пожалуйста, подпишитесь на наши каналы:</b>', reply_markup=sub_kb)
		if message.text == 'Профиль ✝':
			withdr = InlineKeyboardButton(text="💰 Вывести", callback_data="withdraw")
			withdr_kb = (types.InlineKeyboardMarkup().add(withdr))
			texts = f"📝 Имя: <b>{0}</b>\n🆔 <b>ID:</b> <code>{1}</code>\n\n📭 <b>На вывод:</b> {2}₽\n\n🗣 <b>Партнеров привлечено: {3}</b> {\n\n👥 <b>Вас привел:</b> {4}\n➖➖➖➖➖➖➖➖➖➖➖\n🤑 <b>Выведено:</b> {5}₽"
			texth = hlink('Пользователь', f'tg//user?={us[5]}')
			texts = texts.format(message.from_user.first_name, message.from_user.id, us[1], us[12], texth, us[8])
			await message.answer(texts, reply_markup=withdr_kb)
		if message.text == 'Рефералы 💸':
			await message.answer(f'<b>😉 в нашем боте ты будешь зарабатывать благодаря нашей 10-ти уровневой реферальной системе. \n1️⃣ Уровень -  0.5₽ \n2️⃣Уровень - 0.3₽\n3️⃣ Уровень - 0.1₽\n4️⃣ Уровень - 0.1₽\n5️⃣ Уровень - 0.1₽\n6️⃣ Уровень - 0.1₽\n7️⃣ Уровень - 0.1₽\n8️⃣ Уровень - 0.1₽\n9️⃣ Уровень - 0.1₽\n🔟 Уровень - 0.1₽\n\n🔗 Твоя реферальная ссылка для приглашений:</b> https://t.me/lordref_bot?start={message.from_user.id}')
		if message.text == 'Стата 💹':
			s = sql.select_data(0, 'id')[0]
			users_today = len(list_of_user)
			adm = types.InlineKeyboardButton(text="Администрация", url="https://t.me/lord_code")
			coder = types.InlineKeyboardButton(text="👨‍💻 Кодер", url="https://t.me/lord_code")
			topsv = types.InlineKeyboardButton(text="Топ выводов 🌲", callback_data="topInv")
			topsr = types.InlineKeyboardButton(text="Топ рефоводов 💫", callback_data="topRef")
			stat_kb = types.InlineKeyboardMarkup(row_width=2).add(adm, coder, topsv, topsr)
			await message.answer(f'\n📊<b> Статистика проекта:</b>\n👨‍💻 Пользователей в проекте: ${users_today}\n👨‍💻 Пользователей сегодня: {users_today}\n📤 Выплачено всего: {(s[1])}₽\n🕐 Старт бота произведен 15.05.2021', reply_markup=(stat_kb))
		if message.text == 'Мои рефералы 💰':
			await message.answer(f'{message.from_user.first_name} в этом разделе ты можешь отслеживать количество своих рефералов \n1️⃣ Уровень - {us[12]}\n2️⃣ Уровень - {us[13]}\n3️⃣ Уровень - {us[14]}\n4️⃣ Уровень - {us[15]}\n5️⃣ Уровень - {us[16]}\n6️⃣ Уровень - {us[17]}\n7️⃣ Уровень - {us[18]}\n8️⃣ Уровень - {us[19]}\n9️⃣ Уровень - {us[20]}\n🔟 Уровень - {us[21]}')
		if message.text == 'FAQ ℹ️':
			own = types.InlineKeyboardButton(text="✝ Владелец", url="https://t.me/lord_code")
			coder = types.InlineKeyboardButton(text="🐍 Прогер", url="https://t.me/lord_code")
			owc_kb = types.InlineKeyboardMarkup(row_width=2).add(own, coder)
			await message.answer(f'❓ Ответы на часто задаваемые вопросы:\n\nВопрос: возможно вывести на карту или другую систему выплат\nОтвет: вывод только на 🥝Qiwi\n\nВопрос: как тут зарабатывать ?\nОтвет: вы можете ежедневно забирать бонус, а также приглашать рефералов и получать вознаграждение за них.\n\nВопрос: за что могут забанить мой аккаунт ?\nОтвет: за мошенничество, попытку накрутки левых людей в боте и так далее. Такие моменты не пройдут, так как перед выплатой, каждый аккаунт проверяется вручную.\n\nОстались вопросы ? Свяжитесь с поддержкой по кнопке ниже!', reply_markup=owc_kb)


if __name__ == '__main__':

    executor.start_polling(dp)