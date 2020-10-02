from concurrent.futures import ThreadPoolExecutor
from functools import partial
from enum import IntEnum
from typing import Union, Tuple
from PIL import ImageFont, ImageDraw, Image
from config import MARGIN
pool = ThreadPoolExecutor()


class Side(IntEnum):
    CENTER = 0
    TOP = 1
    BOTTOM = 4
    LEFT = 2
    RIGHT = 8

    TOP_LEFT = TOP | LEFT
    TOP_RIGHT = TOP | RIGHT
    BOTTOM_LEFT = BOTTOM | LEFT
    BOTTOM_RIGHT = BOTTOM | RIGHT


def get_xy(position: Union[int, Side],
           width: int,
           height: int,
           text_width: int,
           text_height: int,) -> Tuple[int, int]:
    position = Side(position)
    x, y = (width - text_width)//2, (height - text_width)//2

    if position & Side.TOP:
        y = 0 + MARGIN
    elif position & Side.BOTTOM:
        y = height - text_height - MARGIN
    if position & Side.LEFT:
        x = 0 + MARGIN
    elif position & Side.RIGHT:
        x = width - text_width - MARGIN

    return x, y


def set_watermark(img_path, position, color, font, size, text):
    im = Image.open(img_path).convert("RGBA")
    width, height = im.size

    txt_img = Image.new("RGBA", im.size, (255, 255, 255, 0))
    font = ImageFont.truetype(font, size)
    draw = ImageDraw.Draw(txt_img)

    textwidth, textheight = draw.textsize(text, font)

    x, y = get_xy(position, width, height, textwidth, textheight)

    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font, fill=color)

    combined = Image.alpha_composite(im, txt_img)
    combined.convert('RGBA')
    save_path = f"{img_path}_watermarked.png"
    combined.save(save_path)

    return save_path


async def async_image_process(loop, img, position, color, font, size, text):
    return await loop.run_in_executor(
        pool,
        partial(
            set_watermark, img, position,
            color, font, size, text
        )
    )