# Developed By : Abhishek Kumar (https://telegram.me/TheTeleRoid) 

import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import *


Bot = Client(
    "Donate",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


START_TEXT = """Hey! {}
☞ Very Happy to Know that You are Donating Us.

Thanks For Using [Our Bots](https://t.me/+KYLCdC4XfcdmNGVl).

Made with love For [You](tg://settings)"""

DONATE_BUTTON = [
    InlineKeyboardButton(text='Donate 💸', callback_data='donateme'
    )
]


@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup([DONATE_BUTTON]),
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_message(filters.private & filters.command(["donate"]))
async def filter(bot, update):
    await update.reply_text(
        text="Click the Below Button to Donate Us",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="UPI", callback_data="upidata"),
                [InlineKeyboardButton(text="PayPal", url=https://paypal.me/AbhishekKumarIN47)]
            ],
            [
                [InlineKeyboardButton(text="😥 Close", callback_data="closedata")]
        ),
        disable_web_page_preview=True,
        quote=True
    )


Bot.run()
