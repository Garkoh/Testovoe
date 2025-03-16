from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

settings = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text='Перейти в приложение',
            url='127.0.0.1:8000/'
        )]
    ]
)
