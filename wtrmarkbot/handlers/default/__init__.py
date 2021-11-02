from aiogram import Dispatcher
from .default import (
    start_from_command,
    start_from_callback,
)


def setup(dp: Dispatcher):

    # Команды
    dp.register_message_handler(
        start_from_command, commands=['start']
    )
    dp.register_callback_query_handler(
        start_from_callback,
        lambda c: c.data and c.data.startswith('main_menu')
    )
