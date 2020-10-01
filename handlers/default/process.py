from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from states.state import SetWatermark
from keyboards.reply.watermark import watermark_position, colors
from config import positions, TEXT_COLORS
from loguru import logger
from utlis.image_converter import async_image_process


async def starting(msg: Message):
    logger.info(f"{msg.from_user.full_name} send /start")
    await msg.answer("Скидывай картиночку")
    await SetWatermark.get_pic.set()


async def get_picture(msg: Message, state: FSMContext):
    photos = msg.photo
    # получаем последнюю фотку, она наиболее норм
    last_photo = photos[-1]
    logger.info(f"{msg.from_user.full_name} send photo with id {last_photo.file_id}")
    await state.update_data(photo=last_photo)

    await SetWatermark.next()
    await msg.reply("Выберите позицию вотермарки: ", reply_markup=watermark_position())


async def get_position(msg: Message, state: FSMContext):
    position = msg.text
    if position not in positions:
        await msg.reply("Выберите позицию вотермарки: ", reply_markup=watermark_position())
        return
    logger.info(f"{msg.from_user.full_name} send watermark pos: {position}")
    await state.update_data(postion=position)

    await SetWatermark.next()
    await msg.reply("Выберите цвет текста", reply_markup=colors())


async def get_color(msg: Message, state: FSMContext):
    color_key = msg.text
    if color_key not in TEXT_COLORS.keys():
        await msg.reply("Выберите цвет текста", reply_markup=colors())
    color = TEXT_COLORS[color_key]
    logger.info(f"{msg.from_user.full_name} set color: {color_key}: {color}")
    await state.update_data(color=color)

    await SetWatermark.next()

    #photo = (await state.get_data())['photo']
    #path_to_pic = f"pic/{photo.file_id}"
    #await photo.download(path_to_pic)
    #watermarked_photo = await async_image_process(msg.bot.loop, path_to_pic)
    #await msg.bot.send_photo(
    #    msg.chat.id,
    #    open(watermarked_photo, "rb")
    #)
    #logger.info(f"{watermarked_photo} sended to {msg.from_user.full_name}")

