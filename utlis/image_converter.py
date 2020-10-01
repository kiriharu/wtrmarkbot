from concurrent.futures import ThreadPoolExecutor
from functools import partial
from PIL import ImageFont, ImageDraw, Image

pool = ThreadPoolExecutor()


def set_watermark(img_path, position, color, font, size, text):
    im = Image.open(img_path).convert("RGBA")
    width, height = im.size

    txt_img = Image.new("RGBA", im.size, (255, 255, 255, 0))
    font = ImageFont.truetype(font, size)
    draw = ImageDraw.Draw(txt_img)

    textwidth, textheight = draw.textsize(text, font)

    # calculate the x,y coordinates of the text
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

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