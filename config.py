import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Loading token from .env
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

STARTING_MESSAGE = "TODO: заполни стартовое сообщени. А пока пиши /watermark чтобы наложить вотерку"

MAX_FONT_SIZE = 96
MARGIN = 10

FONTS = list(map(lambda x: x.replace(".ttf", ""), os.listdir("fonts")))

TEXT_COLORS = {
    "Белый": [255, 255, 255],
    "Черный": [0, 0, 0],
    "Красный": [255, 0, 0],
    "Зеленый": [0, 255, 0],
    "Синий": [0, 0, 255],
}

positions = {
    'По центру': 0,
    'Сверху': 1,
    'Снизу': 4,
    'Слева': 2,
    'Справа': 8,

    'Сверху-слева': 1 | 2,
    'Снизу-слева': 4 | 2,
    'Сверху-справа': 1 | 8,
    'Снизу-справа': 4 | 8,
}
