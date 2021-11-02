from io import BytesIO
from typing import Union, Optional

from PIL import UnidentifiedImageError
from aiogram.types import Message, PhotoSize, Document
from loguru import logger

from wtrmarkbot.messages import routes_messages
from wtrmarkbot.middlewares.userdata import userdata_required
from wtrmarkbot.models.user import User, ResultType
from wtrmarkbot.consts import TEXT_COLORS
from wtrmarkbot.utlis.image_converter import add_watermark


async def process(msg: Message, data: Union[PhotoSize, Document], user: User):
    try:
        picture = BytesIO()
        await data.download(destination_file=picture)
        watermarked = await add_watermark(
            picture,
            user.position,
            TEXT_COLORS[user.color],
            user.opacity,
            user.font,
            user.fontsize,
            user.text,
        )
        sent: Optional[Message] = None
        if user.result_type == ResultType.PIC:
            sent = await msg.bot.send_photo(msg.chat.id, watermarked)
        if user.result_type == ResultType.DOC:
            sent = await msg.bot.send_document(
                chat_id=msg.chat.id, document=watermarked, thumb=watermarked
            )
        await sent.reply(**routes_messages.get("sendpic"))
    except UnidentifiedImageError:
        logger.warning("Got UnidentifiedImageError while adding watermark")
        await msg.answer("🤖 Документ поврежден или не является картинкой.")


@userdata_required
async def process_image(msg: Message, user: User):
    logger.info("Process image to add watermark...")
    await process(msg, msg.photo[-1], user)


@userdata_required
async def process_document(msg: Message, user: User):
    logger.info("Process document to add watermark...")
    await process(msg, msg.document, user)
