from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from handlers import webapp_router

# Инициализация FastAPI
app = FastAPI()

# Добавление CORS, чтобы обеспечить доступ из бота
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Подключение маршрутов WebApp
app.include_router(webapp_router)
