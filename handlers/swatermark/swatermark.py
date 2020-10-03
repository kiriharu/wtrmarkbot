from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from states.swatermark import SWatermarkState
from messages import routes_messages


async def from_callback(callback_query: CallbackQuery):
    await callback_query.bot.send_message(
        chat_id=callback_query.from_user.id,
        **routes_messages.get("starting")
    )
    await SWatermarkState.get_pic.set()


async def from_command(msg: Message):
    await msg.answer(**routes_messages.get("starting"))
    await SWatermarkState.get_pic.set()


async def process(msg: Message, state: FSMContext):
    last_photo = msg.photo[-1]
    await state.update_data(photo=last_photo)

