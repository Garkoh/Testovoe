import asyncio
import uvicorn

# from src.bot.bot import bot, dp
from app import app


# async def start_bot():
#     await dp.start_polling(bot)

async def main():
    # bot_task = asyncio.create_task(start_bot())
    uvicorn_task = asyncio.create_task(run_uvicorn())
    await uvicorn_task
    # await asyncio.gather(bot_task, uvicorn_task)

async def run_uvicorn():
    config = uvicorn.Config(app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)
    await server.serve()


# logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    # logging.info("Запуск бота...")
    asyncio.run(main())

