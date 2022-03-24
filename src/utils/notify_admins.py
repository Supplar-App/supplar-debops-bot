import logging

from aiogram import Dispatcher, types

from src.data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    # chat_id = dp.bot.get_chat()

    # здесь нужно получить как то chat_id
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, text="Бот Запущен++")

        except Exception as err:
            logging.exception(err)

