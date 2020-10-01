from aiogram import Dispatcher
from states.state import SetWatermark
from aiogram.types import ContentTypes

from .process import starting, get_picture, get_position, get_color, set_opacity, set_font


def setup(dp: Dispatcher):
    dp.register_message_handler(starting, commands=['start'])
    dp.register_message_handler(
        get_picture,
        state=SetWatermark.get_pic,
        content_types=ContentTypes.PHOTO
    )
    dp.register_message_handler(
        get_position,
        state=SetWatermark.set_position,
        content_types=ContentTypes.TEXT
    )
    dp.register_message_handler(
        get_color,
        state=SetWatermark.set_textcolor,
        content_types=ContentTypes.TEXT
    )
    dp.register_message_handler(
        set_opacity,
        state=SetWatermark.set_opacity,
        content_types=ContentTypes.TEXT
    )
    dp.register_message_handler(
        set_font,
        state=SetWatermark.set_font,
        content_types=ContentTypes.TEXT
    )
