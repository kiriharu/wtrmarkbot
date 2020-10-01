from aiogram.types import ReplyKeyboardMarkup
from config import positions, TEXT_COLORS, FONTS


def keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        row_width=1
    )


def watermark_position() -> ReplyKeyboardMarkup:
    return keyboard().add(*positions)


def fonts() -> ReplyKeyboardMarkup:
    return keyboard().add(*FONTS)


def colors() -> ReplyKeyboardMarkup:
    return keyboard().add(*TEXT_COLORS.keys())
