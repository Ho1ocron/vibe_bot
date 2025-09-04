from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from asyncio import run
from settings import TOKEN, ADMIN_IDS
from aiogram.fsm.storage.redis import RedisStorage
import redis.asyncio as redis
import handlers, logging, sys


async def main() -> None:
    
    bot = Bot(
        TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    redis_client = redis.Redis(host="localhost", port=6379, db=0)
    storage = RedisStorage(redis_client)
    dp = Dispatcher()
    
    dp.include_routers(
        handlers.message_router,
        handlers.callback_router,
        handlers.admin_router,
    )
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    run((main()))