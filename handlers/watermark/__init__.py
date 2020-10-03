from aiogram import Dispatcher
from states.watermark import SetWatermark
from aiogram.types import ContentTypes

from .watermark import (
    starting_from_command,
    starting_from_callback,
    get_picture,
    get_position,
    get_color,
    get_opacity,
    get_font,
    get_fontsize,
    set_text
)


def setup(dp: Dispatcher):

    # Комманды
    dp.register_message_handler(
        starting_from_command, commands=['watermark']
    )

    # Калбеки
    dp.register_callback_query_handler(
        starting_from_callback,
        lambda c: c.data and c.data.startswith('watermark_default')
    )

    # Состояния для создания без настроек
    dp.register_message_handler(
        get_picture,
        state=SetWatermark.get_pic,
        content_types=ContentTypes.PHOTO
    )
    dp.register_message_handler(
        get_position.handle,
        state=SetWatermark.set_position,
        content_types=ContentTypes.TEXT
    )
    dp.register_message_handler(
        get_color.handle,
        state=SetWatermark.set_textcolor,
        content_types=ContentTypes.TEXT
    )
    dp.register_message_handler(
        get_opacity.handle,
        state=SetWatermark.set_opacity,
        content_types=ContentTypes.TEXT
    )
    dp.register_message_handler(
        get_font.handle,
        state=SetWatermark.set_font,
        content_types=ContentTypes.TEXT
    )
    dp.register_message_handler(
        get_fontsize.handle,
        state=SetWatermark.set_fontsize,
        content_types=ContentTypes.TEXT
    )
    dp.register_message_handler(
        set_text,
        state=SetWatermark.set_text,
        content_types=ContentTypes.TEXT
    )
