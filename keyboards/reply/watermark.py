from aiogram.types import ReplyKeyboardMarkup
from config import positions, TEXT_COLORS


def watermark_position() -> ReplyKeyboardMarkup:

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for pos in positions:
        keyboard.add(pos)
    return keyboard


def colors() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for color in TEXT_COLORS.keys():
        keyboard.add(color)
    return keyboard
