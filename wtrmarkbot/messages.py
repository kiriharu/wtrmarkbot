from aiogram.types import ReplyKeyboardRemove
from wtrmarkbot.keyboards.reply.watermark import (
    watermark_position, colors,
    fonts, result_types
)
from wtrmarkbot.keyboards.inline.menu import main_menu
from consts import MAX_FONT_SIZE

STARTING_MESSAGE = f"Привет! Добро пожаловать в @wtrmarkbot!" \
                   f"\n\n" \
                   f"Данный бот поможет без проблем наложить текст-вотермарку на картинку.\n" \
                   f"Также, тут есть следующие возможности:\n" \
                   f"📌 Возможность выбора шрифтов\n" \
                   f"📌 Возможность выбора цвета текста, его размера и прозрачности\n" \
                   f"📌 Возможность выбора позиции, где нужно разместить текст\n" \
                   f"📌 Для работы просто установи настройки и отправь картинку!.\n" \
                   f"\n\n" \
                   f"Сделал @kiriharu with <3. [Репозиторий бота](https://github.com/kiriharu/wtrmarkbot)."

routes_messages = {
    "position": dict(
        text="↕️ Выбери позицию вотермарки: ",
        reply_markup=watermark_position()
    ),
    "color": dict(
        text="🏁 Выбери цвет текста",
        reply_markup=colors()
    ),
    "opacity": dict(
        text="➿ Установи прозрачность цифрой от 1 до 255 (255 непрозрачный, 1 - полностью прозрачный)",
        reply_markup=ReplyKeyboardRemove()
    ),
    "font": dict(
        text="✍️ Выбери шрифт",
        reply_markup=fonts()
    ),
    "fontsize": dict(
        text=f"✍️ Выбери размер шрифта (до {MAX_FONT_SIZE})",
        reply_markup=ReplyKeyboardRemove()
    ),
    "text": dict(
        text=f"💬 Напиши текст вотермарки",
        reply_markup=ReplyKeyboardRemove()
    ),
    "sendpic": dict(
        text="💫 Вот твоя картинка с вотермаркой. Вышло неплохо, хочешь ещё? Отправь следующую картинку!",
        reply_markup=main_menu()
    ),
    "result_type": dict(
        text="🖼 Выбери формат ответа",
        reply_markup=result_types()
    )
}
