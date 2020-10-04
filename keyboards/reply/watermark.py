from aiogram.types import ReplyKeyboardMarkup
from consts import POSITIONS, TEXT_COLORS, FONTS


def keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        row_width=1
    )


def watermark_position() -> ReplyKeyboardMarkup:
    return keyboard().add(*POSITIONS)


def fonts() -> ReplyKeyboardMarkup:
    return keyboard().add(*FONTS)


def colors() -> ReplyKeyboardMarkup:
    return keyboard().add(*TEXT_COLORS.keys())
