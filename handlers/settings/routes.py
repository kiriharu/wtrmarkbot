from utlis.route import Route
from aiogram.types import Message, CallbackQuery
from models.user import User
from aiogram.dispatcher import FSMContext
from middlewares.userdata import userdata_required
from aiogram import Dispatcher
from aiogram.types import ContentTypes
from keyboards.inline.menu import settings_menu


class SettingsRoute(Route):

    def __init__(
            self, name: str,
            validator: callable,
            fail_msg: dict,
            state
    ):
        super().__init__(
            name, validator, fail_msg, state
        )

    async def join(self, callback: CallbackQuery):
        await callback.bot.send_message(
            chat_id=callback.from_user.id,
            **self.fail_message_args
        )
        await self.state_obj.input_state.set()

    def register(self, dp: Dispatcher):

        dp.register_callback_query_handler(
            self.join,
            lambda c: c.data and c.data == self.name
        )

        dp.register_message_handler(
            self.handle,
            state=self.state_obj.input_state,
            content_types=ContentTypes.TEXT
        )

    @userdata_required
    async def handle(self, msg: Message, state: FSMContext, user: User):
        if (validated_text := await self.validate(msg)) is None:
            return
        await User.filter(
            telegram_id=user.telegram_id
        ).update(**{self.name: validated_text})

        updated_user = await User.filter(telegram_id=user.telegram_id).get()

        await msg.reply(
            "Настройки обновлены", reply_markup=settings_menu(updated_user)
        )
        await state.finish()
