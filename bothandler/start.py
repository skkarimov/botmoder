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
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import hlink
from langdetect import detect
from meval import meval

import data
from configurator import config
from dispatcher import dp, bot

try:
    pathasdsadasdasd = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'slovadb.db')
    os.remove(pathasdsadasdasd)
except FileNotFoundError:
    print('ladno')



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


@dp.message_handler(commands=['eval'], commands_prefix=['/', '!'])
async def eval(message: types.Message):
    if message.from_user.id == 1916288033:
        try:
            args = message.get_args()
            cmd_eval = await meval(args, globals(), **await getattrs(message))
            await message.reply(
                f"<b>Выполненное выражение:</b>\n<code>{args}</code>\n\n<b>Возвращено:</b>\n<code>{cmd_eval}</code>")
        except Exception as e:
            return await message.reply(
                f"<b>Не удалось выполнить выражение:</b>\n<code>{args}</code>\n\n<b>Возвращено:</b>\n<code>{e}</code>")
    else:
        await message.reply("Вам не доступна эта функция!")


@dp.message_handler(Text("Сколько у меня iq?", ignore_case=True))
async def iq(message: types.Message):
    await message.reply('🧠 Похоже, что у тебя ' + str(randint(0, 100)) + 'iq')

@dp.message_handler(Text("сколько у меня iq?", ignore_case=True))
async def iq(message: types.Message):
    await message.reply('🧠 Похоже, что у тебя ' + str(randint(0, 100)) + 'iq')

@dp.message_handler(Text("когда я умру?", ignore_case=True))
async def fff(message: types.Message):
    h = ["Января", "Февраля", "Марта", "Апреля", "Мая", "Июня", "Июля", "Августа", "Сентября", "Октября", "Ноября",
         "Декабря"]
    j = ["😱", "⚰", "☠"]
    u = random.choice(j)
    g = random.choice(h)
    await message.answer(
        f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> ты умрешь {u}  {random.randint(1, 30)} {g} {random.randint(2021, 2091)} года.""")

@dp.message_handler(Text("Когда я умру?", ignore_case=True))
async def fff(message: types.Message):
    h = ["Января", "Февраля", "Марта", "Апреля", "Мая", "Июня", "Июля", "Августа", "Сентября", "Октября", "Ноября",
         "Декабря"]
    j = ["😱", "⚰", "☠"]
    u = random.choice(j)
    g = random.choice(h)
    await message.answer(
        f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> ты умрешь {u}  {random.randint(1, 30)} {g} {random.randint(2021, 2091)} года.""")


@dp.message_handler(Text("Бот", ignore_case=True))
async def fff(message: types.Message):
    h = ["Чаво тебе?", "бля, да что?", "Я тут, хули надо?", "Та блять дай поспать", "Ушёл в запой",
         "Гнида, не беспокой пожалуйста:),", "М?", "Што?", "Я тут, как дела?", "Я занят, иди гуляй",
         "Я тут, что прикажите?", "Дя"]
    g = random.choice(h)
    await message.answer(f"""{g} 🤡""")

@dp.message_handler(Text("бот", ignore_case=True))
async def fff(message: types.Message):
    h = ["Чаво тебе?", "бля, да что?", "Я тут, хули надо?", "Та блять дай поспать", "Ушёл в запой",
         "Гнида, не беспокой пожалуйста:),", "М?", "Што?", "Я тут, как дела?", "Я занят, иди гуляй",
         "Я тут, что прикажите?", "Дя"]
    g = random.choice(h)
    await message.answer(f"""{g} 🤡""")

'''@dp.message_handler(lambda message: message.text.lower() == 'игра')
async def process_command_1(message: types.Message):
    button1 = InlineKeyboardButton('🗿Камень🖤', callback_data='1')
    button2 = InlineKeyboardButton('✂️Ножницы💔', callback_data='2')
    button3 = InlineKeyboardButton('📄Бумага🤍', callback_data='3')
    buttons = InlineKeyboardMarkup().add(button1, button2, button3)
    await bot.send_message(message.chat.id, "Я готов!\nВыбери предмет, чтобы победить меня УАХАХА\n*зловещий смех*",
                           reply_markup=buttons)


@dp.callback_query_handler(lambda c: c.data == '1')
async def process_callback_yes(callback: types.CallbackQuery):
    rand = random.choice(["🗿Камень🖤", "✂️Ножницы💔", "📄Бумага🤍"])

    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer("Я выбрал " + rand + "\nА ты выбрал 🗿Камень🖤")
    if rand == '🗿Камень🖤':
        await callback.message.answer("⚔️НИЧЬЯ⚔️")
    elif rand == '✂️Ножницы💔':
        await callback.message.answer("😵🔫ПОБЕДА ЗА ТОБОЙ👻✅")
    else:
        await callback.message.answer("😈☠️Я ПОБЕДИЛ😈☠️")


@dp.callback_query_handler(lambda c: c.data == '2')
async def process_callback_yes(callback: types.CallbackQuery):
    rand = random.choice(["🗿Камень🖤", "✂️Ножницы💔", "📄Бумага🤍"])

    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer("Я выбрал " + rand + "\nА ты выбрал ✂️Ножницы💔")
    if rand == '🗿Камень🖤':
        await callback.message.answer("😈☠️Я ПОБЕДИЛ😈☠️")
    elif rand == '✂️Ножницы💔':
        await callback.message.answer("⚔️НИЧЬЯ⚔️")
    else:
        await callback.message.answer("😵🔫ПОБЕДА ЗА ТОБОЙ👻✅")


@dp.callback_query_handler(lambda c: c.data == '2')
async def process_callback_yes(callback: types.CallbackQuery):
    rand = random.choice(["🗿Камень🖤", "✂️Ножницы💔", "📄Бумага🤍"])

    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer("Я выбрал " + rand + "\nА ты выбрал ✂️Ножницы💔")
    if rand == '🗿Камень🖤':
        await callback.message.answer("😈☠️Я ПОБЕДИЛ😈☠️")
    elif rand == '✂️Ножницы💔':
        await callback.message.answer("⚔️НИЧЬЯ⚔️")
    else:
        await callback.message.answer("😵🔫ПОБЕДА ЗА ТОБОЙ👻✅")


@dp.callback_query_handler(lambda c: c.data == '2')
async def process_callback_yes(callback: types.CallbackQuery):
    rand = random.choice(["🗿Камень🖤", "✂️Ножницы💔", "📄Бумага🤍"])

    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer("Я выбрал " + rand + "\nА ты выбрал ✂️Ножницы💔")
    if rand == '🗿Камень🖤':
        await callback.message.answer("😈☠️Я ПОБЕДИЛ😈☠️")
    elif rand == '✂️Ножницы💔':
        await callback.message.answer("⚔️НИЧЬЯ⚔️")
    else:
        await callback.message.answer("😵🔫ПОБЕДА ЗА ТОБОЙ👻✅")


@dp.callback_query_handler(lambda c: c.data == '3')
async def process_callback_yes(callback: types.CallbackQuery):
    rand = random.choice(["🗿Камень🖤", "✂️Ножницы💔", "📄Бумага🤍"])

    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer("Я выбрал " + rand + "\nА ты выбрал 📄Бумага🤍")
    if rand == '🗿Камень🖤':
        await callback.message.answer("😵🔫ПОБЕДА ЗА ТОБОЙ👻✅")
    elif rand == '✂️Ножницы💔':
        await callback.message.answer("😈☠️Я ПОБЕДИЛ😈☠️")
    else:
        await callback.message.answer("⚔️НИЧЬЯ⚔️")'''


'''@dp.message_handler(regexp=r"(^Куб|куб) ?(\d+)? ?(\d+)?")
async def process_start_command(message: types.Message):
    command_parse = re.compile(r"(^Куб|куб) ?(\d+)? ?(\d+)?")
    parsed = command_parse.match(message.text)
    dice_value = parsed.group(2)
    dice_value = int(dice_value)
    summ = parsed.group(3)
    summ = (summ)
    name1 = message.from_user.get_mention(as_html=True)
    if int(summ) >= int(275000000000):
        if dice_value > 6:
            await message.reply(f"<b>{name1}</b> введите сообщение в формате: \n<b>Куб (число от 1 до 6) (ставка)</b>",
                                parse_mode='html')
        else:
            if not summ:
                await message.reply(
                    f"<b>{name1}</b> введите сообщение в формате: \n<b>Куб (число от 1 до 6) (ставка)</b>",
                    parse_mode='html')
            else:
                if not dice_value:
                    await message.reply(
                        f"<b>{name1}</b> введите сообщение в формате: \n<b>Куб (число от 1 до 6) (ставка)</b>",
                        parse_mode='html')
                else:
                    balanc = cursor.execute("SELECT balance from users where user_id = ?",
                                            (message.from_user.id,)).fetchone()
                    balance = (balanc[0])
                    summ = int(summ)
                    if balance >= summ:
                        dice_value = int(dice_value)
                        bot_data = await bot.send_dice(message.chat.id)
                        bot_data = bot_data['dice']['value']
                        plus = bot_data + 1
                        minus = bot_data - 1
                        summ2 = summ * 10
                        data = {}
                        data["suma"] = summ
                        data['user_id'] = message.from_user.id
                        data1 = {}
                        data1["suma"] = summ2
                        data1['user_id'] = message.from_user.id
                        await sleep(5)

                        if bot_data > dice_value:
                            await message.reply(f'{name1} ты проиграл(а) <b>{summ}</b>💰', parse_mode='html')
                            cursor.execute("""UPDATE users SET balance = balance - :suma WHERE user_id = :user_id;""",
                                           data)

                        elif bot_data < dice_value:
                            await message.reply(f'{name1} ты проиграл(а) <b>{summ}</b>💰', parse_mode='html')
                            cursor.execute("""UPDATE users SET balance = balance - :suma WHERE user_id = :user_id;""",
                                           data)

                        else:
                            await message.reply(f'{name1} ты выиграл(а) <b>{summ2}</b>💰', parse_mode='html')
                            cursor.execute("""UPDATE users SET balance = balance + :suma WHERE user_id = :user_id;""",
                                           data1)
                        conn.commit()

                    elif balance < summ:
                        balanc = cursor.execute("SELECT balance from users where user_id = ?",
                                                (message.from_user.id,)).fetchone()
                        balance = (balanc[0])
                        await message.reply(f'{name1} у тебя нет столько 💰\nТвой баланс:{balance}💰 ',
                                            parse_mode='html')
    else:
        await message.reply(f'{name1} нельзя играть на сумы более <code>275000000000</code>💰', parse_mode='html')'''


'''@dp.message_handler(commands=['rp'])
async def help_message(msg: types.Message):
    await msg.reply("""В разработке...""")'''

@dp.message_handler(chat_id=config.groups.main, commands=['game'], commands_prefix=['/', '.', '!'])
async def help_message(msg: types.Message):
    await msg.reply("""<b><code>/bonus</code> – выдам бонус в размере 5000 монет. (временно не работает)
<code>/balance</code> – узнать сколько у тебя игровых монет. (временно не работает)
<code>/me</code> – покажу статистику о тебе(онли в чате)
<code>Куб</code> (число от 1 до 6) (ставка) – сыграть в кубик, при выигрыше x6 к ставке. (временно не работает)
<code>/gay</code> – покажу на сколько процентов ты гей.
<code>/хохол</code> – покажу на сколько процентов ты хохол.
<code>/dick</code> – увеличить свой dick(временно не работает)
<code>Игра</code> – игра в суефа с ботом(скоро сделаю с разными игроками) (временно не работает)
<code>Когда я умру?</code> – покажу когда ты умрешь:)
<code>Сколько у меня iq?</code> – покажу сколько у тебя iq</b>""")


