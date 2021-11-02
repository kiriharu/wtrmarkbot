import os
from enum import IntEnum


MAX_FONT_SIZE = 96
MARGIN = 10

FONTS = list(map(lambda x: x.replace(".ttf", ""), os.listdir("fonts")))


class Side(IntEnum):
    CENTER = 0
    TOP = 1
    BOTTOM = 4
    LEFT = 2
    RIGHT = 8

    TOP_LEFT = TOP | LEFT
    TOP_RIGHT = TOP | RIGHT
    BOTTOM_LEFT = BOTTOM | LEFT
    BOTTOM_RIGHT = BOTTOM | RIGHT


TEXT_COLORS = {
    "Белый": [255, 255, 255],
    "Черный": [0, 0, 0],
    "Красный": [255, 0, 0],
    "Зеленый": [0, 255, 0],
    "Синий": [0, 0, 255],
}

POSITIONS = {
    "Сверху": Side.TOP,
    "Снизу": Side.BOTTOM,
    "Слева": Side.LEFT,
    "Справа": Side.RIGHT,

    "Сверху в левом углу": Side.TOP_LEFT,
    "Сверху в правом углу": Side.TOP_RIGHT,
    "Снизу в левом углу": Side.BOTTOM_LEFT,
    "Снизу в правом углу": Side.BOTTOM_RIGHT,
    "По центру": Side.CENTER
}
