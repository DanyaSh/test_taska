from test_taska import User
from config import CHANEL_ID, TOKEN
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text
import keyboard

# __________________________________GLOBAL VARIABLES____________________________________

bot =   Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp  =   Dispatcher(bot)

# ______________________________________COMMANDS________________________________________

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    user=User(message)
    await user.starts(message)

@dp.message_handler(commands='help')
async def cmd_start(message: types.Message):
    user=User(message)
    await message.reply(f"help command")

# ________________________________________TEXT__________________________________________

@dp.message_handler()
async def echo(message: types.Message):
    user=User(message)
    if user.route.process=='/city_name':
        await user.weather_of_city(message)
    else:
        await message.reply(f"Моя твоя не понимать...🧐\n{message.text}")


# __________________________________INLINE BUTTONS____________________________________

@dp.callback_query_handler(text='/start')
async def start_friendly(call: types.CallbackQuery):
    user=User(call)
    user.start(call.message)

@dp.callback_query_handler(lambda call: call.data=='/help')
async def instruction(call: types.CallbackQuery):
    user=User(call)
    pass

@dp.callback_query_handler(lambda call: call.data=='/fun_weather')
async def instruction(call: types.CallbackQuery):
    user=User(call)
    await user.fun_weather(call)

@dp.callback_query_handler(lambda call: call.data=='/fun_exchange')
async def instruction(call: types.CallbackQuery):
    user=User(call)
    pass

@dp.callback_query_handler(lambda call: call.data=='/fun_animal')
async def instruction(call: types.CallbackQuery):
    user=User(call)
    await call.message.answer(text='@gif cute animal')

@dp.callback_query_handler(lambda call: call.data=='/fun_polls')
async def instruction(call: types.CallbackQuery):
    user=User(call)
    pass

# __________________________________LOCATION____________________________________

@dp.message_handler(content_types='location')
async def telephone(message: types.Message):
    user=User(message)
    await user.weather_location(message)


# '/fun_weather'
# '/fun_exchange'
# '/fun_animal'
# '/fun_polls'
