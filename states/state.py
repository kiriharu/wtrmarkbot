from aiogram.dispatcher.filters.state import State, StatesGroup


class SetWatermark(StatesGroup):
    get_pic = State()
    set_position = State()
    set_textcolor = State()
    # TODO: Прозрачность
    # TODO: список шрифтов
    # TODO: размер шрифта
    # TODO: какой текст
