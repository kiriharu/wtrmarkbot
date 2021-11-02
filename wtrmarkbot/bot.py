from asyncio import sleep

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from loguru import logger
from tortoise import Tortoise
from tortoise.exceptions import DBConnectionError

from wtrmarkbot.config import (
    TELEGRAM_BOT_TOKEN,
    MYSQL_HOST,
    MYSQL_USER,
    MYSQL_PASSWORD,
    MYSQL_PORT,
    MYSQL_DATABASE
)
from wtrmarkbot.middlewares import UserMiddleware
from wtrmarkbot import handlers

storage = MemoryStorage()
telegram_bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(telegram_bot, storage=storage)


async def database_init():
    if MYSQL_HOST is not None:
        db_url = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@" \
                 f"{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
    else:
        db_url = "sqlite://db.sqlite3"
    try:
        await Tortoise.init(
            db_url=db_url,
            modules={
                'models': ['wtrmarkbot.models']
            }
        )
    except DBConnectionError:
        logger.error("Connection to database failed.")
        await sleep(10)
        await database_init()
    await Tortoise.generate_schemas()
    logger.info("Tortoise inited!")


async def on_startup(disp: Dispatcher):
    await database_init()
    logger.info("Register handlers...")
    # Register you handlers here.
    handlers.default.setup(disp)
    handlers.settings.setup(disp)
    handlers.swatermark.setup(disp)
    dp.middleware.setup(UserMiddleware())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)