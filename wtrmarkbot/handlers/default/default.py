from aiogram.types import Message, CallbackQuery
from loguru import logger

from wtrmarkbot.messages import STARTING_MESSAGE
from wtrmarkbot.middlewares.userdata import userdata_required
from wtrmarkbot.models.user import User
from wtrmarkbot.keyboards.inline.menu import main_menu


@userdata_required
async def start_from_command(msg: Message, user: User):
    logger.info(f"{user.telegram_id} called /start")
    await msg.answer(
        STARTING_MESSAGE,
        reply_markup=main_menu(),
        parse_mode="Markdown",
        disable_web_page_preview=True,
    )


@userdata_required
async def start_from_callback(callback_query: CallbackQuery, user: User):
    logger.info(f"{user.telegram_id} called menu callback")
    await callback_query.bot.send_message(
        chat_id=callback_query.from_user.id,
        text=STARTING_MESSAGE,
        reply_markup=main_menu(),
        parse_mode="Markdown",
        disable_web_page_preview=True,
    )
    await callback_query.answer()
