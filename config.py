import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Loading token from .env
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

FONTS = list(map(lambda x: x.replace(".ttf", ""), os.listdir("fonts")))

TEXT_COLORS = {
    "Белый": [255, 255, 255],
    "Черный": [0, 0, 0],
    "Красный": [255, 0, 0],
    "Зеленый": [0, 255, 0],
    "Синий": [0, 0, 255],
}

positions = [
    "Сверху в левом углу",
    "Сверху в правом углу",
    "Снизу в левом углу",
    "Снизу в правом углу",
    "По центру"
]