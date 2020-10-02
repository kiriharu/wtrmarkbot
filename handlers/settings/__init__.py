from aiogram import Dispatcher
from .settings import settings_from_callback, settings_from_command


def setup(dp: Dispatcher):

    dp.register_message_handler(
        settings_from_command, commands=['settings']
    )

    dp.register_callback_query_handler(
        settings_from_callback,
        lambda c: c.data and c.data.startswith('settings_menu')
    )