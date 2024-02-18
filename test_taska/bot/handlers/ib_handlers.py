from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from bot.utils.states import Weather, Exchange
import bot.keyboards.ikb_keyboards as ikb 
import bot.keyboards.kb_keyboards as kb 
import bot.texts.user_texts as txt
import bot.utils.weather as weather_api
import bot.utils.exchange as exchange_api
import bot.utils.animal as dog_api

router = Router()

@router.callback_query(F.data== "/start")
async def fun_home(clbck: CallbackQuery):
    await clbck.answer(text='🏠', show_alert=False)
    reply_text=txt.start.format(name=clbck.from_user.first_name)
    await clbck.message.answer(
        text=reply_text,
        reply_markup=ikb.get_start_ikb()
    )

@router.callback_query(F.data== "/fun_weather")
async def fun_weather(clbck: CallbackQuery, state: FSMContext):
    await clbck.answer(text='⛅️', show_alert=False)
    await state.set_state(Weather.city_prompt)
    reply_text=txt.city.format(name=clbck.from_user.first_name)
    await clbck.message.answer(
        text=reply_text,
        reply_markup=kb.get_location_kb()
    )

@router.callback_query(Weather.city_prompt, F.data[:9] == "/city_id_")
async def fun_city_id(clbck: CallbackQuery, state: FSMContext):
    await clbck.answer(text='⏳', show_alert=False)
    await state.clear()
    city_id=clbck.data[9:]
    reply_text = await weather_api.get_weather_via_city(city_id)
    await clbck.message.answer(
        text=reply_text,
        reply_markup=ikb.get_home_ikb()
    )

@router.callback_query(F.data == "/fun_animal")
async def fun_animal(clbck: CallbackQuery):
    await clbck.answer(text='🐱', show_alert=False)
    link = await dog_api.generate_image()
    await clbck.message.answer_photo(
        photo=link, 
        reply_markup=ikb.get_home_ikb()
        )

@router.callback_query(F.data == "/fun_exchange")
async def fun_exchange(clbck: CallbackQuery, state: FSMContext):
    await clbck.answer(text="🏧", show_alert=False)
    await state.set_state(Exchange.first_prompt)
    reply_text=txt.exchange.format(name=clbck.from_user.first_name)
    await clbck.message.answer(
        text=reply_text,
        reply_markup=ikb.get_exchange_ikb()
    )

@router.callback_query(lambda f: f.data in ['/usd_rub', '/rub_usd', '/eur_rub', '/rub_eur'])
async def exchange_buttons(clbck: CallbackQuery, state: FSMContext):
    await clbck.answer(text="♻️", show_alert=False)
    first_prompt=clbck.data[1:4].upper()
    second_prompt=clbck.data[5:].upper()
    await state.update_data(
        first_prompt = first_prompt,
        second_prompt = second_prompt
    )
    await state.set_state(Exchange.value_prompt)
    reply_text=txt.exchange_input.format(
        name=clbck.from_user.first_name,
        first=first_prompt,
        second=second_prompt
    )
    await clbck.message.answer(text=reply_text)

@router.callback_query(F.data== "/fun_poll")
async def fun_poll(clbck: CallbackQuery):
    await clbck.answer(text='📝', show_alert=False)