from keyboards.inline.menu import settings_menu
from middlewares.userdata import userdata_required
from aiogram.types import Message, CallbackQuery
from models.user import User
from .routes import SettingsRoute
from consts import TEXT_COLORS, POSITIONS, FONTS, MAX_FONT_SIZE
from messages import routes_messages
from states.settings import SetColor, SetPosition, SetOpacity, SetFont, SetFontSize, SetText
from utlis.helpers import validate_number, check_in, get_key_by_value

configure_position = SettingsRoute(
    "position",
    POSITIONS.get,
    routes_messages.get("position"),
    SetPosition
)

configure_color = SettingsRoute(
    "color",
    lambda text: get_key_by_value(TEXT_COLORS, TEXT_COLORS.get(text)),
    routes_messages.get("color"),
    SetColor
)

configure_opacity = SettingsRoute(
    "opacity",
    validate_number,
    routes_messages.get("opacity"),
    SetOpacity
)

configure_font = SettingsRoute(
    "font",
    lambda text: check_in(text, FONTS),
    routes_messages.get("font"),
    SetFont
)

configure_fontsize = SettingsRoute(
    "fontsize",
    lambda text: validate_number(text, MAX_FONT_SIZE),
    routes_messages.get("fontsize"),
    SetFontSize
)

configure_text = SettingsRoute(
    "text",
    lambda text: text,
    routes_messages.get("text"),
    SetText
)


@userdata_required
async def settings_from_callback(callback_query: CallbackQuery, user: User):
    await callback_query.bot.edit_message_text(
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        text=f"🖼Ваши настройки для установки водяных знаков:\n\n",
        reply_markup=settings_menu(user)
    )


@userdata_required
async def settings_from_command(msg: Message, user: User):
    await msg.answer(
        f"🖼Ваши настройки для установки водяных знаков:\n\n",
        reply_markup=settings_menu(user)
    )
