from aiogram.types import ReplyKeyboardRemove, Message
from aiogram.dispatcher import FSMContext
from states.state import SetWatermark
from keyboards.reply.watermark import watermark_position, colors, fonts
from config import positions, TEXT_COLORS, FONTS, MAX_FONT_SIZE
from typing import Optional


def check_in(text: str, _list: list) -> Optional[str]:
    if text in _list:
        return text


def validate_number(num: str, max_num: int = 255) -> Optional[int]:
    if not num.isdigit():
        return
    int_num = int(num)
    if not int_num > max_num:
        return int_num


messages = {
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


class TextRoute:

    def __init__(
            self,
            name: str,
            validator: callable,
            fail_message_args: dict,
            next_call_message_args: dict
    ):
        self.name = name
        self.validator = validator
        self.fail_message_args = fail_message_args
        self.next_call_message_args = next_call_message_args

    async def handle(self, msg: Message, fsm: FSMContext):
        text = msg.text
        validated_text = self.validator(text)
        if not validated_text:
            return await msg.reply(**self.fail_message_args)
        await fsm.update_data(
            data={self.name: validated_text}
        )

        await SetWatermark.next()
        await msg.reply(**self.next_call_message_args)


position = TextRoute(
    "position",
    lambda text: positions.get(text),
    messages.get("position"),
    messages.get("color")
)
color = TextRoute(
    "color",
    lambda text: TEXT_COLORS.get(text),
    messages.get("color"),
    messages.get("opacity")
)
opacity = TextRoute(
    "opacity",
    lambda text: validate_number(text),
    messages.get("opacity"),
    messages.get("font")
)
font = TextRoute(
    "font",
    lambda text: check_in(text, FONTS),
    messages.get("font"),
    messages.get("fontsize")
)
fontsize = TextRoute(
    "fontsize",
    lambda text: validate_number(text, MAX_FONT_SIZE),
    messages.get("fontsize"),
    messages.get("text")
)
