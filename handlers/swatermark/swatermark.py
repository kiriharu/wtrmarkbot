from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from states.swatermark import SWatermarkState
from messages import routes_messages
from middlewares.userdata import userdata_required
from models.user import User
from consts import TEXT_COLORS
from utlis.image_converter import watermark_process


async def from_callback(callback_query: CallbackQuery):
    await callback_query.bot.send_message(
        chat_id=callback_query.from_user.id,
        **routes_messages.get("starting")
    )
    await SWatermarkState.sget_pic.set()


async def from_command(msg: Message):
    await msg.answer(**routes_messages.get("starting"))
    await SWatermarkState.sget_pic.set()


@userdata_required
async def process(msg: Message, state: FSMContext, user: User):

    await watermark_process(
        msg, msg.photo[-1], user.position, TEXT_COLORS[user.color], user.opacity,
        user.font, user.fontsize, user.text
    )

    await state.finish()