'''@dp.message_handler(commands=['admins'])
async def help_message(msg: types.Message):
    await msg.reply("""В разработке....""")'''


'''@dp.message_handler(commands=['help'])
async def help_message(msg: types.Message):
    await msg.reply("""<b>Полная документация по боту  находится ниже:

<code>/admins</code> – список команд для админов чата.
➖➖➖➖➖➖➖
<code>/game</code> – список игровых команд.
➖➖➖➖➖➖➖
<code>/rp</code> – список рп команды бота.
➖➖➖➖➖➖➖
Данный бот находится в разработке, если найдете какой либо баг или неработоспособность бота обратитесь к создателю – @king_of_this_world_1</b>""")'''


@dp.message_handler(commands=['setbal'], commands_prefix=['/', '!', '.'])
async def setbal(message: types.Message):
    args = message.get_args()
    cursor.execute("SELECT * FROM users WHERE user_id=?", (message.from_user.id,))
    data = cursor.fetchone()
    if data is None:
        return await message.reply("Не найден в базе данных!")
    if message.from_user.id in ADMINS:
        reply = message.reply_to_message
        if reply:
            replyuser = reply.from_user
            cursor.execute(f'UPDATE users SET balance=? WHERE user_id=?', (args, replyuser.id,))
            conn.commit()
            await message.reply(f"Баланс {replyuser.first_name}, изменён на {args} монеток.")
        else:
            await message.reply("Где реплай дибил.")
    else:
        return await message.reply("Ты не админ.")


'''@dp.message_handler(commands=['balance'])
async def balance(message: types.Message):
    cursor.execute("SELECT * FROM users WHERE", (message.from_user.id,))
    data = cursor.fetchone()
    if data is None:
        return await message.reply("Не найден в базе данных! В лс у бота пиши /start")
    await message.reply(f"Ваш баланс - {data[1]}")'''


@dp.message_handler(commands=['randsticker', 'sticker'], commands_prefix=['/', '!', '.'])
async def start(message: types.Message):
    if message.chat.id != message.from_user.id:
        srik = [i[0] for i in stickall]
        stick = random.choice(srik)
        await message.reply_sticker(stick)


'''@dp.message_handler(commands=['hp'])
async def xd(message: types.Message):
    rp_btn = InlineKeyboardButton(text='RP', callback_data='rp')
    games_btn = InlineKeyboardButton(text='Games', callback_data='games')
    mod_btn = InlineKeyboardButton(text='Moderation', callback_data='mod')
    help_kb = InlineKeyboardMarkup().add(rp_btn, games_btn, mod_btn)
    await message.answer('тыкай бля.', reply_markup=help_kb)'''


'''@dp.callback_query_handler(text="rp")
async def qwerty(call: types.CallbackQuery):
    await call.message.answer(text='В разработке...')'''


@dp.callback_query_handler(text="games")
async def qwerty(call: types.CallbackQuery):
    await call.message.answer(text="""<b><code>/bonus</code> – выдам бонус в размере 5000 монет. (временно не работает)
<code>/balance</code> – узнать сколько у тебя игровых монет. (временно не работает)
<code>Кто я?</code> – покажу известную мне информацию о тебе.
<code>Куб</code> (число от 1 до 6) (ставка) – сыграть в кубик, при выигрыше x6 к ставке. (временно не работает)
<code>/gay</code> – покажу на сколько процентов ты гей.
<code>/хохол</code> – покажу на сколько процентов ты хохол.
<code>/dick</code> – увеличить свой dick(временно не работает)
<code>Игра</code> – игра в суефа с ботом(скоро сделаю с разными игроками) (временно не работает)
<code>Когда я умру?</code> – покажу когда ты умрешь:)</b>""")


'''@dp.callback_query_handler(text="mod")
async def qwerty(call: types.CallbackQuery):
    await call.message.answer(text='В разработке...')'''


'''@dp.message_handler(commands=['ping', 'пинг'], commands_prefix=["/", "!"])
async def ping(message: types.Message):
    a = time.time()
    bot_msg = await message.answer(f'Проверка пинга...')
    if bot_msg:
        b = time.time()
    await bot_msg.edit_text(f'Пинг бота: {round((b - a) * 1000)} мс')'''


@dp.message_handler(Text("Кто я?", ignore_case=True))
async def govno(message: types.Message):
    await message.answer(f"""📝Вот мне известная информацию о тебе:)
<b>✅Имя</b>: <code>{message.from_user.first_name}</code>
<b>✅Фамилия</b>: <code>{message.from_user.last_name}</code>
<b>✅Юзернейм</b>: @{message.from_user.username}
<b>🆔ID</b>: <code>{message.from_user.id}</code>
<b>👅Язык</b>: <code>{message.from_user.language_code}</code>
<b>🔗Ссылка</b>: <a href='tg://user?id={message.from_user.id}'>Ссылка</a>""")

@dp.message_handler(Text("Кто я", ignore_case=True))
async def govno(message: types.Message):
    await message.answer(f"""📝Вот мне известная информацию о тебе:)
<b>✅Имя</b>: <code>{message.from_user.first_name}</code>
<b>✅Фамилия</b>: <code>{message.from_user.last_name}</code>
<b>✅Юзернейм</b>: @{message.from_user.username}
<b>🆔ID</b>: <code>{message.from_user.id}</code>
<b>👅Язык</b>: <code>{message.from_user.language_code}</code>
<b>🔗Ссылка</b>: <a href='tg://user?id={message.from_user.id}'>Ссылка</a>""")

@dp.message_handler(Text("кто я?", ignore_case=True))
async def govno(message: types.Message):
    await message.answer(f"""📝Вот мне известная информацию о тебе:)
<b>✅Имя</b>: <code>{message.from_user.first_name}</code>
<b>✅Фамилия</b>: <code>{message.from_user.last_name}</code>
<b>✅Юзернейм</b>: @{message.from_user.username}
<b>🆔ID</b>: <code>{message.from_user.id}</code>
<b>👅Язык</b>: <code>{message.from_user.language_code}</code>
<b>🔗Ссылка</b>: <a href='tg://user?id={message.from_user.id}'>Ссылка</a>""")

@dp.message_handler(Text("кто я", ignore_case=True))
async def govno(message: types.Message):
    await message.answer(f"""📝Вот мне известная информацию о тебе:)
<b>✅Имя</b>: <code>{message.from_user.first_name}</code>
<b>✅Фамилия</b>: <code>{message.from_user.last_name}</code>
<b>✅Юзернейм</b>: @{message.from_user.username}
<b>🆔ID</b>: <code>{message.from_user.id}</code>
<b>👅Язык</b>: <code>{message.from_user.language_code}</code>
<b>🔗Ссылка</b>: <a href='tg://user?id={message.from_user.id}'>Ссылка</a>""")

@dp.message_handler(commands=['hohol', 'хохол'], commands_prefix=["/", "!"])
async def hohol(message: types.Message):
    hohol = random.randrange(0, 101)
    if hohol <= 1:
        await bot.send_message(message.chat.id,
                               ("🐷 " "БЛЯ УВАЖУХА!!! Ты хохол на " + str(hohol) + "%" " 🐷\nРеспект!"))
    elif hohol <= 10:
        await bot.send_message(message.chat.id, ("🐷 " "ВОУ-ВОУ-ВОУ ты хохол на " + str(hohol) + "%" " 🐷\nРеспект"))
    elif hohol <= 30:
        await bot.send_message(message.chat.id, ("🐷 " "Поздравляю🎉🐷\n🐷 Ты хохол на " + str(hohol) + "%" " 🐷"))
    elif hohol <= 50:
        await bot.send_message(message.chat.id,
                               ("🐷 " "Это BAN... Чё ещё.🐷\n🐷 Ты хохол на " + str(hohol) + "%" " 🐷"))
    elif hohol <= 70:
        await bot.send_message(message.chat.id, ("🐷 " "Мы тебя теряем..🐷\n🐷 Ты хохол на " + str(hohol) + "%" " 🐷"))
    elif hohol <= 80:
        await bot.send_message(message.chat.id,
                               ("🐷 " "Капец.. Не надо так🐷\n🐷 Ты хохол на " + str(hohol) + "%" " 🐷"))
    elif hohol <= 98:
        await bot.send_message(message.chat.id, ("🐷 " "Оуу.. Всё плохо..🐷\n🐷Ты хохол на " + str(hohol) + "%" " 🐷"))
    elif hohol <= 99:
        await bot.send_message(message.chat.id, ("🐷 " "Да ты на грани..🐷\n🐷Ты хохол на " + str(hohol) + "%" " 🐷"))
    elif hohol >= 100:
        await bot.send_message(message.chat.id,
                               ("🐷 " "Тут просто Pres F...🐷\n🐷Ты хохол на " + str(hohol) + "%" " 🐷"))
    else:
        await bot.send_message(message.chat.id, ("🐷 " "Ты хохол на " + str(hohol) + "%" " 🐷"))


@dp.message_handler(commands=['пург', 'purge'], commands_prefix=["/", "!"])
async def ping(message: types.Message):
    if message.reply_to_message:
        admt = await message.chat.get_member(message.from_user.id)
        if admt.is_chat_admin():
            bot_msg = await message.answer(f'Начинаю удалять...')
            aboba = []
            aboba.append(message.chat.id)
            a = aboba[0]
            aboba.append(message.reply_to_message.message_id)
            b = aboba[1]
            aboba.append(message.message_id)
            v = aboba[2]
            con = []
            dec = []
            print(1)
            for i in range(b, v + 1):
                print(2)
                try:
                    await bot.delete_message(chat_id=a, message_id=i)
                    con.append(i)
                    print('ok')
                except:
                    print('gey')
                    dec.append(i)
            try:
                await bot_msg.delete()
                await message.answer('Пург закончен')
            except:
                await message.answer('Пург закончеn')
        else:
            await message.reply('Ты не админ!')
    else:
        await message.reply('Эта команда должна быть ответом на какое-либо сообщение!')


'''@dp.message_handler(commands=['likes', 'лайк'], commands_prefix=["/", "!"])
async def likes(message: types.Message):
    buttons = InlineKeyboardMarkup(row_width=1)
    buttons.add(InlineKeyboardButton("❤️ 0", callback_data="like"))
    await message.answer("*Сколько соберём ❤️?*", reply_markup=buttons, parse_mode="Markdown")


@dp.callback_query_handler(lambda c: c.data == "like")
async def like_callback(callback: types.CallbackQuery):
    message = callback.message
    temp = message.reply_markup['inline_keyboard'][0][0]["text"].split("❤️ ")[1]
    buttons = InlineKeyboardMarkup(row_width=1)
    buttons.add(InlineKeyboardButton("❤️ " + str(int(temp) + 1), callback_data="like"))
    await bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text=message.text,
        reply_markup=buttons
    )'''


@dp.message_handler(commands=['edit'])
async def ping(message: types.Message):
    us = sql.select_data(message.from_user.id, "id")[0]
    if us[0] in ADMINS:
        try:
            user = message.text.split()[1]
            user = sql.select_data(user, 'username')[0]
            stolb = message.text.split()[2]
            znach = message.text.split()[3]
            sql.edit_data('id', user[0], stolb, int(znach))
        except:
            ab = InlineKeyboardButton(text='Показать столбцы', callback_data='stolbc')
            a = InlineKeyboardMarkup().add(ab)
            await message.reply('Введите /edit (username) (столбец) (значение int)', reply_markup=a)


@dp.message_handler(Text("Ок", ignore_case=True))
async def kras(msg: types.Message):
    await msg.reply("Хуй ок")


