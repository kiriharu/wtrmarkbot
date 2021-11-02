import os

from wtrmarkbot.consts import TEXT_COLORS
from wtrmarkbot.models import User
from wtrmarkbot.utlis.image_converter import add_watermark


async def create_example(user: User):
    current_dir = os.getcwd()
    example_path = os.path.join(current_dir, "etc", "example.png")
    with open(example_path, "rb") as example:
        return await add_watermark(
            example,
            user.position,
            TEXT_COLORS[user.color],
            user.opacity,
            user.font,
            user.fontsize,
            user.text,
        )