import asyncio
import logging
import sys
from datetime import datetime

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message

import btn

TOKEN = "8600455704:AAFwyd1AijMWpbDQiZNs7D33tffOspjYSXA"


dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=btn.inline
    )


@dp.callback_query()
async def get_call_data(call: CallbackQuery) -> None:
    await call.answer()
    data = call.data
    if data == "start":
        await call.message.answer("Siz boshlash tugmasini bosdingiz!")
    elif data == "help":
        await call.message.answer("Siz yordam tugmasini bosdingiz!")


@dp.message()
async def get_message(message: Message) -> None:
    matn = message.text
    if matn == "salom":
        await message.answer("Salom, Qalaysiz?")
    elif matn == "qandaysan?":
        await message.answer("Yaxshi, Rahmat!")
    elif matn == "rahmat":
        await message.answer("Sizga yordam bera olganimdan xursandman!")
    elif matn == "xayr":
        await message.answer("Xayr, Yana ko'rishguncha!")
    elif matn == "yordam":
        await message.answer("Sizga qanday yordam bera olaman?")

    elif matn == "ism":
        await message.answer("Men Botman, Sizga yordam berish uchun yaratildim!")
    elif matn == "vaqt":
        await message.answer("Hozirgi vaqt: " + datetime.now().strftime("%H:%M:%S"))
    elif matn == "sana":
        await message.answer("Bugungi sana: " + datetime.now().strftime("%Y-%m-%d"))
    elif matn == "hazil":
        await message.answer(
            "Nega kompyuterlar yaxshi hazil qilishmaydi? Chunki ularning ko'pchiliklari 'byte' qiladi!"
        )
    elif matn == "python":
        await message.answer(
            "Python - bu yuqori darajadagi, umumiy maqsadli dasturlash tili. U o'qilishi oson va ko'p qirrali, veb-ishlab chiqish, ma'lumotlarni tahlil qilish, sun'iy intellekt va boshqalar uchun ishlatiladi."
        )
    elif matn == "Aiogram":
        await message.answer(
            "Aiogram - bu Python dasturlash tilida Telegram botlarini yaratish uchun mo'ljallangan kutubxona. U asinxron dasturlashni qo'llab-quvvatlaydi va Telegram Bot API bilan oson integratsiyani ta'minlaydi."
        )
    elif matn == "Telegram":
        await message.answer(
            "Telegram - bu tezkor xabar almashish va ovozli qo'ng'iroqlarni qo'llab-quvvatlaydigan bulutga asoslangan xabar almashish platformasi. U foydalanuvchilarga matn, rasm, video va boshqa fayllarni yuborish imkonini beradi."
        )
    elif matn == "Kim yaratgan?":
        await message.answer(
            "Menni yaratuvchisi - [Sizning Ismingiz], dasturchi va texnologiya ishqibozi."
        )
    elif matn == "Nima qilasan?":
        await message.answer(
            "Men Telegram foydalanuvchilariga turli xil savollarga javob berish, yordam taklif qilish va oddiy suhbat qurish uchun mo'ljallangan botman."
        )
    elif matn == "Dasturchi":
        await message.answer(
            "Dasturchi - bu kompyuter dasturlarini yaratish, sinovdan o'tkazish va saqlash bilan shug'ullanuvchi shaxs. Dasturchilar turli dasturlash tillaridan foydalanib, veb-saytlar, mobil ilovalar, o'yinlar va boshqa dasturlarni ishlab chiqadilar."
        )


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
