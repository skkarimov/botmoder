from time import time
from aiogram import types
from aiogram.dispatcher.filters import Text
from configurator import config
from dispatcher import dp, bot
import localization
import utils
from random import randint

@dp.message_handler(chat_id=config.groups.main, commands="report", commands_prefix="/!")
async def cmd_report(message: types.Message):
    # Check if command is sent as reply to some message
    if not message.reply_to_message:
        await message.reply(localization.get_string("error_no_reply"))
        return

    # Check if command is sent to own message
    if message.reply_to_message.from_user.id == message.from_user.id:
        await message.reply(localization.get_string("error_report_self"))
        return

    # Check if command is sent as reply to admin
    user = await message.bot.get_chat_member(config.groups.main, message.reply_to_message.from_user.id)
    if user.is_chat_admin() and user.can_restrict_members:
        await message.reply(localization.get_string("error_report_admin"))
        return

    # Cannot report group posts
    if message.reply_to_message.from_user.id == 777000:
        await message.bot.delete_message(config.groups.main, message.message_id)
        return

    # Check for report message (anything sent after /report or !report command)
    msg_parts = message.text.split()
    report_message = None
    if len(msg_parts) > 1:
        report_message = message.text.replace("!report", "")
        report_message = report_message.replace("/report", "")

    # Generate keyboard with some actions
    action_keyboard = types.InlineKeyboardMarkup()
    # Delete message by its id
    action_keyboard.add(types.InlineKeyboardButton(
        text=localization.get_string("action_del_msg"),
        callback_data=f"del_{message.reply_to_message.message_id}")
    )

    # Delete message by its id and ban user by their id
    action_keyboard.add(types.InlineKeyboardButton(
        text=localization.get_string("action_del_and_ban"),
        callback_data=f"delban_{message.reply_to_message.message_id}_{message.reply_to_message.from_user.id}"
    ))

    # Delete message by its id and mute user for 24 hours by their id
    action_keyboard.add(types.InlineKeyboardButton(
        text=localization.get_string("action_del_and_readonly"),
        callback_data=f"mute_{message.reply_to_message.message_id}_{message.reply_to_message.from_user.id}"
    ))

    # Delete message by its id and mute user for 7 days by their id
    action_keyboard.add(types.InlineKeyboardButton(
        text=localization.get_string("action_del_and_readonly2"),
        callback_data=f"mute2_{message.reply_to_message.message_id}_{message.reply_to_message.from_user.id}"
    ))

    # Do nothing, false alarm
    action_keyboard.add(types.InlineKeyboardButton(
        text=localization.get_string("action_false_alarm"),
        callback_data=f"dismiss_{message.reply_to_message.message_id}_{message.reply_to_message.from_user.id}"
    ))

    # Do nothing, false alarm + mute reporter for one day
    action_keyboard.add(types.InlineKeyboardButton(
        text=localization.get_string("action_false_alarm_2"),
        callback_data=f"dismiss2_{message.message_id}_{message.from_user.id}"
    ))

    # Do nothing, false alarm + mute reporter for one week
    action_keyboard.add(types.InlineKeyboardButton(
        text=localization.get_string("action_false_alarm_3"),
        callback_data=f"dismiss3_{message.message_id}_{message.from_user.id}"
    ))

    # Do nothing, false alarm + ban reporter
    action_keyboard.add(types.InlineKeyboardButton(
        text=localization.get_string("action_false_alarm_4"),
        callback_data=f"dismiss4_{message.message_id}_{message.from_user.id}"
    ))

    await message.reply_to_message.forward(config.groups.reports)
    await message.bot.send_message(
        config.groups.reports,
        utils.get_report_comment(
            message.reply_to_message.date,
            message.reply_to_message.message_id,
            report_message
        ),
        reply_markup=action_keyboard)
    await message.reply(localization.get_string("report_delivered"))


@dp.message_handler(chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP], chat_id=config.groups.main, commands=['help'], commands_prefix=['!', '/', '.'])
async def help(message: types.Message):
        await message.reply(localization.get_string("all_commands"))


@dp.message_handler(chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP], chat_id=config.groups.main, commands=['me'], commands_prefix=['!', '/', '.'])
async def welcome(message: types.Message):
    if message.from_user.username is None:
        await message.reply(f"Name - {message.from_user.full_name}\nID - {message.from_user.id}\n")
    else:
        await message.reply(f"Name - {message.from_user.full_name}\n"
                            f"ID - <code>{message.from_user.id}</code>\n"
                            f"Username - @{message.from_user.username}\n"
                            )


@dp.message_handler(chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP], chat_id=config.groups.main, commands=['admins', 'admin', 'adm'],
                    commands_prefix=['!/', '@', '.'])
async def get_admin_list(message: types.Message):
    admins_id = [(admin.user.id, admin.user.full_name) for admin in await bot.get_chat_administrators(
        chat_id=message.chat.id)]
    admins_list = []
    for ids, name in admins_id:
        admins_list.append("".join(f"[{name}](tg://user?id={ids})"))
    result_list = ""
    for admins in admins_list:
        result_list += "".join(admins) + '\n'
    await message.reply("Админы :\n" + result_list, parse_mode=types.ParseMode.MARKDOWN)
