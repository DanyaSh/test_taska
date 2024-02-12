from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram import flags
from aiogram.fsm.context import FSMContext
import json
from urllib.request import urlopen

from bot.keyboards.user_keyboards import get_home_ikb, get_start_ikb

router = Router()

@router.callback_query(F.data== "/start")
# @flags.chat_action("upload_photo")
async def fun_home(clbck: CallbackQuery, state: FSMContext):
    await clbck.answer(text='🏠', show_alert=False)
    reply_text = f"👋 Hi {clbck.from_user.first_name}!\n"
    reply_text += f"What do you want❓"
    await clbck.message.answer(
        text=reply_text,
        reply_markup=get_start_ikb()
    )

@router.callback_query(F.data== "/fun_animal")
# @flags.chat_action("upload_photo")
async def fun_animal(clbck: CallbackQuery, state: FSMContext):
    await clbck.answer(text='🐱', show_alert=False)
    # await clbck.message.answer(text='Тут будет милая фотка с животным')
    cute_animal = f"https://random.dog/woof.json"
    data = urlopen(cute_animal).read()
    d = json.loads(data)
    link=d['url']
    await clbck.message.answer_photo(photo=link, reply_markup=get_home_ikb())
    # await clbck.message.answer_photo(photo=link)
    

























#@router.callback_query(F.data == "generate_image")
#async def input_image_prompt(clbck: CallbackQuery, state: FSMContext):
#    await state.set_state(Gen.img_prompt)
#    await clbck.message.edit_text(text.gen_image)
#    await clbck.message.answer(text.gen_exit, reply_markup=kb.exit_kb)
#
#@router.message(Gen.img_prompt)
#@flags.chat_action("upload_photo")
#async def generate_image(msg: Message, state: FSMContext):
#    prompt = msg.text
#    mesg = await msg.answer(text.gen_wait)
#    img_res = await utils.generate_image(prompt)
#    if len(img_res) == 0:
#        return await mesg.edit_text(text.gen_error, reply_markup=kb.iexit_kb)