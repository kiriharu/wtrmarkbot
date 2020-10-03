from keyboards.inline.menu import settings_menu
from middlewares.userdata import userdata_required
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from models.user import User
from handlers.watermark.routes import messages
from states.state import SetColor
from config import TEXT_COLORS
from .routes import color


@userdata_required
async def settings_from_callback(callback_query: CallbackQuery, user: User):
    await callback_query.bot.edit_message_text(
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        text=f"🖼Ваши настройки для установки водяных знаков:\n\n",
        reply_markup=settings_menu(user)
    )


# TODO: Сделать отображение позиции, а не номера позиции
@userdata_required
async def settings_from_command(msg: Message, user: User):
    await msg.answer(
        f"🖼Ваши настройки для установки водяных знаков:\n\n",
        reply_markup=settings_menu(user)
    )


async def set_color_join(callback_query: CallbackQuery):
    await color.join(callback_query)
    #await callback_query.bot.send_message(
    #    chat_id=callback_query.from_user.id,
    #    **messages.get("color")
    #)
    #await SetColor.input_state.set()


@userdata_required
async def set_color_state(msg: Message, state: FSMContext, user: User):
    await color.handle(msg, state, user)
    #color = msg.text
    #if msg.text not in TEXT_COLORS.keys():
    #    return await msg.answer(**messages.get("color"))
    #await User.filter(telegram_id=user.telegram_id).update(color=color)
    #await msg.answer(f"Вы успешно установили цвет на {color}")
    #await state.finish()
    #await settings_from_command(msg, user)
