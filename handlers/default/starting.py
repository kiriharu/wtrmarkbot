from aiogram.types import Message
from config import STARTING_MESSAGE


async def start(msg: Message):
    await msg.answer(STARTING_MESSAGE)