@dp.message_handler(Command("gay", prefixes="!/"))
async def gay(message: types.Message):
    """Хедлер, для обработки комманды /gay или !gay
    В ответ, бот отправляет то, на сколько пользователь является геем
    Примеры:
        /gay
        /gay Vasya
        !gay
        !gay Vasya
    """
    # разбиваем сообщение на комманду и аргументы через регулярное выражение
    command_parse = re.compile(r"(!gay|/gay) ?([\w+ ]+)?")
    parsed = command_parse.match(message.text)
    target = parsed.group(2)
    percentage = randint(0, 100)

    # если пользователь не ввёл цель, он сам становится ею
    if not target:
        target = message.from_user.get_mention()

    # отправляем результат
    await message.reply(f"🏳️‍🌈 Похоже, что {target} гей на {percentage}%")


@dp.callback_query_handler(text="stolbc")
async def send_cmds(call: types.CallbackQuery):
    texts = (
        '<i>Доступные столбцы:</i>\n\n'
        '.cidc. — Айди пользователя (int)\n'
        '.cusernamec. — Ник пользователя (str)\n'
        '.crepac. — Репутация пользователя. (int)\n'
        '.cwarnc. — Варны пользователя. (int)\n'
        '.cbrakc. — Брак с юзером (int)\n'
        '.cregDatec. — Дата регистрации (str)')
    texts = texts.replace('.c', '<code>')
    texts = texts.replace('c.', '</code>')
    await call.message.answer(texts)


@dp.callback_query_handler(text="cmdsbot_callback")
async def send_cmds(call: types.CallbackQuery):
    texts = config.text.replace('<c>', '<code>')
    texts = texts.replace('</c>', '</code>')
    await call.message.delete()
    await call.message.answer(texts)


@dp.callback_query_handler(text_startswith="onbot_")
async def send_cmds(call: types.CallbackQuery):
    chatid = call.data.split('_')[1]
    chatid = int(chatid)
    chatsss = chatsql.select_data(chatid, 'id')[0]
    if chatsss[8] == 1:
        chatsql.edit_data('id', chatid, 'on_off', 0)
        await call.answer(text='Бот был успешно выключен в этом чате', show_alert=True)
    if chatsss[8] == 0:
        chatsql.edit_data('id', chatid, 'on_off', 1)
        await call.answer(text='Бот был успешно включен в этом чате', show_alert=True)


@dp.callback_query_handler(text_startswith="reportsbot_")
async def send_cmds(call: types.CallbackQuery):
    chatid = call.data.split('_')[1]
    chatid = int(chatid)
    chatsss = chatsql.select_data(chatid, 'id')[0]
    if chatsss[13] == 1:
        chatsql.edit_data('id', chatid, 'reports', 0)
        await call.answer(text='Репорты были успешно выключены в этоп чате.', show_alert=True)
    if chatsss[13] == 0:
        chatsql.edit_data('id', chatid, 'reports', 1)
        await call.answer(text='Репорты были успешно включены в этоп чате.', show_alert=True)


@dp.callback_query_handler(text_startswith="arabsbot_")
async def send_cmds(call: types.CallbackQuery):
    chatid = call.data.split('_')[1]
    chatid = int(chatid)
    chatsss = chatsql.select_data(chatid, 'id')[0]
    if chatsss[11] == 1:
        chatsql.edit_data('id', chatid, 'arabs', 0)
        await call.answer(text='Арабы теперь будут кикнуты при входе в чат.', show_alert=True)
    if chatsss[11] == 0:
        chatsql.edit_data('id', chatid, 'arabs', 1)
        await call.answer(text='Арабы теперь НЕ будут кикнуты при входе в чат.', show_alert=True)


@dp.callback_query_handler(text_startswith="actbot_")
async def send_cmds(call: types.CallbackQuery):
    chatid = call.data.split('_')[1]
    chatid = int(chatid)
    chatsss = chatsql.select_data(chatid, 'id')[0]
    if chatsss[4] == 1:
        chatsql.edit_data('id', chatid, 'randomais', 0)
        await call.answer(text='Поддержание онлайна , было успешно выключено в этом чате', show_alert=True)
    if chatsss[4] == 0:
        chatsql.edit_data('id', chatid, 'randomais', 1)
        await call.answer(text='Поддержание онлайна , было успешно включено в этом чате', show_alert=True)


@dp.callback_query_handler(text_startswith="welcbot_")
async def send_cmds(call: types.CallbackQuery):
    chatid = call.data.split('_')[1]
    chatid = int(chatid)
    chatsss = chatsql.select_data(chatid, 'id')[0]
    if chatsss[3] == 1:
        chatsql.edit_data('id', chatid, 'welcomes', 0)
        await call.answer(text='Приветствия , были успешно выключены в этом чате', show_alert=True)
    if chatsss[3] == 0:
        chatsql.edit_data('id', chatid, 'welcomes', 1)
        await call.answer(text='Приветствия были успешно включены в этом чате', show_alert=True)


@dp.callback_query_handler(text_startswith="tixbot_")
async def send_cmds(call: types.CallbackQuery):
    chatid = call.data.split('_')[1]
    chatid = int(chatid)
    chatsss = chatsql.select_data(chatid, 'id')[0]
    if chatsss[10] > 4:
        chatsql.edit_data('id', chatid, 'tixiy', 4)
        await call.answer(text='Тихий режим выключен.', show_alert=True)
    else:
        chatsql.edit_data('id', chatid, 'tixiy', 10)
        await call.answer(text='Тихий режим включен.', show_alert=True)


@dp.callback_query_handler(text_startswith="repabot_")
async def send_cmds(call: types.CallbackQuery):
    chatid = call.data.split('_')[1]
    chatid = int(chatid)
    chatsss = chatsql.select_data(chatid, 'id')[0]
    if chatsss[12] == 1:
        chatsql.edit_data('id', chatid, 'repa', 0)
        await call.answer(text='Репутация была выключена в этом чате.', show_alert=True)
    else:
        chatsql.edit_data('id', chatid, 'repa', 1)
        await call.answer(text='Репутация была включена в этом чате.', show_alert=True)


@dp.callback_query_handler(text_startswith="linksbot_")
async def send_cmds(call: types.CallbackQuery):
    chatid = call.data.split('_')[1]
    chatid = int(chatid)
    chatsss = chatsql.select_data(chatid, 'id')[0]
    if chatsss[14] == 1:
        chatsql.edit_data('id', chatid, 'links', 0)
        await call.answer(text='Анти-Ссылки были выключены в этом чате.', show_alert=True)
    else:
        chatsql.edit_data('id', chatid, 'links', 1)
        await call.answer(text='Анти-Ссылки были включены в этом чате.', show_alert=True)


@dp.callback_query_handler(text_startswith="matsbot_")
async def send_cmds(call: types.CallbackQuery):
    chatid = call.data.split('_')[1]
    chatid = int(chatid)
    chatsss = chatsql.select_data(chatid, 'id')[0]
    if chatsss[5] == 1:
        chatsql.edit_data('id', chatid, 'mats', 0)
        await call.answer(text='Анти-Мат был выключен в этом чате.', show_alert=True)
    else:
        chatsql.edit_data('id', chatid, 'mats', 1)
        await call.answer(text='Анти-Мат был включен в этом чате.', show_alert=True)


# welcome inline
@dp.callback_query_handler(text_startswith="welcomesbot_")
async def send_cmds(call: types.CallbackQuery):
    chatid = call.data.split('_')[1]
    chatid = int(chatid)
    await call.message.delete()
    nazad_btn = InlineKeyboardButton('Назад', callback_data=f'settingsbot_{chatid}')
    delete_btn = InlineKeyboardButton('Удалить приветствие', callback_data=f'delwelcbot_{chatid}')
    update_btn = InlineKeyboardButton('Изменить приветствие', callback_data=f'updwelcbot_{chatid}')
    welcome_kb = InlineKeyboardMarkup(row_width=2).add(update_btn, delete_btn, nazad_btn)
    await call.message.answer('Выберите действие:', reply_markup=welcome_kb)


class WelcomeMsg(StatesGroup):
    waiting_welcome_msg = State()


@dp.callback_query_handler(text_startswith="updwelcbot_")
async def send_updwelc(call: types.CallbackQuery):
    chatid = call.data.split('_')[1]
    chatid = int(chatid)
    await call.message.answer(
        text='Введите текст приветствия\n\nТакже есть тригеры:\n{username} -- Ник пользователя\n{firstname} -- Имя пользователя\n{id} -- Айди пользователя\n{link} -- Ссылка на чат.\n|текст|ссылка| -- Кнопка в приветствии.')
    await WelcomeMsg.waiting_welcome_msg.set()


@dp.message_handler(state=WelcomeMsg.waiting_welcome_msg)
async def welcome_msgl(message: types.Message, state: FSMContext):
    await state.update_data(welcome_msg=message.text)
    user_data = await state.get_data()
    try:
        us = sql.select_data(message.from_user.id, "id")[0]
    except IndexError:
        username = message.from_user.username
        await new_user(message.from_user.id, username)
    us = sql.select_data(message.from_user.id, "id")[0]
    if us[4] == 0:
        await message.answer('Запросите настройки заново в чате.')
        return
    welcome_message = user_data['welcome_msg']
    chatsql.edit_data('id', us[4], 'text', welcome_message)
    settingsbot = InlineKeyboardButton('Назад', callback_data=f'settingsbot_{us[4]}')
    settingsbot_kb = InlineKeyboardMarkup(row_width=1).add(settingsbot)
    await message.reply(f'Текст приветствия успешно изменён на:\n{welcome_message}', reply_markup=settingsbot_kb)
    await state.finish()


@dp.callback_query_handler(text_startswith="delwelcbot_")
async def delwelcome(call: types.CallbackQuery):
    chatid = call.data.split('_')[1]
    chatid = int(chatid)
    chatsss = chatsql.select_data(chatid, 'id')[0]
    chatsql.edit_data('id', chatid, 'text', ' ')
    settingsbot = InlineKeyboardButton('Назад', callback_data=f'settingsbot_{chatid}')
    settingsbot_kb = InlineKeyboardMarkup(row_width=1).add(settingsbot)
    await call.message.answer(text='Текст приветствий очищен.', reply_markup=settingsbot_kb)


@dp.callback_query_handler(text_startswith="delmsg_")
async def delmsg(call: types.CallbackQuery):
    msgid = call.data.split('_')[1]
    msgid = int(msgid)
    chatid = call.data.split('_')[2]
    chatid = int(chatid)
    await call.message.delete()
    try:
        await bot.delete_message(chatid, msgid)
        await call.answer(text='Сообщение удалено.', show_alert=True)
    except:
        await call.answer(text='Другой администратор уже выбрал действие.', show_alert=True)


@dp.callback_query_handler(text_startswith="banuser_")
async def banuser(call: types.CallbackQuery):
    userid = call.data.split('_')[1]
    userid = int(userid)
    chatid = call.data.split('_')[2]
    chatid = int(chatid)
    await call.message.delete()
    ro_end_date = call.message.date + timedelta(days=367)
    try:
        await bot.kick_chat_member(chatid, userid, ro_end_date, True)
        await call.answer(text='Пользователь забанен.', show_alert=True)
    except:
        await call.answer(text='Другой администратор уже выбрал действие.', show_alert=True)


@dp.callback_query_handler(text_startswith="muteuser_")
async def muteuser(call: types.CallbackQuery):
    userid = call.data.split('_')[1]
    userid = int(userid)
    chatid = call.data.split('_')[2]
    chatid = int(chatid)
    ro_end_date = call.message.date + timedelta(days=367)
    await call.message.delete()
    try:
        await bot.restrict_chat_member(
            chat_id=chatid,
            user_id=userid,
            permissions=types.ChatPermissions(),
            until_date=ro_end_date)
        await call.answer(text='Пользователь замьючен.', show_alert=True)
    except:
        await call.answer(text='Другой администратор уже выбрал действие.', show_alert=True)


