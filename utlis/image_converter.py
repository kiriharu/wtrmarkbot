from concurrent.futures import ThreadPoolExecutor
from functools import partial
from PIL import ImageFont, ImageDraw, Image
from consts import MARGIN
from messages import routes_messages
from io import BytesIO

pool = ThreadPoolExecutor()


def get_xy(position_num, width, height, text_width, text_height) -> tuple:
    if position_num == 1:
        # Сверху в левом углу
        return 0 + MARGIN, 0 + MARGIN
    if position_num == 2:
        # Сверху в правом углу
        return width - text_width - MARGIN, 0 + MARGIN
    if position_num == 3:
        # Снизу в левом углу
        return 0 + MARGIN, height - text_height - MARGIN
    if position_num == 4:
        # Снизу в правом углу
        return width - text_width - MARGIN, height - text_height - MARGIN
    if position_num == 5:
        # По центру
        return (width - text_width) // 2, (height - text_width) // 2


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
    combined.convert('RGBA')
    combined_bytearr = BytesIO()
    combined.save(combined_bytearr, format="PNG")

    return combined_bytearr.getvalue()


async def async_image_process(loop, img_bytes, position, color, font, size, text):
    return await loop.run_in_executor(
        pool,
        partial(
            set_watermark, img_bytes, position,
            color, font, size, text
        )
    )


async def watermark_process(msg, photo, position, color,
                            opacity, font, fsize, text):
    pic_bytes = BytesIO()
    await photo.download(pic_bytes)
    color_with_opacity = color.copy()
    color_with_opacity.append(opacity)
    watermarked_photo = await async_image_process(
        msg.bot.loop,
        pic_bytes,
        position,
        tuple(color_with_opacity),
        f"fonts/{font}.ttf",
        int(fsize),
        text
    )
    sended_pic = await msg.bot.send_photo(
        msg.chat.id,
        watermarked_photo
    )
    await sended_pic.reply(**routes_messages.get("sendpic"))
