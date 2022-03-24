from aiogram import executor

from loader import dp
from src import middlewares, filters, handlers # Если будут middlewares, filters, то соблюдать порядок middlewares, filters, handlers

from src.utils.notify_admins import on_startup_notify
from src.utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)


    # Уведомляет про запуск
    # await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)