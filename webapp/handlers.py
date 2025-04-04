import os

from fastapi import APIRouter, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# import bot
from services import calculate_birthday_info


webapp_router = APIRouter()


templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))


@webapp_router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@webapp_router.get("/birthday", response_class=HTMLResponse)
async def birthday(request: Request, birthdate: str = Query(...)):
    user_data, share_link = await calculate_birthday_info(birthdate)
    return templates.TemplateResponse("result.html", {"request": request, "user_data": user_data, "share_link": share_link})


# @webapp_router.on_event("shutdown")
# async def shutdown():
#     await bot.session.close()