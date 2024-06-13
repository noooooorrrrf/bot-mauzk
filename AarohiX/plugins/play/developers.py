import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
from random import  choice, randint

#          
                
@app.on_message(
    filters.command(["المبرمج","اعدام","مبرمج السورس","المطور"], "")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fba6a5152ca49bce2f2b1.jpg",
        caption=f"""**⩹━★⊷━⌞ 𝗦𝗼𝗨𝗿𝗖𝗲 𝗖𝗷 ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم المبرمج\nللتحدث مع السورس السورس اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ 𝗦𝗼𝗨𝗿𝗖𝗲 𝗖𝗷 ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᯓ 𓆩 ˹ -𓆩⏤͟͞𝐄3𝐃𝐀𝐌˼⍣⃝🇪🇬𓆪𓆃", url=f"https://t.me/DAD_E3DAM"), 
                 ],[
                   InlineKeyboardButton(
                        "★⌞ 𝗦𝗼𝗨𝗿𝗖𝗲 𝗖𝗷 ⌝⚡", url=f"https://t.me/CG_G11"),
                ],

            ]

        ),

    )
