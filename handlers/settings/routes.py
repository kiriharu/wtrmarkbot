from utlis.route import Route
from states.state import SettingsState
from aiogram.types import Message, CallbackQuery
from models.user import User
from aiogram.dispatcher import FSMContext
from middlewares.userdata import userdata_required


class SettingsRoute(Route):

    def __init__(
            self, name: str,
            validator: callable,
            fail_msg: dict,
            state: SettingsState
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

    @userdata_required
    async def handle(self, msg: Message, state: FSMContext, user: User):
        if not (validated_text := await self.validate(msg)):
            return
        await User.filter(
            telegram_id=user.telegram_id
        ).update(**{self.name: validated_text})
        await msg.reply("Настройки обновлены")
        await state.finish()