import json
from ast import literal_eval
from pathlib import Path
from os import getenv
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

DOTENV_PATH = BASE_DIR / '.env'
PATHES_FILE = BASE_DIR / "pathes.json"
MAPS_DIR = BASE_DIR / "map"

if DOTENV_PATH.exists():
    load_dotenv(DOTENV_PATH)

# * Telegram Config

TOKEN = getenv('TOKEN')
ADMIN_IDS = literal_eval(getenv('ADMIN_IDS'))

# * Database Config

DB_HOST = getenv('DB_HOST')

DB_PORT = getenv('DB_PORT')

DB_USER = getenv('DB_USER')

DB_PASS = getenv('DB_PASS')

DB_NAME = getenv('DB_NAME')

DEBUG = getenv('DEBUG')

TORTOISE_MODELS = ['database']

DB_URL: str # Сделать тут или не тут db_url

if DEBUG:
    DB_URL = ""


async def get_maps_path(map_name: str) -> str:
    with open(PATHES_FILE, encoding="utf-8") as f:
        data = json.load(f)

    # Return the correct map path or raise an error if not found
    try:
        return data[map_name]
    except KeyError:
        raise ValueError(f"❌ Map '{map_name}' not found in pathes.json")