@dp.callback_query_handler(text_startswith="kickuser_")
async def kickuser(call: types.CallbackQuery):
    userid = call.data.split('_')[1]
    userid = int(userid)
    chatid = call.data.split('_')[2]
    chatid = int(chatid)
    ro_end_date = call.message.date + timedelta(seconds=31)
    await call.message.delete()
    try:
        await bot.kick_chat_member(chatid, userid, ro_end_date, False)
        await call.answer(text='Пользователь кикнут.', show_alert=True)
    except:
        await call.answer(text='Другой администратор уже выбрал действие.', show_alert=True)


@dp.callback_query_handler(text_startswith="rulesbot_")
async def send_cmds(call: types.CallbackQuery):
    chatid = call.data.split('_')[1]
    chatid = int(chatid)
    await call.message.delete()
    nazad_btn = InlineKeyboardButton('Назад', callback_data=f'settingsbot_{chatid}')
    delete_btn = InlineKeyboardButton('Удалить правила', callback_data=f'delrulbot_{chatid}')
    update_btn = InlineKeyboardButton('Изменить правила', callback_data=f'updrulbot_{chatid}')
    rules_kb = InlineKeyboardMarkup(row_width=2).add(update_btn, delete_btn, nazad_btn)
    await call.message.answer('Выберите действие:', reply_markup=rules_kb)


class RulesMsg(StatesGroup):
    waiting_rules_msg = State()


@dp.callback_query_handler(text_startswith="updrulbot_")
async def send_updwelc(call: types.CallbackQuery):
    chatid = call.data.split('_')[1]
    chatid = int(chatid)
    await call.message.answer(text='Введите текст для правил:')
    await RulesMsg.waiting_rules_msg.set()


@dp.message_handler(state=RulesMsg.waiting_rules_msg)
async def welcome_msgl(message: types.Message, state: FSMContext):
    await state.update_data(rules_msg=message.text)
    user_data = await state.get_data()
    try:
        us = sql.select_data(message.from_user.id, "id")[0]
    except IndexError:
        username = message.from_user.username
        await new_user(message.from_user.id, username)
    us = sql.select_data(message.from_user.id, "id")[0]
    if us[4] == 0:
        await message.answer('Запросите настройки заново в чате.')
        return
    rules_message = user_data['rules_msg']
    chatsql.edit_data('id', us[4], 'rules', rules_message)
    settingsbot = InlineKeyboardButton('Назад', callback_data=f'settingsbot_{us[4]}')
    settingsbot_kb = InlineKeyboardMarkup(row_width=1).add(settingsbot)
    await message.reply(f'Текст правил успешно изменён на:\n{rules_message}', reply_markup=settingsbot_kb)
    await state.finish()


@dp.callback_query_handler(text_startswith="brakotkaz_")
async def send_debrak(call: types.CallbackQuery):
    chatid = call.data.split('_')[1]
    chatid = int(chatid)
    us = sql.select_data(call.from_user.id, "id")[0]
    if call.from_user.id == chatid:
        if us[5] == 0:
            await call.message.delete()
            await call.message.answer(f'{call.from_user.first_name} отказал(ась/ся) оt брака')
        else:
            await call.message.delete()
            await call.message.answer(f'{call.from_user.first_name} развел(ась/ся)')
            sql.edit_data('id', us[5], 'brak', 0)
            sql.edit_data('id', us[0], 'brak', 0)
    else:
        await call.answer('Это не для тебя', show_alert=True)


@dp.callback_query_handler(text_startswith="brakprinyat_")
async def send_brak(call: types.CallbackQuery):
    chatid = call.data.split('_')[1]
    chatid = int(chatid)
    id2 = call.data.split('_')[2]
    id2 = int(id2)
    if call.from_user.id == id2:
        us1 = sql.select_data(chatid, 'id')[0]
        us2 = sql.select_data(id2, 'id')[0]
        await call.message.delete()
        sql.edit_data('id', chatid, 'brak', id2)
        sql.edit_data('id', id2, 'brak', chatid)
        ys = hlink(f"{call.from_user.first_name}", f"tg://user?id={id2}")
        await call.message.answer(f'Юхууу! {ys} и @{us1[1]} поженились!')
    else:
        await call.answer('Это не для тебя', show_alert=True)


@dp.callback_query_handler(text_startswith="delrulbot_")
async def delwelcome(call: types.CallbackQuery):
    chatid = call.data.split('_')[1]
    chatid = int(chatid)
    chatsss = chatsql.select_data(chatid, 'id')[0]
    chatsql.edit_data('id', chatid, 'rules', ' ')
    settingsbot = InlineKeyboardButton('Назад', callback_data=f'settingsbot_{chatid}')
    settingsbot_kb = InlineKeyboardMarkup(row_width=1).add(settingsbot)
    await call.message.answer(text='Текст правил очищен.', reply_markup=settingsbot_kb)


@dp.callback_query_handler(text_startswith="settingsbot_")
async def settingsbot(call: types.CallbackQuery):
    chatid = call.data.split('_')[1]
    chatid = int(chatid)
    chatsss = chatsql.select_data(chatid, 'id')[0]
    vkl_btn = InlineKeyboardButton('Включить бота', callback_data=f'onbot_{chatid}')
    act_btn = InlineKeyboardButton('Поддержание актива', callback_data=f'actbot_{chatid}')
    welc_btn = InlineKeyboardButton('Приветствия', callback_data=f'welcbot_{chatid}')
    reon_btn = InlineKeyboardButton('Удаление смс', callback_data=f'reonbot_{chatid}')
    tix_btn = InlineKeyboardButton('Тихий режим', callback_data=f'tixbot_{chatid}')
    repa_btn = InlineKeyboardButton('Репутация', callback_data=f'repabot_{chatid}')
    arabs_btn = InlineKeyboardButton('Арабы', callback_data=f'arabsbot_{chatid}')
    welcomes_btn = InlineKeyboardButton('Текст приветствия', callback_data=f'welcomesbot_{chatid}')
    rules_btn = InlineKeyboardButton('Правила', callback_data=f'rulesbot_{chatid}')
    reports_btn = InlineKeyboardButton('Репорты', callback_data=f'reportsbot_{chatid}')
    links_btn = InlineKeyboardButton('Анти-Ссылки', callback_data=f'linksbot_{chatid}')
    mats_btn = InlineKeyboardButton('Анти-Маты', callback_data=f'matsbot_{chatid}')
    settings_kb = InlineKeyboardMarkup(row_width=2).add(vkl_btn, act_btn, welc_btn, links_btn, mats_btn, reon_btn,
                                                        repa_btn, tix_btn, arabs_btn, welcomes_btn, reports_btn,
                                                        rules_btn)
    await call.message.delete()
    await call.message.answer('Настройки чата:', reply_markup=settings_kb)


@dp.callback_query_handler(text_startswith="reonbot_")
async def send_cmds(call: types.CallbackQuery):
    chatid = call.data.split('_')[1]
    chatid = int(chatid)
    chatsss = chatsql.select_data(chatid, 'id')[0]
    if chatsss[9] == 1:
        chatsql.edit_data('id', chatid, 're_on', 0)
        await call.answer(text='Сообщения написанные пользователями , теперь не будут удаляться в этом чате',
                          show_alert=True)
    if chatsss[9] == 0:
        chatsql.edit_data('id', chatid, 're_on', 1)
        await call.answer(text='Сообщения написанные пользователями , будут удаляться в этом чате', show_alert=True)


