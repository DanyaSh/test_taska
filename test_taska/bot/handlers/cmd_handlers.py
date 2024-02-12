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

from bot.keyboards.user_keyboards import get_start_ikb

router = Router()  # [1]

@router.message(Command("start"))  # [2]
async def cmd_start(msg: Message):
    reply_text = f"👋 Hi {msg.from_user.first_name}!\n"
    reply_text += f"What do you want❓"
    await msg.answer(
        text=reply_text,
        reply_markup=get_start_ikb()
    )