from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from bot.utils.states import Weather
import bot.utils.weather as weather_api
import bot.keyboards.ikb_keyboards as ikb
import bot.texts.user_texts as txt

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