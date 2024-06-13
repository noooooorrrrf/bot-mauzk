import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from config import BANNED_USERS
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest


@app.on_message(filters.regex("^/start"), group=39)
async def cpanel(_, message: Message):             
        text = "**🧑🏻‍✈️︙اهلا بك بك عزيزي العضو ♥️**\n\n**⤵️︙ اليـكـ كيب الاعضاء الخاص بسورس سي جي**"
        kep = ReplyKeyboardMarkup([
["مطور البوت", "مبرمج السورس"],
["السورس","اصدار"],
["اقتباس","استوري"],
["انمي","متحركه"],
["تويت", "صراحه"],
["نكته","احكام"],
[" لو خيروك","انصحني"],
["قران","نقشبندي"],
["اذكار","كتابات"],
["حروف","بوت"],
["غنيلي","سوال"],
["تلاوات","عبدالباسط"],
["افاتار بنات","افاتار شباب"],
["❎ ¦ حذف الكيبورد"]], resize_keyboard=True)
        await message.reply(
              text=text,
               reply_markup=kep,quote=True)

@app.on_message(filters.command(["❎ ¦ حذف الكيبورد"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الكيبورد بنجاح""",
        reply_markup=ReplyKeyboardRemove()
    )

@app.on_message(filters.command("⛔ ¦ المحظورين") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/89840a4c57675832debf9.jpg",
        caption=f"""• اليك طريقه معرفه المحظورين .\n\n• قم بـ استخدام الامر هكذا : /blockedusers المحظورين ميوزك\n\n• 𝗦𝗼𝗨𝗿𝗖𝗲 𝗖𝗷 » @CG_G11 .\n•⊶⊶★─⊶『[𝗖𝗷](https://t.me/CG_G11)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝗦𝗼𝗨𝗿𝗖𝗲 𝗖𝗷 .", url=f"https://t.me/CG_G11"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🍁 ¦ حظر") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5dc0bab3462bd868b3081.jpg",
        caption=f"""• اليك طريقه حظر اي شخص .\n\n• قم بـ استخدام الامر هكذا : /block حظر ميوزك\n\n• 𝗦𝗼𝗨𝗿𝗖𝗲 𝗖𝗷 » @CG_G11 .\n•⊶⊶★─⊶『[𝗖𝗷](https://t.me/CG_G11)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝗦𝗼𝗨𝗿𝗖𝗲 𝗖𝗷 .", url=f"https://t.me/CG_G11"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🖇 ¦ الغاء حظر") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4268ef332d710c5547357.jpg",
        caption=f"""• اليك طريقه الغاء حظر شخص .\n\n• قم بـ استخدام الامر هكذا : /unblock الغاء حظر ميوزك\n\n• 𝗦𝗼𝗨𝗿𝗖𝗲 𝗖𝗷 » @CG_G11 .\n•⊶⊶★─⊶『[𝗖𝗷](https://t.me/CG_G11)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝗦𝗼𝗨𝗿𝗖𝗲 𝗖𝗷 .", url=f"https://t.me/CG_G11"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🔥 ¦ المحظورين عام") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/cc2b0b6c4eea77c43b8b4.jpg",
        caption=f"""• اليك طريقه معرفه المحظورين عام .\n\n• قم بـ استخدام الامر هكذا : /blockedusers المحظورين ميوزك\n\n• 𝗦𝗼𝗨𝗿𝗖𝗲 𝗖𝗷 » @CG_G11 .\n•⊶⊶★─⊶『[𝗖𝗷](https://t.me/CG_G11)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝗦𝗼𝗨𝗿𝗖𝗲 𝗖𝗷 .", url=f"https://t.me/CG_G11"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🗞 ¦ حظر عام") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d0db8351713f77bb8450b.jpg",
        caption=f"""• اليك طريقه الحظر العام .\n\n• قم بـ استخدام الامر هكذا :/ح ع\n\n• 𝗦𝗼𝗨𝗿𝗖𝗲 𝗖𝗷 » @CG_G11 .\n•⊶⊶★─⊶『[𝗖𝗷](https://t.me/CG_G11)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝗦𝗼𝗨𝗿𝗖𝗲 𝗖𝗷 .", url=f"https://t.me/CG_G11"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🔖 ¦ الغاء العام") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/611ee77edc1763ea2b07b.jpg",
        caption=f"""• اليك طريقه الغاء الحظر العام .\n\n• قم بـ استخدام الامر هكذا : /unblock الغاء حظر ميوزك\n\n• 𝗦𝗼𝗨𝗿𝗖𝗲 𝗖𝗷 » @CG_G11 .\n•⊶⊶★─⊶『[𝗖𝗷](https://t.me/CG_G11)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝗦𝗼𝗨𝗿𝗖𝗲 𝗖𝗷 .", url=f"https://t.me/CG_G11"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🪂 ¦ الاحصائيات") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/571e1fb1857c8ae6e6be1.jpg",
        caption=f"""• اليك طريقه معرفه الاحصائيات .\n\n• قم بـ استخدام الامر هكذا : الاحصائيات\n\n• 𝗦𝗼𝗨𝗿𝗖𝗲 𝗖𝗷 » @CG_G11 .\n•⊶⊶★─⊶『[𝗖𝗷](https://t.me/CG_G11)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝗦𝗼𝗨𝗿𝗖𝗲 𝗖𝗷 .", url=f"https://t.me/CG_G11"),
            ],
            ]
        ),
    )

@app.on_message(filters.command(["ذكاء الاصطناعي"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c544b771eeed7dbdc51a9.jpg",
        caption=f"""• اليك طريقه معرفه سرعه البوت .\n\n• قم بـ استخدام الامر هكذا : /gpt\n\n• 𝗦𝗼𝗨𝗿𝗖𝗲 𝗖𝗷 » @CG_G11 .\n•⊶⊶★─⊶『[𝗖𝗷](https://t.me/CG_G11)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝗦𝗼𝗨𝗿𝗖𝗲 𝗖𝗷 .", url=f"https://t.me/CG_G11"),
            ],
            ]
        ),
    )