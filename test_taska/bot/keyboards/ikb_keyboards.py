import json
import os
from dotenv import load_dotenv, find_dotenv
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv(find_dotenv())
work_dir=os.getenv('CAT')

def get_start_ikb() -> InlineKeyboardMarkup:
    """Get ikb for main menu
"""
    b_weather   = InlineKeyboardButton(
        text='🌦 Weather', 
        callback_data='/fun_weather'
    )
    
    b_exchange  = InlineKeyboardButton(
        text='🏧 Exchange', 
        callback_data='/fun_exchange'
    )
    
    b_animal    = InlineKeyboardButton(
        text='🐱 Cute animal', 
        callback_data='/fun_animal'
    )
    
    b_polls     = InlineKeyboardButton(
        text='📝 Poll', 
        callback_data='/fun_poll'
    )

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

def get_cities_ikb(text) -> InlineKeyboardMarkup:
    """Get ikb for list of cities
    """
    with open(f"{work_dir}test_taska/bot/data/city_list.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    
    dict_city = {}
    for x in data:
        dict_city[x["name"]]=x['id']
    list_result=[]
    for x in dict_city.keys():
        if text.lower() in x.lower(): list_result.append(x)

    buttons=[]
    for x in list_result:
        b_city = InlineKeyboardButton(
            text=x, 
            callback_data='/city_id_'+str(dict_city[x])
        )
        buttons.append([b_city])
    ikb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return(ikb)