from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="boshlash", callback_data="start")],
        [InlineKeyboardButton(text="yordam", callback_data="help")],
    ]
)
