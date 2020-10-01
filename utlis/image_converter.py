from concurrent.futures import ThreadPoolExecutor
from functools import partial
from PIL import ImageFont, ImageDraw, Image

pool = ThreadPoolExecutor()


def set_watermark(img_path):
    im = Image.open(img_path)
    width, height = im.size

    draw = ImageDraw.Draw(im)
    text = "it-talks"

    font = ImageFont.truetype('fonts/MotorolaV50copy.ttf', 36)
    textwidth, textheight = draw.textsize(text, font)

    # calculate the x,y coordinates of the text
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font)

    save_path = f"{img_path}_watermarked.jpg"
    # Save watermarked image
    im.save(save_path)
    return save_path


async def async_image_process(loop, img):
    return await loop.run_in_executor(
        pool,
        partial(set_watermark, img)
    )