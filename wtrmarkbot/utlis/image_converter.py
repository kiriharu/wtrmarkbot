import asyncio
from time import time
from typing import Union, Tuple, BinaryIO
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
from functools import partial

from PIL import ImageFont, ImageDraw, Image
from loguru import logger

from wtrmarkbot.consts import MARGIN, Side

pool = ThreadPoolExecutor()


def get_xy(
    position: Union[int, Side],
    width: int,
    height: int,
    text_width: int,
    text_height: int,
) -> Tuple[int, int]:
    position = Side(position)
    x, y = (width - text_width) // 2, (height - text_height) // 2

    if position & Side.TOP:
        y = 0 + MARGIN
    elif position & Side.BOTTOM:
        y = height - text_height - MARGIN
    if position & Side.LEFT:
        x = 0 + MARGIN
    elif position & Side.RIGHT:
        x = width - text_width - MARGIN

    return x, y


def set_watermark(img_bytes, position, color, font, size, text):
    im = Image.open(img_bytes).convert("RGBA")
    width, height = im.size

    txt_img = Image.new("RGBA", im.size, (255, 255, 255, 0))
    font = ImageFont.truetype(font, size)
    draw = ImageDraw.Draw(txt_img)

    textwidth, textheight = draw.textsize(text, font)

    x, y = get_xy(position, width, height, textwidth, textheight)

    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font, fill=color)

    combined = Image.alpha_composite(im, txt_img)
    combined.convert("RGBA")
    combined_bytearr = BytesIO()
    combined.save(combined_bytearr, format="PNG")

    return combined_bytearr.getvalue()


async def async_image_process(img_bytes, position, color, font, size, text):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        pool, partial(set_watermark, img_bytes, position, color, font, size, text)
    )


async def add_watermark(
    photo: Union[BytesIO, BinaryIO],
    position: str,
    color: list,
    opacity: int,
    font: str,
    fsize: int,
    text: str,
) -> BytesIO:
    ts = time()
    color_with_opacity = color.copy()
    color_with_opacity.append(opacity)
    image = await async_image_process(
        photo,
        position,
        tuple(color_with_opacity),
        f"fonts/{font}.ttf",
        int(fsize),
        text,
    )
    te = time()
    took = te - ts
    logger.info(f"Image watermarking took {took}s")
    return image
