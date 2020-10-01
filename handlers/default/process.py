from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from states.state import SetWatermark
from utlis.image_converter import async_image_process
from .routes import position, color, opacity, font, fontsize, messages


async def starting(msg: Message):
    await msg.answer(**messages.get("starting"))
    await SetWatermark.get_pic.set()


async def get_picture(msg: Message, state: FSMContext):
    last_photo = msg.photo[-1]
    await state.update_data(photo=last_photo)
    await SetWatermark.next()
    await msg.reply(**messages.get("position"))


async def get_position(msg: Message, state: FSMContext):
    await position.handle(msg, state)


async def get_color(msg: Message, state: FSMContext):
    await color.handle(msg, state)


async def set_opacity(msg: Message, state: FSMContext):
    await opacity.handle(msg, state)


async def set_font(msg: Message, state: FSMContext):
    await font.handle(msg, state)


async def set_fontsize(msg: Message, state: FSMContext):
    await fontsize.handle(msg, state)


async def set_text(msg: Message, state: FSMContext):
    text = msg.text
    data = await state.get_data()

    data.get("color").append(data.get("opacity"))
    path_to_pic = f"pic/{data.get('photo').file_id}"

    await data.get('photo').download(path_to_pic)
    watermarked_photo = await async_image_process(
        msg.bot.loop,
        path_to_pic,
        data.get("position"),
        tuple(data.get("color")),
        f"fonts/{data.get('font')}.ttf",
        data.get("fontsize"),
        text
    )
    await msg.bot.send_photo(
        msg.chat.id,
        open(watermarked_photo, "rb")
    )
    await msg.reply("Собственно, вот твоё фото с вотермаркой. "
                    "Клацай /start чтобы поставить вотермарку на ещё одно фото.")
    await state.finish()
