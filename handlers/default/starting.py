from aiogram.types import Message
from config import STARTING_MESSAGE
from middlewares.userdata import userdata_required
from models.user import User


@userdata_required
async def start(msg: Message, user: User):
    await msg.answer(STARTING_MESSAGE)
