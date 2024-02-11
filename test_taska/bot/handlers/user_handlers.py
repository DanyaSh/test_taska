#from aiogram import types, Dispatcher
#from bot.keyboards.user_keyboards import get_main_kb
#
#async def cmd_start(msg: types.Message) -> None:
#    """Command start
#
#    Args:
#        msg:(types.Message): msg object    
#    """
#    reply_text = f"Привет, как твои дела?\n"
#    reply_text += f"Твое имя - {msg.from_user.first_name}!"
#
#    await msg.answer(
#        text=reply_text,
#        reply_markup=get_main_kb()
#        )
#
#def register_user_handlers(dp: Dispatcher) -> None:
#    """Register user handlers
#    """
#    dp.register_message_handler(cmd_start, commands=['start'])

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from bot.keyboards.user_keyboards import get_main_kb

router = Router()  # [1]

@router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    reply_text = f"Привет, как твои дела?\n"
    reply_text += f"Твое имя - {message.from_user.first_name}!"
    await message.answer(
        text=reply_text,
        reply_markup=get_main_kb()
    )

#@router.message(F.text.lower() == "да")
#async def answer_yes(message: Message):
#    await message.answer(
#        "Это здорово!",
#        reply_markup=ReplyKeyboardRemove()
#    )
#
#@router.message(F.text.lower() == "нет")
#async def answer_no(message: Message):
#    await message.answer(
#        "Жаль...",
#        reply_markup=ReplyKeyboardRemove()
#    )