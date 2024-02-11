#from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#
#def get_main_kb() -> InlineKeyboardMarkup:
#    """Get kb for main menu
#    """
#    ikb = InlineKeyboardMarkup(inline_keyboard=[
#        [InlineKeyboardButton('Button1', callback_data='cb_btn_1_main')]
#    ])
#    return ikb


from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_main_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Да")
    kb.button(text="Нет")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)