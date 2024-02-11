from test_taska import User
# from config import TOKEN, GROUP_ID
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# __________________________________CONSTANTS____________________________________
TOKEN           = os.getenv('TOKEN')
GROUP_ID        = os.getenv('GROUP_ID')

# __________________________________GLOBAL VARIABLES____________________________________

bot =   Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp  =   Dispatcher(bot)

# ______________________________________COMMANDS________________________________________

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    user=User(message)
    await user.starts(message)

@dp.message_handler(commands='help')
async def cmd_help(message: types.Message):
    user=User(message)
    await message.reply(f"help command")

@dp.message_handler(commands='about')
async def cmd_about(message: types.Message):
    user=User(message)
    await user.about(message)

# ________________________________________TEXT__________________________________________

@dp.message_handler()
async def echo(message: types.Message):
    user=User(message)
    if user.route.process=='/city_name':
        await user.weather_of_city(message)
    elif user.route.process=='/pairs':
        await user.pairs_text(message)
    elif user.route.process=='/convert':
        await user.exchange_input(message)
    elif message.text=="❌ Cancel":
        await user.cancel(message)
    else:
        await message.reply(f"Моя твоя не понимать...🧐\n{message.text}")

# __________________________________INLINE BUTTONS____________________________________

@dp.callback_query_handler(lambda call: call.data=='/start')
async def instruction(call: types.CallbackQuery):
    user=User(call)
    await user.try_call_answer(obj=call, text="🏠", show_alert=False)
    await user.starts(call.message)

@dp.callback_query_handler(lambda call: call.data=='/help')
async def instruction(call: types.CallbackQuery):
    user=User(call)
    pass

@dp.callback_query_handler(lambda call: call.data=='/fun_weather')
async def instruction(call: types.CallbackQuery):
    user=User(call)
    await user.fun_weather(call)

@dp.callback_query_handler(lambda call: call.data=='/fun_exchange' or call.data=='/change_pair')
async def instruction(call: types.CallbackQuery):
    user=User(call)
    await user.fun_exchange(call)

@dp.callback_query_handler(lambda call: call.data=='/fun_animal')
async def instruction(call: types.CallbackQuery):
    user=User(call)
    await user.try_call_answer(obj=call, text="🤗", show_alert=False)
    await user.cute_animal(call.message)

@dp.callback_query_handler(lambda call: call.data=='/fun_poll')
async def instruction(call: types.CallbackQuery):
    user=User(call)
    await user.try_call_answer(obj=call, text="📝", show_alert=False)
    await user.create_poll(call.message)

@dp.callback_query_handler(lambda call: call.data[:9]=='/city_id_')
async def callback_inline(call):
    user=User(call.from_user.id)
    await user.try_call_answer(obj=call, text="⏳", show_alert=False)
    await user.weather_city_id(call)

@dp.callback_query_handler(lambda call: call.data in ['/usd_rub', '/rub_usd', '/eur_rub', '/rub_eur'])
async def callback_inline(call):
    user=User(call.from_user.id)
    await user.pre_exchange_input(call)

# __________________________________LOCATION____________________________________
@dp.message_handler(content_types='location')
async def telephone(message: types.Message):
    user=User(message)
    await user.weather_location(message)

# __________________________________POOL____________________________________
@dp.message_handler(content_types=["poll"])
async def telephone(message: types.Message):
    p=message.poll
    await bot.send_poll(chat_id=GROUP_ID, 
                        question=p.question, 
                        options=[x.text for x in p.options], 
                        is_anonymous=p.is_anonymous, 
                        type=p.type, 
                        allows_multiple_answers=p.allows_multiple_answers, 
                        correct_option_id=p.correct_option_id, 
                        explanation=p.explanation, 
                        explanation_entities=p.explanation_entities, 
                        open_period=p.open_period, 
                        close_date=p.close_date)