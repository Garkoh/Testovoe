from aiogram import Bot, Dispatcher

from src.bot.config import TOKEN
from src.bot.handlers import router

bot = Bot(token=TOKEN)

dp = Dispatcher()

dp.include_router(router)
