from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text)
async def message_with_text(msg: Message):
    await msg.answer("Это текстовое сообщение!")

@router.message(F.sticker)
async def message_with_sticker(msg: Message):
    await msg.answer("Это стикер!")

@router.message(F.animation)
async def message_with_gif(msg: Message):
    await msg.answer("Это GIF!")