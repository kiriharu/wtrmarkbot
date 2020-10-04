from aiogram import Dispatcher
from .swatermark import from_command, from_callback, process
from states.swatermark import SWatermarkState
from aiogram.types import ContentTypes


def setup(dp: Dispatcher):
    dp.register_message_handler(
        from_command, commands=['swatermark']
    )

    dp.register_callback_query_handler(
        from_callback,
        lambda c: c.data and c.data.startswith('watermark_from_settings')
    )

    dp.register_message_handler(
        process,
        state=SWatermarkState.sget_pic,
        content_types=ContentTypes.PHOTO
    )