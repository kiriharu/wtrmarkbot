from typing import Any, Optional
from aiogram.types import Message


class Route:

    def __init__(
        self,
        name: str, validator: callable,
        fail_message_args: dict,
        state_obj: Any,
    ):
        self.name = name
        self.validator = validator
        self.fail_message_args = fail_message_args
        self.state_obj = state_obj

    async def handle(self, *args, **kwargs):
        pass

    def register(self, *args, **kwargs):
        pass

    async def validate(self, msg: Message) -> Optional[Any]:
        validated_text = self.validator(msg.text)
        if validated_text is None:
            await msg.reply(**self.fail_message_args)
            return None
        return validated_text
