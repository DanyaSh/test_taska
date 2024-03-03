from aiogram import Bot, Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from bot.utils.states import Weather
import bot.utils.weather as weather_api
import bot.keyboards.ikb_keyboards as ikb
import bot.texts.user_texts as txt
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
GROUP_ID = os.getenv('GROUP_ID')
TOKEN_BOT=os.getenv('TOKEN_BOT')

bot=Bot(token=TOKEN_BOT, parse_mode="HTML")

router = Router()

@router.message(F.sticker)
async def message_with_sticker(msg: Message):
    await msg.answer(text=txt.sticker)

@router.message(F.animation)
async def message_with_gif(msg: Message):
    await msg.answer(txt.animation)

@router.message(Weather.city_prompt, F.location)
async def answer_weather_location(msg: Message, state: FSMContext):
    lat = msg.location.latitude
    lon = msg.location.longitude
    reply_text = await weather_api.get_weather_via_location(lat=lat, lon=lon)
    await state.clear()
    await msg.answer(text=reply_text, reply_markup=ikb.get_home_ikb())

@router.message(F.poll)
async def forward_poll(msg: Message):
    p=msg.poll
    await bot.send_poll(
        chat_id=GROUP_ID,
        question=p.question, 
        options=[x.text for x in p.options], 
        is_anonymous=p.is_anonymous, 
        type=p.type, 
        allows_multiple_answers=p.allows_multiple_answers, 
        correct_option_id=p.correct_option_id, 
        explanation=p.explanation, 
        explanation_entities=p.explanation_entities, 
        open_period=p.open_period, 
        close_date=p.close_date
    ) 