from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram import flags

import bot.keyboards.user_keyboards as ikb 
import bot.texts.user_texts as txt
import bot.utils.api_utils as utl

# from bot.utils.states import Gen
# from aiogram.fsm.context import FSMContext

router = Router()

@router.callback_query(F.data== "/start")
async def fun_home(clbck: CallbackQuery):
    await clbck.answer(text='🏠', show_alert=False)
    reply_text=txt.start.format(name=clbck.from_user.first_name)
    await clbck.message.answer(
        text=reply_text,
        reply_markup=ikb.get_start_ikb()
    )

@router.callback_query(F.data== "/fun_animal")
async def fun_animal(clbck: CallbackQuery):
    await clbck.answer(text='🐱', show_alert=False)
    link = await utl.generate_image()
    await clbck.message.answer_photo(photo=link, reply_markup=ikb.get_home_ikb())