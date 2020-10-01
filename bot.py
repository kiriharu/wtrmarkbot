from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from loguru import logger
from asyncio import Queue

import config
import handlers

picture_queue = Queue()
storage = MemoryStorage()
telegram_bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(telegram_bot, storage=storage)


def on_startup():
    logger.info("Register handlers...")
    # Register you handlers here.
    handlers.default.setup(dp)

# TODO: Добавить сохранение настроек и генерирование картинок с настроек
# TODO: Мидлварь для логированния и сбора статистики (а че крашнулось чтобы понимать)
# TODO: Заработать милливон вечнозеленых на этом боте, стать известным, а потом проснуться


if __name__ == "__main__":
    on_startup()
    executor.start_polling(dp, skip_updates=True)
