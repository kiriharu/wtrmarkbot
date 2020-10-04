from aiogram import Dispatcher
from .settings import settings_from_callback, settings_from_command

from .settings import (
    configure_position, configure_color, configure_opacity,
    configure_font, configure_fontsize, configure_text
)


def setup(dp: Dispatcher):

    dp.register_message_handler(
        settings_from_command, commands=['settings']
    )

    dp.register_callback_query_handler(
        settings_from_callback,
        lambda c: c.data and c.data.startswith('settings_menu')
    )

    configure_position.register(dp)
    configure_color.register(dp)
    configure_opacity.register(dp)
    configure_font.register(dp)
    configure_fontsize.register(dp)
    configure_text.register(dp)
