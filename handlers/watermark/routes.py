from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from states.watermark import SetWatermark
from utlis.route import Route


class TextRoute(Route):

    def __init__(self,
                 name: str,
                 validator: callable,
                 fail_msg: dict,
                 nxt_call_msg: dict
                 ):
        super().__init__(
            name, validator, fail_msg, SetWatermark
        )
        self.nxt_call_msg = nxt_call_msg

    async def handle(self, msg: Message, state: FSMContext):
        if (validated_text := await self.validate(msg)) is None:
            return
        await state.update_data(
            data={self.name: validated_text}
        )
        await self.state_obj.next()
        await msg.reply(**self.nxt_call_msg)

