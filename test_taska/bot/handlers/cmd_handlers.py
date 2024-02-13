from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

import bot.keyboards.user_keyboards as ikb
import bot.texts.user_texts as txt

router = Router()

@router.message(Command("start"))
async def cmd_start(msg: Message):
    reply_text=txt.start.format(name=msg.from_user.first_name)
    await msg.answer(
        text=reply_text,
        reply_markup=ikb.get_start_ikb()
    )

@router.message(Command("help"))
async def cmd_help(msg: Message):
    reply_text=txt.help
    await msg.answer(
        text=reply_text,
        reply_markup=ikb.get_home_ikb()
    )