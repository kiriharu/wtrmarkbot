from aiogram import Dispatcher

from wtrmarkbot.handlers.settings.settings import (
    configure_position,
    configure_color,
    configure_opacity,
    configure_font,
    configure_fontsize,
    configure_text,
    configure_result_type,
    settings_from_callback,
)


def setup(dp: Dispatcher):
    dp.register_callback_query_handler(
        settings_from_callback, lambda c: c.data and c.data.startswith("settings_menu")
    )

    configure_position.register(dp)
    configure_color.register(dp)
    configure_opacity.register(dp)
    configure_font.register(dp)
    configure_fontsize.register(dp)
    configure_text.register(dp)
    configure_result_type.register(dp)
