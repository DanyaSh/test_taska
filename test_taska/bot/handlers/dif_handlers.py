from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from bot.utils.states import Weather, Exchange
import bot.utils.weather as weather_api
import bot.utils.exchange as exchange_api
import bot.keyboards.ikb_keyboards as ikb
import bot.texts.user_texts as txt

router = Router()

@router.message(F.sticker)
async def message_with_sticker(msg: Message):
    await msg.answer("Это стикер!")

@router.message(F.animation)
async def message_with_gif(msg: Message):
    await msg.answer("Это GIF!")

@router.message(Weather.city_prompt, F.location)
async def answer_weather_location(msg: Message, state: FSMContext):
    lat = msg.location.latitude
    lon = msg.location.longitude
    reply_text = await weather_api.get_weather_via_location(lat=lat, lon=lon)
    await state.clear()
    await msg.answer(text=reply_text, reply_markup=ikb.get_home_ikb())

@router.message(Weather.city_prompt, F.text)
async def answer_weather_city(msg: Message, state: FSMContext):
    reply_ikb = ikb.get_cities_ikb(text=msg.text)
    reply_text=txt.choice_city.format(text=msg.text)
    await msg.answer(text=reply_text, reply_markup=reply_ikb)

@router.message(Exchange.first_prompt, F.text)
async def exchange_input(msg: Message, state: FSMContext):
    first_prompt=msg.text[:3].upper()
    second_prompt=msg.text[4:].upper()
    await state.update_data(
        first_prompt = first_prompt,
        second_prompt = second_prompt
    )
    await state.set_state(Exchange.value_prompt)
    reply_text=txt.exchange_input.format(
        name=msg.from_user.first_name,
        first=first_prompt,
        second=second_prompt
    )
    await msg.answer(text=reply_text)

@router.message(Exchange.value_prompt, F.text)
async def answer_exchange(msg: Message, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    first = data['first_prompt']
    second = data['second_prompt']
    value = float(''.join(msg.text.split(" ")))
    rates = await exchange_api.get_rate(
        first = first,
        second = second
    )
    reply_text = txt.exchange_output.format(
        first  = first,
        second = second,
        value  = value,
        answer = value * rates
    )
    await msg.answer(text=reply_text, reply_markup=ikb.get_home_ikb())

@router.message(F.text)
async def message_with_text(msg: Message):
    await msg.answer("Это текстовое сообщение!")