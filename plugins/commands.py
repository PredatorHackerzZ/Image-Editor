# By @TroJanzHEX
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters
from script import script  # pylint:disable=import-error
from database.forcesub import ForceSub
from database.access_db import db
from database.add_user import AddUserToDatabase

@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client: Client, message: Message):
    await AddUserToDatabase(bot, update)
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    try:
        await message.reply_text(
            text=script.START_MSG.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🌀 Channel ", url="https://t.me/TeleRoidGroup"),
                        InlineKeyboardButton("🔆 Support ", url="https://t.me/TeleRoid14"),
                    ],
                    [
                        InlineKeyboardButton("🚸 Help ", callback_data="help_data"),
                        InlineKeyboardButton("🔔 About ", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton("💠 BotList ", url="https://t.me/joinchat/t1ko_FOJxhFiOThl"),
                        InlineKeyboardButton("👥 GitHub ", url="https://github.com/PredatorHackerzZ/Image-Editor"),
                    ],
                    [
                        InlineKeyboardButton(
                            "🔐 Close",
                            callback_data="close_e",
                        )
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass


@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    await AddUserToDatabase(bot, update)
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    try:
        await message.reply_text(
            text=script.HELP_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙 BACK", callback_data="start_data"),
                        InlineKeyboardButton("🔔 ABOUT", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "🈴 SOURCE CODE",
                            url="https://telegram.dog/Moviesflixers_DL",
                        )
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass


@Client.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    await AddUserToDatabase(bot, update)
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    try:
        await message.reply_text(
            text=script.ABOUT_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙 BACK", callback_data="help_data"),
                        InlineKeyboardButton("🏠 Home", callback_data="start_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "SOURCE CODE",
                            url="https://telegram.dog/Moviesflixers_DL",
                        )
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass
