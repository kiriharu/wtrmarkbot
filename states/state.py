from aiogram.dispatcher.filters.state import State, StatesGroup


class SetWatermark(StatesGroup):
    get_pic = State()
    set_position = State()
    set_textcolor = State()
    set_opacity = State()
    set_font = State()
    set_fontsize = State()
    set_text = State()

# TIP!: Наследование от базового класса вызывает какие-то непонятные баги :/


class SetColor(StatesGroup):
    input_state = State()


class SetPosition(StatesGroup):
    input_state = State()


class SetOpacity(StatesGroup):
    input_state = State()


class SetFont(StatesGroup):
    input_state = State()


class SetFontSize(StatesGroup):
    input_state = State()


class SetText(StatesGroup):
    input_state = State()
