from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_start_ikb() -> InlineKeyboardMarkup:
    """Get ikb for main menu
    """
    b_weather   = InlineKeyboardButton(text='🌦 Weather', callback_data='/fun_weather')
    b_exchange  = InlineKeyboardButton(text='🏧 Exchange', callback_data='/fun_exchange')
    b_animal    = InlineKeyboardButton(text='🐱 Cute animal', callback_data='/fun_animal')
    b_polls     = InlineKeyboardButton(text='📝 Poll', callback_data='/fun_poll')

    line1=[b_weather, b_exchange]
    line2=[b_animal, b_polls]
    buttons=[line1, line2]

    ikb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return ikb

def get_home_ikb() -> InlineKeyboardMarkup:
    """Get ikb for home
    """
    b_home   = InlineKeyboardButton(text='🏠 Home', callback_data='/start')

    line1=[b_home]
    buttons=[line1]

    ikb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return ikb