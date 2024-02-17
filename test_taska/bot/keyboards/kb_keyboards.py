from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_location_kb() -> ReplyKeyboardMarkup:
    """Get location keyboard"""
    kb = ReplyKeyboardBuilder()
    kb.button(
        text="📍Send my location",
        request_location=True
    )
    kb.adjust(1)
    kb = kb.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return kb