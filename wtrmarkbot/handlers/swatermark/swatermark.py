from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from wtrmarkbot.states.swatermark import SWatermarkState
from wtrmarkbot.messages import routes_messages
from wtrmarkbot.middlewares.userdata import userdata_required
from wtrmarkbot.models.user import User
from wtrmarkbot.consts import TEXT_COLORS
from wtrmarkbot.utlis.image_converter import watermark_process


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
