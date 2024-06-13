import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app

import re
import sys
from os import getenv

from dotenv import load_dotenv



@app.on_message(filters.command(["اصدار"], ""))
async def bkouqw(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fba6a5152ca49bce2f2b1.jpg",
        caption=f"""**⋖━━❲𖣂❳━━●○𝗖𝗷○●━━❲𖣂❳━━⋗**\nمرحبا بك عزيزي {message.from_user.mention}\n
♡♕᚜ اسم سورس:-سي جي
♡♕᚜ نوعه:-ميوزك
♡♕᚜ للغه برمجه:- بايثون
♡♕᚜ اللغه:-اللغه العربيه ويدعم الانجليزيه 
♡♕᚜ مجال تشغيل :- تشغيل بوتات الميوزك
♡♕᚜ نظام تشغيل:-سي جي بوت ميوزك
♡♕᚜ الاصدار 4.0.1 pyrogram 
♡♕᚜ تاريخ تاسيس:-10-4-2020

**⋖━━❲𖣂❳━━●○𝗖𝗷○●━━❲𖣂❳━━⋗**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "●━◉⟞⟦ ѕᴏụʀᴄᴇ 𝗖𝗷 ⟧⟝◉━●", url=f"https://t.me/CG_G11"), 
               ],
          ]
        ),
    )


