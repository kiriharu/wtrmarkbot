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
    "Сверху в левом углу": 1,
    "Сверху в правом углу": 2,
    "Снизу в левом углу": 3,
    "Снизу в правом углу": 4,
    "По центру": 5
}
