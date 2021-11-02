from typing import Union

from PIL import UnidentifiedImageError
from aiogram.types import Message, PhotoSize, Document
from loguru import logger

from wtrmarkbot.middlewares.userdata import userdata_required
from wtrmarkbot.models.user import User
from wtrmarkbot.consts import TEXT_COLORS
from wtrmarkbot.utlis.image_converter import watermark_process


async def process(msg: Message, data: Union[PhotoSize, Document], user: User):
    try:
        await watermark_process(
            msg, data, user.position, TEXT_COLORS[user.color], user.opacity,
            user.font, user.fontsize, user.text, user.result_type
        )
    except UnidentifiedImageError:
        await msg.answer(
            "🤖 Документ поврежден или не является картинкой."
        )


@userdata_required
async def process_image(msg: Message, user: User):
    logger.info("Process image to add watermark...")
    await process(msg, msg.photo[-1], user)


@userdata_required
async def process_document(msg: Message, user: User):
    logger.info("Process document to add watermark...")
    await process(msg, msg.document, user)
