from aiogram.fsm.state import StatesGroup, State

class Exchange(StatesGroup):
    first_prompt = State()
    second_prompt = State()
    value_prompt = State()

class Weather(StatesGroup):
    city_prompt = State()