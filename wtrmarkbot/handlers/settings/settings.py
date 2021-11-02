from aiogram.types import CallbackQuery
from loguru import logger

from wtrmarkbot.keyboards.inline.menu import settings_menu
from wtrmarkbot.middlewares.userdata import userdata_required
from wtrmarkbot.models.user import User, ResultType
from wtrmarkbot.handlers.settings.routes import SettingsRoute
from wtrmarkbot.consts import TEXT_COLORS, POSITIONS, FONTS, MAX_FONT_SIZE
from wtrmarkbot.messages import routes_messages
from wtrmarkbot.states.settings import (
    SetColor,
    SetPosition,
    SetOpacity,
    SetFont,
    SetFontSize,
    SetText,
    SetResultType,
)
from wtrmarkbot.utlis.helpers import validate_number, check_in, get_key_by_value
from wtrmarkbot.handlers.settings.utils import create_example

configure_position = SettingsRoute(
    "position", POSITIONS.get, routes_messages.get("position"), SetPosition
)

configure_color = SettingsRoute(
    "color",
    lambda text: get_key_by_value(TEXT_COLORS, TEXT_COLORS.get(text)),
    routes_messages.get("color"),
    SetColor,
)

configure_opacity = SettingsRoute(
    "opacity", validate_number, routes_messages.get("opacity"), SetOpacity
)

configure_font = SettingsRoute(
    "font", lambda text: check_in(text, FONTS), routes_messages.get("font"), SetFont
)

configure_fontsize = SettingsRoute(
    "fontsize",
    lambda text: validate_number(text, MAX_FONT_SIZE),
    routes_messages.get("fontsize"),
    SetFontSize,
)

configure_text = SettingsRoute(
    "text", lambda text: text, routes_messages.get("text"), SetText
)

configure_result_type = SettingsRoute(
    "result_type",
    lambda text: check_in(text, ResultType.get_results()),
    routes_messages.get("result_type"),
    SetResultType,
)


@userdata_required
async def settings_from_callback(callback_query: CallbackQuery, user: User):
    logger.info(f"{user.telegram_id} called settings")
    await callback_query.bot.send_photo(
        chat_id=callback_query.from_user.id,
        photo=await create_example(user),
        caption=f"🖼Ваши настройки для установки водяных знаков:\n\n",
        reply_markup=settings_menu(user),
    )

    await callback_query.answer()
