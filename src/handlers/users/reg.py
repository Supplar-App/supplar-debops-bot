from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from src.keyboards.default import keyboards_login
from loader import dp


@dp.message_handler(Command("reg"))
async def bot_register_user(message: types.Message):
    await message.answer(f"Будет зарегистрирован новый пользователь - {message.from_user.full_name}!",
                         reply_markup=keyboards_login)
    # здесь нужно сделать инлайн кнопки
    await message.answer(f"Хотите использовать имя - `{message.from_user.full_name}` ?", parse_mode="Markdown")


@dp.message_handler(text="SIGN IN")
async def sign_in(message: types.Message):
    await message.answer(f"Введите имя пользователя, чтобы войти")


@dp.message_handler(text="SIGN UP")
async def sign_in(message: types.Message):
    await message.answer(f"Введите имя пользователя, чтобы зарегистрироваться")


@dp.message_handler(text="Info")
async def sign_in(message: types.Message):
    await message.answer(f"Существующий пользователь нажмите 'SIGN IN'\n"
                         f"Создать нового пользователя нажмите 'SIGN UP'")


