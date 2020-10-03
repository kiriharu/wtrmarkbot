from aiogram.dispatcher.filters.state import State, StatesGroup


class SWatermarkState(StatesGroup):
    get_pic = State()
