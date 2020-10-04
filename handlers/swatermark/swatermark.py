from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from states.swatermark import SWatermarkState
from messages import routes_messages
from middlewares.userdata import userdata_required
from models.user import User
from utlis.image_converter import async_image_process
from consts import TEXT_COLORS, POSITIONS


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
    path_to_pic = f"pic/{msg.photo[-1].file_id}"
    await msg.photo[-1].download(path_to_pic)
    color = TEXT_COLORS[user.color].copy()
    color.append(user.opacity)

    watermarked_photo = await async_image_process(
        msg.bot.loop,
        path_to_pic,
        user.position,
        tuple(color),
        f"fonts/{user.font}.ttf",
        int(user.fontsize),
        user.text
    )
    sended_pic = await msg.bot.send_photo(
        msg.chat.id,
        open(watermarked_photo, "rb")
    )
    await sended_pic.reply(**routes_messages.get("sendpic"))
    await state.finish()
