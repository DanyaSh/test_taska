from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from bot.utils.states import Gen
import bot.utils.api_utils as utl
import bot.keyboards.ikb_keyboards as ikb
import bot.texts.user_texts as txt

router = Router()

@router.message(F.sticker)
async def message_with_sticker(msg: Message):
    await msg.answer("Это стикер!")

@router.message(F.animation)
async def message_with_gif(msg: Message):
    await msg.answer("Это GIF!")

@router.message(Gen.city_prompt, F.location)
async def answer_weather(msg: Message, state: FSMContext):
    lat = msg.location.latitude
    lon = msg.location.longitude
    reply_text = await utl.get_weather_via_location(lat=lat, lon=lon)
    await state.clear()
    await msg.answer(text=reply_text)

@router.message(Gen.city_prompt, F.text)
async def answer_weather(msg: Message, state: FSMContext):
    reply_ikb = ikb.get_cities_ikb(text=msg.text)
    reply_text=txt.choice_city.format(text=msg.text)
    await msg.answer(text=reply_text, reply_markup=reply_ikb)

@router.message(F.text)
async def message_with_text(msg: Message):
    await msg.answer("Это текстовое сообщение!")