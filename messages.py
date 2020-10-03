from aiogram.types import ReplyKeyboardRemove
from keyboards.reply.watermark import watermark_position, colors, fonts
from consts import MAX_FONT_SIZE

STARTING_MESSAGE = "TODO: заполни стартовое сообщени. А пока пиши /watermark чтобы наложить вотерку"

routes_messages = {
    "starting": dict(
        text="Скидывай картиночку.",
        reply_markup=ReplyKeyboardRemove(),
    ),
    "position": dict(
        text="Выберите позицию вотермарки: ",
        reply_markup=watermark_position()
    ),
    "color": dict(
        text="Выберите цвет текста",
        reply_markup=colors()
    ),
    "opacity": dict(
        text="Установите прозрачность цифрой от 1 до 255 (255 непрозрачный, 1 - полностью прозрачный)",
        reply_markup=ReplyKeyboardRemove()
    ),
    "font": dict(
        text="Выберите шрифт",
        reply_markup=fonts()
    ),
    "fontsize": dict(
        text=f"Выберите размер шрифта (до {MAX_FONT_SIZE})",
        reply_markup=ReplyKeyboardRemove()
    ),
    "text": dict(
        text=f"Напишите текст вотермарки",
        reply_markup=ReplyKeyboardRemove()
    )
}