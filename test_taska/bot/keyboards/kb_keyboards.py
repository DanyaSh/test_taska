from aiogram.types import ReplyKeyboardMarkup, KeyboardButtonPollType
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

def get_poll_kb() -> ReplyKeyboardMarkup:
    """Get keyboard for create poll in private group
    """
    kb = ReplyKeyboardBuilder()

    kb.button(
        text="❌Cancel"
    )
    
    kb.button(
        text="✅Create poll",
        request_poll=KeyboardButtonPollType()
    )

    kb.adjust(2)
    kb = kb.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True
    )

    return kb