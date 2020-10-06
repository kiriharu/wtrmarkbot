from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from loguru import logger
from tortoise import Tortoise
from middlewares.userdata import UserMiddleware
import config
import handlers


storage = MemoryStorage()
telegram_bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(telegram_bot, storage=storage)


def on_startup():
    logger.info("Register handlers...")
    # Register you handlers here.
    handlers.default.setup(dp)
    handlers.settings.setup(dp)
    handlers.watermark.setup(dp)
    handlers.swatermark.setup(dp)
    dp.middleware.setup(UserMiddleware())


async def database_init():
    if config.MYSQL_HOST is not None:
        db_url = f"mysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@" \
                 f"{config.MYSQL_HOST}:{config.MYSQL_PORT}/{config.MYSQL_DATABASE}"
    else:
        db_url = "sqlite://db.sqlite3"
    await Tortoise.init(
        db_url=db_url,
        modules={
            'model': ['models.user']
        }
    )
    await Tortoise.generate_schemas()
    logger.info("Tortoise inited!")

# TODO: Мидлварь для логированния и сбора статистики (а че крашнулось чтобы понимать)


if __name__ == "__main__":
    on_startup()
    dp.loop.create_task(database_init())
    executor.start_polling(dp, skip_updates=True)