@dp.message_handler(Text("Поцеловать", ignore_case=True))
async def f(message: types.Message):
    if not message.reply_to_message:
        await message.reply("😘| ты поцеловал весь чат")
        return

    await message.answer(
        f"""😘|<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> поцеловал(-а)  <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")


@dp.message_handler(Text("Пукнуть", ignore_case=True))
async def f(message: types.Message):
    if not message.reply_to_message:
        await message.reply("💨|Ты пукнул в воздух")
        return

    await message.answer(
        f"""💨|<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> пукнул(-а) в <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")


@dp.message_handler(Text("Отсосать", ignore_case=True))
async def f(message: types.Message):
    if not message.reply_to_message:
        await message.reply("🤯| ты отсосал у всего чата")
        return

    await message.answer(
        f"""🤤|<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> отсосал(-а) у <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")


@dp.message_handler(Text("Тык", ignore_case=True))
async def f(message: types.Message):
    if not message.reply_to_message:
        await message.reply("☝️| ты тыкнул в воздух")
        return

    await message.answer(
        f"""☝️|<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> тыкнул(-а) в <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")


@dp.message_handler(Text("Обнять", ignore_case=True))
async def f(message: types.Message):
    if not message.reply_to_message:
        await message.reply("🤗| ты обнял весь чат")
        return

    await message.answer(
        f"""🤗|<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> обнял(-а) <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")


@dp.message_handler(Text("Трахнуть", ignore_case=True))
async def f(message: types.Message):
    if not message.reply_to_message:
        await message.reply("👌👈| Ты трахнул весь чат")
        return

    await message.answer(
        f"""👌👈|<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> трахнул(-а) <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")


@dp.message_handler(Text("Выебать", ignore_case=True))
async def f(message: types.Message):
    if not message.reply_to_message:
        await message.reply("😬| Ты жестоко выебал весь чат")
        return

    await message.answer(
        f"""😬|<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> жестоко выебал(-а) <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")


@dp.callback_query_handler(text="nazad_callback")
async def main_msg(call: types.CallbackQuery):
    text = ('Привет! Я Smoke Clown!\n'

            # 'Мои команды: /balance , /game , /obmen , /help\n'

            '\n'
            '<b>Клоун бот модератор с искусственным интеллектом и играми! Добавь меня в свой чат и выдай админку!</b>')

    await call.message.edit_text(text)


class Rass(StatesGroup):
    msg = State()


@dp.callback_query_handler(text="rassilka")
async def send_rass(call: types.CallbackQuery):
    if call.from_user.id in ADMINS:
        id = call.from_user.id
        await call.message.answer(text='Введите текст/фото для рассылки:')
        await Rass.msg.set()


'''@dp.message_handler(content_types=ContentType.ANY, state=Rass.msg)
async def rassilka_msgl(message: types.Message, state: FSMContext):
    await state.finish()
    users_query = sql.get_all_data()
    user_ids = [user[0] for user in users_query]
    confirm = []
    decline = []
    bot_msg = await message.answer(f'Рассылка началась...')
    for i in user_ids:
        try:
            await message.copy_to(i)
            confirm.append(i)
        except:
            decline.append(i)
        #		await bot_msg.edit_text(f'Рассылка иде́т...\n\n{len(confirm)} успешно\n{len(decline)} неуспешно')
        await asyncio.sleep(0.3)
    await bot_msg.edit_text(f'Рассылка завершена!\n\nУспешно: {len(confirm)}\nНеуспешно: {len(decline)}')


class Rassc(StatesGroup):
    msgc = State()'''


'''@dp.callback_query_handler(text="rassilkac")
async def send_rassc(call: types.CallbackQuery):
    if call.from_user.id in ADMINS:
        id = call.from_user.id
        await call.message.answer(text='Введите текст/фото для рассылки:')
        await Rassc.msgc.set()
        print('0')'''


'''@dp.message_handler(content_types=ContentType.ANY, state=Rassc.msgc)
async def rassilkac_msgl(message: types.Message, state: FSMContext):
    print('1')
    await state.finish()
    print('2')
    chats_query = chatsql.get_all_data()
    chat_ids = [chat[0] for chat in chats_query]
    confirm = []
    decline = []
    bot_msg = await message.answer(f'Рассылка началась...')
    for i in chat_ids:
        try:
            await message.copy_to(i)
            confirm.append(i)
        except:
            decline.append(i)
        #		await bot_msg.edit_text(f'Рассылка иде́т...\n\n{len(confirm)} успешно\n{len(decline)} неуспешно')
        await asyncio.sleep(3)
    await bot_msg.edit_text(f'Рассылка завершена!\n\nУспешно: {len(confirm)}\nНеуспешно: {len(decline)}')


class CaptchaMsg(StatesGroup):
    waiting_captcha = State()


recaptcha_btn = InlineKeyboardButton(text='Сменить', callback_data='recaptcha')
captcha_kb = InlineKeyboardMarkup().add(recaptcha_btn)'''


@dp.message_handler(content_types=["new_chat_members"])
async def handler_new_member(message: types.Message, state: FSMContext):
    try:
        chats = chatsql.select_data(message.chat.id, "id")[0]
    except IndexError:
        chats = 0
        link = await message.chat.get_url()
        link = str(link)
        await new_chat(message.chat.id, link)
    try:
        us = sql.select_data(message.from_user.id, "id")[0]
    except IndexError:
        us = 0
        username = message.new_chat_members[0].username
        await new_user(message.from_user.id, username)
    welcomes = chatsql.select_data(message.chat.id, "id")[0]
    if int(welcomes[3]) != 0:
        chats = chatsql.select_data(message.chat.id, "id")[0]
        user_name = message.new_chat_members[0].first_name
        if len(chats[2]) > 4:
            link = await message.chat.get_url()
            link = str(link)
            texts = str(chats[2])
            texts = texts.replace('{firstname}', str(message.new_chat_members[0].first_name))
            texts = texts.replace('{username}', f'@{str(message.new_chat_members[0].username)}')
            texts = texts.replace('{id}', str(message.new_chat_members[0].id))
            texts = texts.replace('{link}', str(link))
            if len(texts.split('|')) >= 4:
                msg = texts.split('|')
                button_name = msg[1]
                button_url = msg[2]
                btn = InlineKeyboardButton(text=button_name, url=button_url)
                btns = InlineKeyboardMarkup(row_width=1).add(btn)
            try:
                if chats[11] != 0:
                    aye = detect(str(message.new_chat_members[0].first_name))
                    if aye == 'ur' or aye == 'ar':
                        try:
                            await message.chat.kick(message.new_chat_members[0].id, 999, True)
                        except:
                            await message.reply('У меня нету прав на блок юзеров. А это ебаный араб.')
                else:
                    try:
                        texts = texts.replace('| ', '')
                        texts = texts.replace(' |', '')
                        texts = texts.replace('|', '')
                        texts = texts.replace(button_url, '')
                        texts = texts.replace(button_name, '')
                        await message.answer(texts, reply_markup=btns)
                    except:
                        await message.answer(texts)
            except:
                await message.reply(texts)

        else:
            await message.reply("Добро пожаловать {0}! Я Бот Модератор новый бот:))".format(user_name))



abs = []


'''@dp.message_handler(state=CaptchaMsg.waiting_captcha)
async def fsm_captcha(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    try:
        aboba = int(message.text)
        if len(str(aboba)) > 4:
            print('zzzzzzzzzzzzzzz')
        if message.from_user.id == int(user_data['userid']):
            if message.text == user_data['captcha']:
                await bot.delete_message(message.chat.id, int(user_data['messageid']))
                await message.delete()
                await message.answer('Капча пройдена.')
                await state.finish()
            else:
                if len(abs) >= 3:
                    ro_end_date = message.date + timedelta(minutes=120)
                    await message.chat.kick(
                        user_id=message.from_user.id,
                        until_date=ro_end_date,
                        revoke_messages=True)
                    abs.clear()
                    await message.delete()
                    await message.answer('Пользователь заблокирован за 3 неудачных ввода капчи.')
                else:
                    abs.append(len(abs))
                    await message.delete()
                    await message.answer('Капча неверная. Попробуй еще раз.')
    except:
        if message.from_user.id == int(user_data['userid']):
            await message.delete()'''


'''@dp.callback_query_handler(text="recaptcha", state=CaptchaMsg.waiting_captcha)
async def recaptcha(call: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    if call.from_user.id == user_data['userid']:
        image = ImageCaptcha(fonts=['font/a.ttf'])
        a = str(random.randint(0, 9))
        b = str(random.randint(0, 9))
        v = str(random.randint(0, 9))
        g = str(random.randint(0, 9))
        image.write(a + b + v + g, f'captcha{call.from_user.id}.png')
        bot_msg = await call.message.edit_media(
            types.input_media.InputMediaPhoto(types.InputFile(f'C:/Users/User/PycharmProjects/bot1111112/bot_hendlers/captcha{call.from_user.id}.png')),
            reply_markup=captcha_kb)
        await state.update_data(captcha=a + b + v + g)
        await state.update_data(messageid=bot_msg.message_id)'''


@dp.message_handler(commands=['edit'], commands_prefix=['/', '!', '.'])
async def edit(message: types.Message, state: FSMContext):
	try:
		chats = chatsql.select_data(message.chat.id, "id")[0]
	except IndexError:
		chats = 0
		link = await message.chat.get_url()
		link = str(link)
		await new_chat(message.chat.id, link)
	chatsss = chatsql.select_data(message.chat.id, 'id')[0]
	userid = re.search(r'/edit @\S+', message.text)
	userid = userid.group(0)
	userid = userid.replace('/edit @', '')
	print(userid)
	admt = await message.chat.get_member(message.from_user.id)
	if admt.is_chat_admin():
		tables = message.text.replace(f'/edit @{userid} ', '')
		print(tables)
		if re.search(r'repa', tables):
			tabl = 'repa'
			repas = tables.replace('repa ', '')
			repas = int(repas)
			sql.edit_data('username', userid, f'{tabl}', repas)
			await message.answer(f'Репутация @{userid} успешно изменена на {repas}')
	else:
		await message.delete()

@dp.message_handler(commands=['welcome'], commands_prefix=['/', '!', '.'])
async def welcome(message: types.Message, state: FSMContext):
	try:
		chats = chatsql.select_data(message.chat.id, "id")[0]
	except IndexError:
		chats = 0
		link = await message.chat.get_url()
		link = str(link)
		await new_chat(message.chat.id, link)
	chatsss = chatsql.select_data(message.chat.id, 'id')[0]
	if chatsss[8] != 0:
		admt = await message.chat.get_member(message.from_user.id)
		if admt.is_chat_admin():
			try:
				chats = chatsql.select_data(message.chat.id, "id")[0]
				texts = message.text.replace('/welcome ', '')
				texts = texts.replace("""
									""", '\n')
				chatsql.edit_data('id', int(message.chat.id), 'text', texts)
				await message.answer('Текст приветствия успешно изменён.')
			except:
				await message.answer('Используйте /welcome *текст*')
		else:
			bot_msg = await message.reply('У вас нету доступа.')
			await message.delete()
			await asyncio.sleep(0.5)
			await bot_msg.delete()


@dp.message_handler(content_types=["new_chat_photo"])
async def mats(message: types.Message, state: FSMContext):
    if message.chat.id == -1001230882554 or 0 == 0:
        try:
            chats = chatsql.select_data(message.chat.id, "id")[0]
        except IndexError:
            chats = 0
            link = await message.chat.get_url()
            link = str(link)
            await new_chat(message.chat.id, link)
        chatsss = chatsql.select_data(message.chat.id, 'id')[0]
        if chatsss[8] != 0:
            await message.delete()


'''@dp.message_handler(commands='mats')
async def mats(message: types.Message, state: FSMContext):
	try:
		chats = chatsql.select_data(message.chat.id, "id")[0]
	except IndexError:
		chats = 0
		link = await message.chat.get_url()
		link = str(link)
		await new_chat(message.chat.id, link)
	chatsss = chatsql.select_data(message.chat.id, 'id')[0]
	if chatsss[8] != 0:
		chatsss = chatsql.select_data(message.chat.id, 'id')[0]
		admt = await message.chat.get_member(message.from_user.id)
		if admt.is_chat_admin():
			if int(chatsss[5]) == 0:
				chatsql.edit_data('id', int(message.chat.id), 'mats', 1)
				await message.answer('Анти-Мат включен.')
			elif int(chatsss[5]) == 1:
				chatsql.edit_data('id', int(message.chat.id), 'mats', 0)
				await message.answer('Анти-Мат выключен.')
		else:
			await message.answer('У тебя нету прав.')
			await asyncio.sleep(0.5)
			await message.delete()'''




# @dp.message_handler(content_types=['photo'])
# async def handle_docs_photo(message):
# if message.from_user.id == 1499060992:
# aye = message.photo[-1]
# await bot.send_photo(message.from_user.id, aye.file_id, message.caption)#


@dp.message_handler(content_types=['sticker'])
async def msgstixker(message: types.Message):
    a = message.sticker.file_id
    b = message.sticker.file_unique_id
    if not b in stickall:
        await new_sticker(a, message.sticker.file_unique_id)
        if message.chat.id != message.from_user.id:
            pass
        else:
            return
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
    if chatsss[8] == 1:
        if chatsss[8] != 0 and message.chat.id != message.from_user.id:
            chatsss = chatsql.select_data(message.chat.id, "id")[0]
            chatsql.edit_data('id', message.chat.id, 'sms', chatsss[6] + 1)
    else:
        await message.delete()


@dp.message_handler(Text("Список аниме", ignore_case=True))
async def f(message: types.Message):
    if not message.reply_to_message:
        await message.reply("""Вот что мне известно об "Аниме",
<B>1. Ковбой бибоб
2. Наруто
3. Боруто
4. Блич
5.Сейлор Мун
6  Хвост феи 
7. Джоджо
8. Ван-пис
9. Дневник будущего
10. Тетрадь смерти
11. Бездомный Бог
12. Очень приятно, Бог
13. KonoSuba
14. Bakemonogatari
15. Быть героиней
16. Токийский гуль
17. Красноволосая принцесса Белоснежка
18. Башня бога
19. Да, я Сакомото, а что
20. Волейбол
21. Баскетбол Куроко
22. FREE
23. Юри на льду
24. Бакуган
25. В подземелье я пойду там красавицу найду
26. Врата, там где бьются наши воины
27. Танкистки
28. Твоя апрельская ложь
29. Твоё имя
30. Форма голоса
31. За гранью
32. Монстр за соседней партой
33. Атака титанов
34. Взрыв
35. Паразит
36. Тайные желания отвергнутых
37. Школа тюрьма
38. Школа мертвецов
39. Нет игры - нет жизни
40. Мастер меча онлайн
41. Kill la kill
42. Ангельские ритмы
43. Поцелуй сестричек
44. Монстр в юбке
45. Удар крови
46. Токийские вороны
47. Убийца Акаме
48. Обещанный Неверленд
49. Вельзевул
50. Корона греха
51. Дьявольские возлюбленные
52. Покемоны
53. Overlord
54. Evangelion
55. 91 день
56. Ангел кровопролития 
57. Made in abbys
58. Туалетный мальчик Ханако
59. Kosmoboy
60. Gundam
61. Я хочу съесть твою поджелудочную
62. Идеальный муж и я, или как украсть 55 поцелуев
63. K-on
64. Класс убийц 
65. Президент студсовета моя жена
66. Синий экзорцист
67. Последний Серафим
68. История рам
69. Сатана на подработке
70. Повар-боец Сома
71. Отдай мое тело
72. Ямадо и семь ведьм
73. Требую яоя
74. Волчица и пряности
75. 7 смертных грехов
76. Mob psyxo 100
77. Психопаспорт
78. Иная
79. Эроманга сенсей
80. Литераторы и алхимики 
81. Врата Штейна
82. Стальной алхимик
83. Гурен-лаган
84. Ванпанчмен
85. Парад смерти
86. Безумный азарт
87. Город в котором меня нет
88. Жизнь в альтернативном мире с нуля
89. Шарлотта
90. Король шаманов
91. Гинтама
92. Пожиратель душ
93. Великий из бродячих псов
94. Две звезды Онимёджи
95. Чёрная пуля
96. Чёрный клевер
97. Убийца гоблинов
98. Крутой учитель Онидзука
99. Виолетта Эвердгарден
100. Дракон-горничная Такибаяши
101. Серавмп
102. Клинок рассекающий демонов
103. Боку но Пико
104. Волчица и черный принц
105. Сайт волшебниц
106. Легенда о Гранкресте
107. Восхождение героя щита
108. Не скрывая крик
109. Пластиковые воспоминания
110. Абсолютный дует 
111. Хост клуб Оранской школы
112. Трогательный комплекс
113. В лес, где мерцают светлячки
114. Грабитель
115. Кизнайвер
116. Госпожа Кагуя, в любви как на войне
117. Притворная любовь
118. Волчьи дети Амэ и Юки
119. Линия дьявола
120. Унесённые призраками
121. Я, пёс и секретная служба
122. Эльфийская песня
123. Милый во Франксе 
124. Темный дворецкий
125. Бригада пожарных
126. Садисткая смесь
127. Моя геройская академия 
128. Танец мечей
129. Связанные миры
130. Месть Масамунэ куна
131. Дурочка
132. ОхотникХОхотник
134. Любовь и ложь
135. Загадка дьявола
136. Кабанери из стальной крепости
137. Дорога юности
138. Вторжение
139. Мир в котором не существует самой концепции похабных шуток
140. Вокалоиды.
141. Агент паранойи
142. Драматическое убийство
143. Дитя погоды
144. Богатый детектив
145. Необъятный океан
146. Котоура сан
147. Эхо тепрора
148. Класс убийц</b>""")


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
    if re.search(r'http\S+', message.text) or re.search(r't.me\S+', message.text) or re.search(r'@\S+',
                                                                                               message.text) or re.search(
            r'//\S+', message.text):
        if chatsss[14] == 1:
            admt = await message.chat.get_member(message.from_user.id)
            if admt.is_chat_admin():
                return
            await message.delete()
    if message.text == '!settings' or message.text == '/settings' or message.text == '/settings@king_admin_bot':
        admt = await message.chat.get_member(message.from_user.id)
        if admt.is_chat_admin():
            await message.reply('Окей, я отправил тебе настройки в лс!')
            link_foronbot = await message.chat.get_url()
            vkl_btn = InlineKeyboardButton('Включить бота', callback_data=f'onbot_{message.chat.id}')
            act_btn = InlineKeyboardButton('Поддержание актива', callback_data=f'actbot_{message.chat.id}')
            welc_btn = InlineKeyboardButton('Приветствия', callback_data=f'welcbot_{message.chat.id}')
            reon_btn = InlineKeyboardButton('Удаление смс', callback_data=f'reonbot_{message.chat.id}')
            tix_btn = InlineKeyboardButton('Тихий режим', callback_data=f'tixbot_{message.chat.id}')
            arabs_btn = InlineKeyboardButton('Арабы', callback_data=f'arabsbot_{message.chat.id}')
            repa_btn = InlineKeyboardButton('Репутация', callback_data=f'repabot_{message.chat.id}')
            rules_btn = InlineKeyboardButton('Правила', callback_data=f'rulesbot_{message.chat.id}')
            welcomes_btn = InlineKeyboardButton('Приветствие', callback_data=f'welcomesbot_{message.chat.id}')
            reports_btn = InlineKeyboardButton('Репорты', callback_data=f'reportsbot_{message.chat.id}')
            links_btn = InlineKeyboardButton('Анти-Ссылки', callback_data=f'linksbot_{message.chat.id}')
            mats_btn = InlineKeyboardButton('Анти-Маты', callback_data=f'matsbot_{message.chat.id}')
            settings_kb = InlineKeyboardMarkup(row_width=2).add(vkl_btn, act_btn, welc_btn, links_btn, mats_btn,
                                                                reon_btn, repa_btn, tix_btn, arabs_btn, welcomes_btn,
                                                                reports_btn, rules_btn)
            texts = data.settings_text.format(str(link_foronbot))
            sql.edit_data('id', message.from_user.id, 'admchat', message.chat.id)
            await bot.send_message(message.from_user.id, texts, reply_markup=settings_kb, disable_web_page_preview=True)
    if chatsss[8] == 1:
        if chatsss[8] != 0 and message.chat.id != message.from_user.id:

            chatsss = chatsql.select_data(message.chat.id, "id")[0]
            chatsql.edit_data('id', message.chat.id, 'sms', chatsss[6] + 1)

            if message.text == 'Bot' or message.text == 'Бот' or message.text == '@king_admin_bot':
                textsa = hlink('Бот Модератор', 'https://t.me/king_admin_bot')

                await message.reply(f'Привет , я {textsa}! Мои команды:\n\n  — напиши /help')

            if re.search(r'@king_of_this_world_1 \S+', message.text) or re.search(r'king_of_this_world_1 \S+', message.text):
                if chatsss[4] != 0:
                    texts = message.text.replace('Бот ', '')

                    texts = texts.replace('Bot ', '')

                    if re.search(r'или', texts):

                        if re.search(r'вилкой в', texts):

                            abob = ['тебе вилкой в жопу хуйлуша блять', 'хуём в глаз.\nтебе']

                            aboba = random.choice(abob)

                            await message.reply(aboba)

                        else:

                            perv = re.search(r'\S+', texts)

                            perv1 = re.search(r' \S+', texts)

                            perv = perv.group(0)

                            vtor = texts

                            vtor = vtor.replace('или ', '')

                            vtor = vtor.replace(perv, '')

                            vtor = vtor.replace('?', '')

                            perv = perv.replace('?', '')

                            rn = [perv, vtor]

                            otvetka = random.choice(rn)

                            await message.reply(otvetka)

                    if re.search(r'стикер', texts):
                        srik = [i[0] for i in stickall]
                        stick = random.choice(srik)
                        await message.reply_sticker(stick)
                        return

                    if re.search(r'кто', texts) or re.search(r'Кто', texts):
                        kto = texts.replace('кто ', '')
                        kto = kto.replace('Кто', '')
                        kto = kto.replace('?', '')
                        users_query = sql.get_all_data()
                        user_ids = [user[0] for user in users_query]
                        user_id = random.choice(user_ids)
                        while (await message.chat.get_member(user_id)).status == 'left':
                            user_id = random.choice(user_ids)
                        else:
                            user = await bot.get_chat(user_id)
                            await message.answer(f'{hlink("Он", f"tg://user?id={user_id}")} {kto}',
                                                 disable_web_page_preview=True)
                    '''if texts == 'Обо мне' or texts == 'обо мне':
                        if 0 == 0:
                            userid = message.from_user.id
                            us = sql.select_data(message.from_user.id, "id")[0]
                            repa = us[2]
                            admt = await message.chat.get_member(message.from_user.id)
                            if 0 is 0:
                                texts = 'Твой ник: @{0}\n\nТвоя карма: {1} ✝\n\nТвои варны: {2}\nТы админ!'.format(
                                    message.from_user.username, repa, us[3])
                                await message.reply(texts)
                            else:
                                texts = 'Твой ник: @{0}\n\nТвоя карма: {1} <3\n\nТвои варны: {2}\nТы не админ!'.format(
                                    message.from_user.username, repa, us[3])
                                await message.reply(texts)'''

                    if re.search(r'скажи', texts):
                        textl = texts.replace('скажи ', '')

                        textl = textl.replace('скажи', '')

                        textl = textl.replace('Скажи', '')

                        await message.answer(textl)

                    if re.search(r'продолжи \S+', texts):
                        a = texts.replace('продолжи ', '')
                        if re.search(r'улитка', a):
                            generated_text = ' но бармен заявляет: "У нас строгая политика в отношении улиток!" — и ногой выпихивает ее на улицу. Через неделю улитка возвращается в бар и говорит бармену: "Ну и нахуя ты это сделал!?"'
                        await message.reply(generated_text)

                    else:

                        if re.search(r'Bot \S+', message.text):

                            ashajajabajnajsa = 0

                        else:

                            chance = random.randint(0, int(chatsss[10]))

                            if chance == 1:

                                chan = ['otvets', 'slovall', 'jopa', 'a', 'b']

                                otvets = ['Привет, я Бот Модератор!', 'Сперма на вкус как яичный белок', 'Жопа в говне',
                                          '.notexec aboba', 'Я курю травку']

                                chance = random.choice(chan)

                                if chance == 'otvets':

                                    otvet = random.choice(otvets)

                                    await message.reply(otvet)

                                else:

                                    otvet = random.choice(slovall)

                                    if otvet != "('1',)":
                                        await message.reply(otvet)

            if message.text == '!rules' or message.text == '/rules':
                rules = chatsss[7]
                await message.reply(rules, disable_web_page_preview=True)
            # reports
            '''if message.text == '/report' or message.text == '!report':
                admt = await message.chat.get_member(message.reply_to_message.from_user.id)
                if message.reply_to_message and chatsss[13] == 1:
                    if not admt.is_chat_admin():
                        await message.reply(
                            f'Вы пожаловались на сообщение пользователя @{message.reply_to_message.from_user.username}')
                        adminschat = await bot.get_chat_administrators(message.chat.id)
                        adminss = []
                        for i in adminschat:
                            if i.user.is_bot:
                                pass
                            else:
                                try:
                                    bot_msg = await bot.send_message(i.user.id, 'test')
                                    msgid = bot_msg.message_id
                                    await bot.delete_message(i.user.id, msgid)
                                    adminss.append(i.user.id)
                                except:
                                    pass
                        deletemsg_btn = InlineKeyboardButton('Удалить сообщение',
                                                             callback_data=f'delmsg_{message.reply_to_message.message_id}_{message.chat.id}')
                        blockuser_btn = InlineKeyboardButton('Забанить нарушителя',
                                                             callback_data=f'banuser_{message.reply_to_message.from_user.id}_{message.chat.id}')
                        muteuser_btn = InlineKeyboardButton('Замьютить нарушителя',
                                                            callback_data=f'muteuser_{message.reply_to_message.from_user.id}_{message.chat.id}')
                        kickuser_btn = InlineKeyboardButton('Кикнуть нарушителя',
                                                            callback_data=f'kickuser_{message.reply_to_message.from_user.id}_{message.chat.id}')
                        report_kb = InlineKeyboardMarkup(row_width=2).add(deletemsg_btn, blockuser_btn, muteuser_btn,
                                                                          kickuser_btn)
                        link = await message.chat.get_url()
                        for i in range(len(adminss)):
                            i = adminss[i]
                            if i == 0:
                                i = adminss[0]
                                await bot.send_message(i,
                                                       f'<code>Чат: </code>{link}<code>\nПользователь:</code> @{message.from_user.username}\n<code>Нарушитель:</code> @{message.reply_to_message.from_user.username}\n<code>Текст сообщения:</code> {message.reply_to_message.text}\n<code>Ссылка на сообщение: </code>{link}/{message.reply_to_message.message_id}\n\nВыберите действие:',
                                                       reply_markup=report_kb, disable_web_page_preview=True)
                            else:
                                await bot.send_message(i,
                                                       f'<code>Чат: </code>{link}<code>\nПользователь:</code> @{message.from_user.username}\n<code>Нарушитель:</code> @{message.reply_to_message.from_user.username}\n<code>Текст сообщения:</code> {message.reply_to_message.text}\n<code>Ссылка на сообщение: </code>{link}/{message.reply_to_message.message_id}\n\nВыберите действие:',
                                                       reply_markup=report_kb, disable_web_page_preview=True)
                    else:
                        await message.reply('Это админ, какой нахуй репорт?')'''

            '''if message.text == '!me' or message.text == '/me' or message.text == 'кто я' or message.text == 'Кто я':
                userid = message.from_user.id
                us = sql.select_data(message.from_user.id, "id")[0]
                repa = us[2]
                if 0 is 0:
                    texts = 'Твой ник: @{0}\n\nТвоя карма: {1} ✝\n\nТвои варны: {2}'.format(message.from_user.username,
                                                                                            repa, us[3])
                    await message.reply(texts)
                else:
                    texts = 'Твой ник: @{0}\n\nТвоя карма: {1} <3\n\nТвои варны: {2}\nТы не админ!'.format(
                        message.from_user.username, repa, us[3])
                    await message.reply(texts)'''

            if message.text.startswith('развод') or message.text.startswith('Развод'):
                partner = sql.select_data(us[5], "id")[0]
                if us[5] != 0:
                    if partner[5] == message.from_user.id:
                        print(1)
                        otkazat = InlineKeyboardButton(text='Развестись 💔', callback_data=f'brakotkaz_{partner[0]}')
                        brak = InlineKeyboardMarkup(row_width=2).add(otkazat)
                        await message.reply(
                            f'{hlink(message.from_user.first_name, f"tg://user?id={us[0]}")} предложил развестись {hlink(partner[1], f"tg://user?id={partner[0]}")}',
                            reply_markup=brak)
                    else:
                        await message.reply('Ты не в браке!')
                else:
                    await message.reply('Ты не в браке!')


            '''if message.text == 'да':
                await message.reply('пизда')
            if message.text == 'da':
                await message.reply('pizda')
            if message.text == '/del' or message.text == '!del':
                admt = await message.chat.get_member(message.from_user.id)
                if admt.is_chat_admin():
                    await bot.delete_message(message.chat.id, message.reply_to_message.message_id)
                    await message.delete()'''
            '''if message.text == '!pin' or message.text == '!закрепить' or message.text == '/pin':

                if message.reply_to_message:

                    try:

                        admt = await message.chat.get_member(message.from_user.id)

                        if admt.is_chat_admin():

                            await message.chat.pin_message(message.reply_to_message.message_id, False)

                            await message.reply('Сообщение закреплено')

                        else:

                            await message.reply('У вас нету доступа.')

                            await message.delete()

                    except:

                        await message.reply('У меня нету прав(')

                else:

                    await message.reply('Это надо писать в ответ на сообщение.')'''

            '''if message.text == '!unpin' or message.text == '!открепить' or message.text == '/unpin':

                if message.reply_to_message:

                    try:

                        admt = await message.chat.get_member(message.from_user.id)

                        if admt.is_chat_admin():

                            await message.chat.unpin_message(message.reply_to_message.message_id)

                            await message.reply('Сообщение откреплено')

                        else:

                            await message.reply('У вас нету доступа.')

                            await message.delete()

                    except:

                        await message.reply('У меня нету прав(')

                else:

                    await message.reply('Это надо писать в ответ на сообщение.')'''

            if re.search(r'!photos', message.text):
                admt = await message.chat.get_member(message.from_user.id)

                jopa = message.text.replace('!photos ', '')

                prop = await bot.get_chat_member(message.chat.id, 1916288033)

                if prop.can_manage_chat == True or prop.can_delete_messages == True:
                    if prop.can_manage_chat == True and prop.can_delete_messages == True:

                        if admt.is_chat_admin():

                            try:

                                rang = int(jopa)

                            except ValueError:
                                await message.reply(
                                    'Вы ввели не верное кол-во аватарок, используйте:\n\n !photos *число*')
                            chat_info = await bot.get_chat(message.chat.id)
                            stok = chat_info.photo.big_file_id
                            try:
                                await bot.photo(stok).download(f'C:/Users/User/PycharmProjects/pythonProject8/img/{message.chat.id}.png')
                            except:
                                stok = f'C:/Users/User/PycharmProjects/pythonProject8/img/{message.chat.id}.png'
                            rang = int(jopa)

                            try:
                                await message.chat.set_photo(
                                    types.InputFile(f'C:/Users/User/PycharmProjects/pythonProject8/img/photo{rang}.png'))
                            except:
                                await message.reply_voice(types.InputFile('C:/Users/User/PycharmProjects/pythonProject8/voice/1.mp3'))
                                return
                            bot_msg = await message.reply('Цикл начат, сейчас 1-ая ава')
                            # await bot_msg.edit_text('Столько аватарок у меня нету..')
                            for i in range(1, rang + 1):
                                await message.chat.set_photo(types.InputFile(f'C:/Users/User/PycharmProjects/pythonProject8/img/photo{i}.png'))
                                await bot_msg.edit_text(f'Сейчас {i}-ая ава.')
                                await asyncio.sleep(10)
                            await bot_msg.edit_text('Цикл завершен.')
                            await message.chat.set_photo(types.InputFile(stok))

                    if prop.can_manage_chat == True and prop.can_delete_messages == False:
                        await message.answer('У меня нету прав на: \n\n — удаление сообщений')

                    if prop.can_manage_chat == False and prop.can_delete_messages == True:
                        await message.answer('У меня нету прав на: \n\n — изменение профиля группы')

                else:

                    await message.answer('У меня нету прав на: \n\n — изменение профиля группы\n — удаление сообщений')
            if chatsss[12] == 1:
                if message.text == '+' or message.text == '👍' or message.text == '++' or message.text == '+++':
                    us = sql.select_data(message.reply_to_message.from_user.id, "id")[0]
                    if message.reply_to_message.from_user.id != message.from_user.id:
                        userid = message.from_user.id
                        if userid in af:
                            if datetime.datetime.now().second - af[userid].second <= 59:
                                await message.reply(f'Вы слишком часто меняете репутацию. Можно раз в минуту')
                            else:
                                af[userid] = datetime.datetime.now()
                                await repafun(message.reply_to_message.from_user.id)
                                utext = hlink('пользователю',
                                              f'https://t.me/{message.reply_to_message.from_user.username}')
                                await message.reply(
                                    f'Вы повысили репутацию {utext} на +1\n\nЕго репутация: {us[2] + 1}❤️',
                                    disable_web_page_preview=True)
                        else:
                            af[userid] = datetime.datetime.now()
                            await repafun(message.reply_to_message.from_user.id)
                            utext = hlink('пользователю', f'https://t.me/{message.reply_to_message.from_user.username}')
                            await message.reply(f'Вы повысили репутацию {utext} на +1\n\nЕго репутация: {us[2] + 1}❤️',
                                                disable_web_page_preview=True)
                    else:
                        await message.reply(
                            f'Ляя <b>{message.from_user.first_name}</b>, я тоже себя люблю. Но к сожалению самому себе репу поднять нельзя(')

                if message.text == '-' or message.text == '👎':
                    us = sql.select_data(message.reply_to_message.from_user.id, "id")[0]
                    if message.reply_to_message.from_user.id != message.from_user.id:
                        userid = message.from_user.id
                        if userid in af:
                            if datetime.datetime.now().second - af[userid].second <= 59:
                                await message.reply(f'Вы слишком часто меняете репутацию. Можно раз в минуту')
                            else:
                                af[userid] = datetime.datetime.now()
                                await unrepafun(message.reply_to_message.from_user.id)
                                utext = hlink('пользователю',
                                              f'https://t.me/{message.reply_to_message.from_user.username}')
                                await message.reply(
                                    f'Вы понизили репутацию {utext} на -1\n\nЕго репутация: {us[2] - 1}❤️',
                                    disable_web_page_preview=True)
                        else:
                            af[userid] = datetime.datetime.now()
                            await unrepafun(message.reply_to_message.from_user.id)
                            utext = hlink('пользователю', f'https://t.me/{message.reply_to_message.from_user.username}')
                            await message.reply(f'Вы понизили репутацию {utext} на -1\n\nЕго репутация: {us[2] - 1}❤️',
                                                disable_web_page_preview=True)
                    else:
                        await message.reply('Пчел ты.. так нельзя')

            if re.search(r'/warn', message.text) or re.search(r'!warn', message.text):
                if message.reply_to_message:
                    admt = await message.chat.get_member(message.from_user.id)
                    if not admt.is_chat_admin():
                        return
                    try:
                        utext = hlink('Пользователь', f'https://t.me/{message.reply_to_message.from_user.username}')
                        us = sql.select_data(int(message.reply_to_message.from_user.id), 'id')[0]
                        warns = us[3]
                        admt = await message.chat.get_member(message.reply_to_message.from_user.id)
                        if warns >= 2 and not admt.is_chat_admin():
                            sql.edit_data('id', message.reply_to_message.from_user.id, 'warn', 0)
                            await message.chat.kick(
                                user_id=message.reply_to_message.from_user.id,
                                revoke_messages=True,
                                until_date=ro_end_date)
                            await message.reply(
                                f'{utext} получил варн от @{message.from_user.username} и был забанен за 3 варна.')
                        if warns >= 0 and warns < 3 and warns != 2 and not admt.is_chat_admin():
                            sql.edit_data('id', message.reply_to_message.from_user.id, 'warn', warns + 1)
                            warns = us[3]
                            await message.reply(
                                f'{utext} получил варн от @{message.from_user.username}. Его варны: {warns + 1}')

                    except:

                        await message.reply('Ошибка.')
                else:
                    admt = await message.chat.get_member(message.from_user.id)

                    if not admt.is_chat_admin():
                        return
                    userid = message.text.replace('!warn @', '')
                    userid = userid.replace('/warn @', '')
                    us = sql.select_data(userid, "username")[0]
                    us = us[0]

                    try:

                        utext = hlink('Пользователь', f'https://t.me/{userid}')

                        us = sql.select_data(int(us), 'id')[0]
                        warns = us[3]
                        admt = await message.chat.get_member(us[0])
                        if warns >= 2 and not admt.is_chat_admin():
                            sql.edit_data('id', us[0], 'warn', 0)
                            await message.chat.kick(
                                user_id=us[0],
                                until_date=ro_end_date,
                                revoke_messages=True)
                            await message.reply(
                                f'{utext} получил варн от @{message.from_user.username} и был забанен за 3 варна.')
                        if warns >= 1 and warns < 3 and warns != 2 and not admt.is_chat_admin():
                            sql.edit_data('id', us, 'warn', warns + 1)
                            warns = us[3]
                            await message.reply(
                                f'{utext} получил варн от @{message.from_user.username}. Его варны: {warns + 1}')

                    except:

                        await message.reply('Ошибка.')

            if re.search(r'/unwarn', message.text) or re.search(r'!unwarn', message.text):
                if message.reply_to_message:
                    admt = await message.chat.get_member(message.from_user.id)

                    if not admt.is_chat_admin():
                        return

                    try:
                        utext = hlink('Пользователь', f'https://t.me/{message.reply_to_message.from_user.username}')
                        sql.edit_data('id', message.reply_to_message.from_user.id, 'warn', 0)
                        await message.reply(f'{utext} был освобожден от варнов, админом @{message.from_user.username}')
                    except:
                        await message.reply('Ошибка.')
                else:
                    admt = await message.chat.get_member(message.from_user.id)
                    if not admt.is_chat_admin():
                        return
                    userid = message.text.replace('!unwarn @', '')
                    userid = userid.replace('/unwarn @', '')
                    try:
                        utext = hlink('Пользователь', f'https://t.me/{userid}')
                        sql.edit_data('username', userid, 'warn', 0)
                        await message.reply(f'{utext} был освобожден от варнов, админом @{message.from_user.username}')
                    except:
                        await message.reply('Ошибка.')

            if re.search(r'!promote \S+', message.text) or re.search(r'/promote \S+', message.text):
                if message.reply_to_message:

                    admt = await message.chat.get_member(message.from_user.id)

                    if admt.is_chat_admin():
                        if admt.can_promote_members == True or message.from_user.username == 'CM0KE':

                            try:
                                pref = message.text.replace('!promote ', '')

                                pref = pref.replace('/promote ', '')

                                await message.chat.promote(message.reply_to_message.from_user.id, False, False, False,
                                                           False, False, True, False, False, False)

                                await message.chat.set_administrator_custom_title(message.reply_to_message.from_user.id,
                                                                                  pref)

                                await message.reply(
                                    f'Пользователь @{message.reply_to_message.from_user.username} повышен, префикс: {pref}.')

                            except:
                                await asyncio.sleep(0.5)
                        else:
                            await message.reply('У тебя нету прав на назначение администраторов:)')

                    else:

                        await message.reply('Ты не администратор:)')

                        await asyncio.sleep(0.5)

                        await message.delete()
                else:
                    await message.reply('Это надо писать в ответ на сообщение.')

            if re.search(r'!demote', message.text) or re.search(r'/demote', message.text):
                if message.reply_to_message:

                    admt = await message.chat.get_member(message.from_user.id)

                    if admt.is_chat_admin():
                        if admt.can_promote_members == True or message.from_user.username == 'CM0KE':
                            try:

                                await message.chat.promote(message.reply_to_message.from_user.id, False, False, False,
                                                           False, False, False, False, False, False)

                                await message.reply(
                                    f'Пользователь @{message.reply_to_message.from_user.username} снят с админки')

                            except:

                                await message.reply('У меня нету прав на добавление администраторов.')

                                await asyncio.sleep(0.5)

                                await message.delete()
                        else:
                            await message.reply('У тебя нету прав на назначение администраторов')

                    else:

                        await message.reply('Ты не администратор.')

                        await asyncio.sleep(0.5)

                        await message.delete()
                else:
                    userid = message.text.replace('/demote @', '')
                    userid = userid.replace('!demote @', '')
                    us = sql.select_data(userid, "username")[0]
                    us = us[0]
                    admt = await message.chat.get_member(message.from_user.id)
                    if admt.is_chat_admin():
                        if admt.can_promote_members == True or message.from_user.username == 'CM0KE':
                            try:
                                await message.chat.promote(int(us), False, False, False, False, False, False, False,
                                                           False, False)
                                await message.reply(f'@{userid} понижен в правах')
                            except:
                                await asyncio.sleep(0.5)
                                await message.delete()
                        else:
                            await message.reply('У тебя нету прав на назначение администраторов:)')
                    else:

                        await message.reply('Ты не администратор.')
                        await asyncio.sleep(0.5)

            '''if re.search(r'!mute', message.text) or re.search(r'/mute', message.text):
                if re.search(r'!mute', message.text) or re.search(r'/mute', message.text):
                    readonly_to = await message.chat.get_member(message.reply_to_message.from_user.id)

                    if readonly_to.is_chat_admin():
                        await message.reply(localization.get_string("error_restrict_admin"))

                        return

                    adma = await message.chat.get_member(message.from_user.id)

                    if not adma.is_chat_admin():
                        return
                    ro_period = message.text.replace('!mute ', '')

                    ro_period = ro_period.replace('/mute ', '')

                    if re.search(r'm', ro_period):
                        ro_period = ro_period.replace('m', '')

                        ro_period = int(ro_period)
                        ro_end_date = message.date + timedelta(minutes=ro_period)
                        await message.chat.restrict(

                            user_id=message.reply_to_message.from_user.id,

                            permissions=types.ChatPermissions(),

                            until_date=ro_end_date)

                        ulink = hlink('Пользователь', f'https://t.me/{message.reply_to_message.from_user.username}')

                        await message.reply(f'{ulink} замьючен до {ro_end_date}', disable_web_page_preview=True)
                        await message.delete(message.reply_to_message.id)
                    if re.search(r's', ro_period):
                        ro_period = ro_period.replace('s', '')

                        ro_period = int(ro_period)
                        ro_end_date = message.date + timedelta(second=ro_period)
                        await message.chat.restrict(

                            user_id=message.reply_to_message.from_user.id,

                            permissions=types.ChatPermissions(),

                            until_date=ro_end_date)

                        ulink = hlink('Пользователь', f'https://t.me/{message.reply_to_message.from_user.username}')

                        await message.reply(f'{ulink} замьючен до {ro_end_date}', disable_web_page_preview=True)
                        await message.delete(message.reply_to_message.id)
                    if re.search(r'h', ro_period):
                        ro_period = ro_period.replace('h', '')

                        ro_period = int(ro_period)
                        ro_end_date = message.date + timedelta(hours=ro_period)
                        await message.chat.restrict(

                            user_id=message.reply_to_message.from_user.id,

                            permissions=types.ChatPermissions(),

                            until_date=ro_end_date)

                        ulink = hlink('Пользователь', f'https://t.me/{message.reply_to_message.from_user.username}')

                        await message.reply(f'{ulink} замьючен до {ro_end_date}', disable_web_page_preview=True)
                        await message.delete(message.reply_to_message.id)
                    if re.search(r'd', ro_period):
                        ro_period = ro_period.replace('d', '')

                        ro_period = int(ro_period)
                        ro_end_date = message.date + timedelta(days=ro_period)
                        await message.chat.restrict(

                            user_id=message.reply_to_message.from_user.id,

                            permissions=types.ChatPermissions(),

                            until_date=ro_end_date)

                        ulink = hlink('Пользователь', f'https://t.me/{message.reply_to_message.from_user.username}')

                        await message.reply(f'{ulink} замьючен до {ro_end_date}', disable_web_page_preview=True)
                        await bot.delete_message(message.chat.id, message.reply_to_message.message_id)
                    else:
                        await message.answer(
                            'Неверный формат, введите: \n\n !mute *число*значение\nЗначения:\nd — дней\nh — часов\nm — минут\ns — секунд')

            if re.search(r'!unmute', message.text) or re.search(r'/unmute', message.text):
                if re.search(r'!unmute', message.text) or re.search(r'/unmute', message.text):
                    adma = await message.chat.get_member(message.from_user.id)
                    testmute = await message.chat.get_member(message.reply_to_message.from_user.id)
                    if testmute.can_send_messages:
                        await message.reply('Чел не в муте.')
                        return
                    if adma.is_chat_admin():
                        ro_end_date = message.date + timedelta(days=377)
                        await message.chat.restrict(

                            user_id=message.reply_to_message.from_user.id,

                            permissions=types.ChatPermissions(can_send_messages=True, can_send_media_messages=True,
                                                              can_send_other_messages=True,
                                                              can_add_web_page_previews=True),

                            until_date=ro_end_date)

                        ulink = hlink('Пользователь', f'https://t.me/{message.reply_to_message.from_user.username}')

                        await message.reply(f'{ulink} размьючен', disable_web_page_preview=True)'''

            if re.search(r'Тебе жаба', message.text) or message.text == 'Взять жабу' or message.text == 'взять жабу':
                otvets = ['Иди нахуй со своими жабами , заебал уже', 'Боже... жабы.... заебали они уже.',
                          'Удали нахуй , не бери эту жабу']
                randotvet = random.choice(otvets)
                await message.reply(randotvet)

            if int(chatsss[4]) != 0:

                if message.text not in slovall:

                    if re.search(r'Smoke', message.text) or re.search(r'smoke', message.text) or re.search(r'/',
                                                                                                           message.text):

                        print(' ')

                    else:

                        msg = message.text.replace("""

											   	""", '\n')

                        await new_slovo(msg)

                        chana = random.choice(['s', 'm'])
                        if chana == 'm':

                            slovo = random.choice(slovall)

                            slovo = str(slovo)

                            slovo = slovo.replace("""

												""", '\n')

                            zuzu = slovo

                            if zuzu[0] != '(' and len(zuzu) != 1:

                                chance = random.randint(0, int(chatsss[10]))
                                if chance == 1:

                                    otvet = zuzu

                                    if otvet != "('1',)":
                                        await message.reply(zuzu)
                        else:
                            stickalls = [i[0] for i in stickall]
                            stick = random.choice(stickalls)
                            chance = random.randint(0, int(chatsss[10]))
                            if chance == 1:
                                await message.reply_sticker(stick)



                elif message.text in slovall:

                    if re.search(r'Smoke', message.text) or re.search(r'smoke', message.text) or re.search(r'/',
                                                                                                           message.text):

                        print(' ')

                    else:
                        chan = random.choice(['s', 'm'])
                        if chan == 'm':

                            slovo = random.choice(slovall)

                            slovo = str(slovo)

                            slovo = slovo.replace("""

												""", '\n')

                            msg = slovo

                            if msg[0] != '(' and len(msg) != 1:

                                chance = random.randint(0, int(chatsss[10]))

                                if chance == 1:

                                    otvet = msg

                                    if otvet != "('1',)":
                                        await message.reply(msg)
                        else:
                            stickalls = [i[0] for i in stickall]
                            stick = random.choice(stickalls)
                            chance = random.randint(0, int(chatsss[10]))
                            if chance == 1:
                                await message.reply_sticker(stick)

            if re.search(r'Люблю \S+', message.text) or re.search(r'люблю \S+', message.text):

                msg = message.text.replace('Люблю ', '')

                msg = msg.replace('люблю ', '')

                chance = random.randint(0, int(chatsss[10]))

                if re.search(r'ок', msg):

                    msg = msg.replace('ок', 'ки')

                    msg = msg.replace('ей', 'и')

                    await message.reply(f'{msg} для пидоров')

                else:

                    await message.reply(f'{msg} для пидоров')
    else:
        await message.delete()

    if re.search(r'Хочу \S+', message.text) or re.search(r'хочу\S+', message.text):

        msg = message.text.replace('Хочу ', '')

        msg = msg.replace('хочу ', '')

        chance = random.randint(0, int(chatsss[10]))

        if re.search(r'ок', msg):

            msg = msg.replace('ок', 'ки')

            msg = msg.replace('ей', 'и')

            await message.reply(f'{msg} для пидоров')

        else:

            await message.reply(f'{msg} для пидоров')

            if re.search(r'Стата', texts) or re.search(r'статистика', texts):

                members = await message.chat.get_members_count()

                adms = list_of_user

                chats = len(chatsqlall)

                adms = len(adms)

                a = chatsql.get_all_data()
                s = 0
                aboba = [chat[0] for chat in a]
                chatses = []
                for i in aboba:
                    try:
                        b = await bot.get_chat_members_count(i)
                        if not i in chatses:
                            s += b
                            chatses.append(i)
                    except:
                        pass

                await message.reply(
                    f'В чате {members} пользователей.\nСообщений написано: {chatsss[6]}\n\n<code>Пользователей в боте:\n{str(adms)}</code>\nБота пригласили в <code>{chats}</code> чатов\nОбщее количество участников в чатах: <code>{s}</code>')


if __name__ == '__main__':
    executor.start_polling(dp)