from datetime import datetime

from fastapi import HTTPException

from src.bot.cache.accessor import get_redis_data, on_shutdown, get_redis_connection


# Логика обработки данных для вычисления информации о дне рождения
async def calculate_birthday_info(birthdate: str):
    try:
        birthdate_obj = datetime.strptime(birthdate, "%Y-%m-%d")

        now = datetime.now()

        delta = birthdate_obj.replace(year=now.year) - now


        if delta.days < 0:
            birthdate_obj = birthdate_obj.replace(year=now.year + 1)
            delta = birthdate_obj.replace(year=now.year + 1) - now

        days_left = delta.days
        hours_left = delta.seconds // 3600
        minutes_left = (delta.seconds // 60) % 60

        # Открытие Redis
        redis_client = await get_redis_connection()

        # Получение данных из Redis
        user = await get_redis_data()

        # Конвертация данных к Json формату
        decoded_data = {key.decode('utf-8'): value.decode('utf-8') if isinstance(value, bytes) else value for key, value
                        in user.items()}

        user_data = {
            "first_name": f"{decoded_data["first_name"]}",
            "last_name": f"{decoded_data["last_name"]}",
            "username": f"{decoded_data["username"]}",
            "days_left": days_left,
            "hours_left": hours_left,
            "minutes_left": minutes_left,
            "birthdate": birthdate_obj.strftime("%Y-%m-%d")
        }
        # Закрытие Redis
        await on_shutdown(redis_client)

        share_link = f"http://127.0.0.1:8000/birthday?birthdate={birthdate_obj.strftime("%Y-%m-%d")}"

        return user_data, share_link
    except Exception as e:
        raise HTTPException(status_code=400, detail="Ошибка при обработке даты.")
