from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from states.state import SetWatermark
from keyboards.reply.watermark import watermark_position, colors
from config import positions, TEXT_COLORS
from loguru import logger
from aiogram.types import ReplyKeyboardRemove
from utlis.image_converter import async_image_process


def validate_opacity_number(num: str) -> bool:
    if not num.isdigit():
        return False
    num = int(num)
    if num > 255:
        return False
    return True


async def starting(msg: Message):
    logger.info(f"{msg.from_user.id} send /start")
    await msg.answer("Скидывай картиночку")
    await SetWatermark.get_pic.set()


async def get_picture(msg: Message, state: FSMContext):
    photos = msg.photo
    # получаем последнюю фотку, она наиболее норм
    last_photo = photos[-1]
    logger.info(f"{msg.from_user.id} send photo with id {last_photo.file_id}")
    await state.update_data(photo=last_photo)

    await SetWatermark.next()
    await msg.reply("Выберите позицию вотермарки: ", reply_markup=watermark_position())


async def get_position(msg: Message, state: FSMContext):
    position = msg.text
    if position not in positions:
        await msg.reply("Выберите позицию вотермарки: ", reply_markup=watermark_position())
        return
    #TODO: move logger to middleware
    logger.info(f"{msg.from_user.id} send watermark pos: {position}")
    await state.update_data(postion=position)

    await SetWatermark.next()
    await msg.reply("Выберите цвет текста", reply_markup=colors())


async def get_color(msg: Message, state: FSMContext):
    color_key = msg.text
    if color_key not in TEXT_COLORS.keys():
        await msg.reply("Выберите цвет текста", reply_markup=colors())
        return
    color = TEXT_COLORS[color_key]
    logger.info(f"{msg.from_user.id} set color: {color_key}: {color}")
    await state.update_data(color=color)

    await SetWatermark.next()
    await msg.reply("Установите прозрачность цифрой от 0 до 255 (255 полностью прозрачный, 0 - непрозрачный)",
                    reply_markup=ReplyKeyboardRemove()
                    )


async def set_opacity(msg: Message, state: FSMContext):
    is_valide_num = validate_opacity_number(msg.text)
    if not is_valide_num:
        await msg.reply("Установите прозрачность цифрой от 0 до 255 (255 полностью прозрачный, 0 - непрозрачный)",
                        reply_markup=ReplyKeyboardRemove()
                        )
        return
    opacity = int(msg.text)
    logger.info(f"{msg.from_user.id} set opacity to: {opacity}")
    await state.update_data(opacity=opacity)

    #photo = (await state.get_data())['photo']
    #path_to_pic = f"pic/{photo.file_id}"
    #await photo.download(path_to_pic)
    #watermarked_photo = await async_image_process(msg.bot.loop, path_to_pic)
    #await msg.bot.send_photo(
    #    msg.chat.id,
    #    open(watermarked_photo, "rb")
    #)
    #logger.info(f"{watermarked_photo} sended to {msg.from_user.full_name}")

