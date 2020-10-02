from keyboards.inline.menu import settings_menu
from middlewares.userdata import userdata_required
from aiogram.types import Message, CallbackQuery
from models.user import User


@userdata_required
async def settings_from_callback(callback_query: CallbackQuery, user: User):
    await callback_query.bot.edit_message_text(
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        text=f"🖼Ваши настройки для установки водяных знаков:\n\n",
        reply_markup=settings_menu(user)
    )


# TODO: Сделать отображение позиции
@userdata_required
async def settings_from_command(msg: Message, user: User):
    await msg.answer(
        f"🖼Ваши настройки для установки водяных знаков:\n\n",
        reply_markup=settings_menu(user)
    )
