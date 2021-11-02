from aiogram import Dispatcher
from aiogram.types import ContentTypes

from wtrmarkbot.handlers.swatermark.swatermark import from_callback, process
from wtrmarkbot.states.swatermark import SWatermarkState


def setup(dp: Dispatcher):
    dp.register_callback_query_handler(
        from_callback,
        lambda c: c.data and c.data.startswith('watermark_from_settings')
    )

    dp.register_message_handler(
        process,
        state=SWatermarkState.sget_pic,
        content_types=ContentTypes.PHOTO
    )
