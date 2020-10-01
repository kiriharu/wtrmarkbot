from aiogram.types import ReplyKeyboardMarkup

positions = [
    "Сверху в левом углу",
    "Сверху в правом углу",
    "Снизу в левом углу",
    "Снизу в правом углу",
    "По центру"
]


def watermark_position() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for pos in positions:
        keyboard.add(pos)
    return keyboard
