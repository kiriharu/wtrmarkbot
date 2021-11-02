from aiogram.dispatcher.filters.state import State, StatesGroup


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


class SetResultType(StatesGroup):
    input_state = State()
