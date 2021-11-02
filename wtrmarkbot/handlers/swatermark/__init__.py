from aiogram import Dispatcher
from aiogram.types import ContentTypes

from wtrmarkbot.handlers.swatermark.swatermark import process_image, process_document


def setup(dp: Dispatcher):
    dp.register_message_handler(process_image, content_types=ContentTypes.PHOTO)
    dp.register_message_handler(process_document, content_types=ContentTypes.DOCUMENT)
