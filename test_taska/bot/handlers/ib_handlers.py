from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from bot.utils.states import Gen
import bot.keyboards.ikb_keyboards as ikb 
import bot.keyboards.kb_keyboards as kb 
import bot.texts.user_texts as txt
import bot.utils.weather as weather_api
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
    await state.set_state(Gen.city_prompt)
    reply_text=txt.city.format(name=clbck.from_user.first_name)
    await clbck.message.answer(
        text=reply_text,
        reply_markup=kb.get_location_kb()
    )

@router.callback_query(Gen.city_prompt, F.data[:9] == "/city_id_")
async def fun_city_id(clbck: CallbackQuery, state: FSMContext):
    await clbck.answer(text='⏳', show_alert=False)
    await state.clear()
    city_id=clbck.data[9:]
    reply_text = await weather_api.get_weather_via_city(city_id)
    await clbck.message.answer(
        text=reply_text,
        reply_markup=ikb.get_home_ikb()
    )

@router.callback_query(F.data== "/fun_animal")
async def fun_animal(clbck: CallbackQuery):
    await clbck.answer(text='🐱', show_alert=False)
    link = await dog_api.generate_image()
    await clbck.message.answer_photo(
        photo=link, 
        reply_markup=ikb.get_home_ikb()
        )
