from aiogram.dispatcher.filters.state import State, StatesGroup


class SetWatermark(StatesGroup):
    get_pic = State()
    set_position = State()
    # TODO: цвет текста
    # TODO: наложить пикчу?
