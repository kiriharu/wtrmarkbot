from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from wtrmarkbot.models.user import User
from wtrmarkbot.utlis.helpers import get_key_by_value
from wtrmarkbot.consts import POSITIONS


def inline_kbrd() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(row_width=1)


def main_menu() -> InlineKeyboardMarkup:
    return inline_kbrd().add(
        InlineKeyboardButton("📖Настройки", callback_data="settings_menu"),
    )


def settings_menu(user: User) -> InlineKeyboardMarkup:
    return inline_kbrd().add(
        InlineKeyboardButton(
            f"👉Позиция: {get_key_by_value(POSITIONS, user.position)}",
            callback_data="position",
        ),
        InlineKeyboardButton(f"🟥Цвет текста: {user.color}", callback_data="color"),
        InlineKeyboardButton(f"💫Прозрачность: {user.opacity}", callback_data="opacity"),
        InlineKeyboardButton(f"✏Шрифт: {user.font}", callback_data="font"),
        InlineKeyboardButton(
            f"📈Размер шрифта: {user.fontsize}", callback_data="fontsize"
        ),
        InlineKeyboardButton(f"🗒Текст: {user.text}", callback_data="text"),
        InlineKeyboardButton(
            f"🖼Формат ответа: {user.result_type}", callback_data="result_type"
        ),
        InlineKeyboardButton(f"🌠В меню", callback_data="main_menu"),
    )
