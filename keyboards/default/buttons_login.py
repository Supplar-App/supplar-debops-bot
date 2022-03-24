from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboards_login = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="SIGN UP"),
            KeyboardButton(text="SIGN IN")
        ],
        [
            KeyboardButton(text="Info")
        ],
    ],
    resize_keyboard=True
)
