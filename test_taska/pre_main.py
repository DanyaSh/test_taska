from aiogram import Bot, Dispatcher
from aiogram.utils.chat_action import ChatActionMiddleware
from bot.handlers import cmd_handlers, ib_handlers, txt_handlers, dif_handlers
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
TOKEN_BOT  = os.getenv('TOKEN_BOT')
LIST_ADMIN = os.getenv('LIST_ADMIN')
list_admin=LIST_ADMIN.split(',')

bot = Bot(token=TOKEN_BOT, parse_mode="HTML")
dp = Dispatcher()

dp.include_routers(
    cmd_handlers.router,
    ib_handlers.router,
    txt_handlers.router,
    dif_handlers.router
)
dp.message.middleware(ChatActionMiddleware())

async def startup_fun():
    for x in list_admin:
        await bot.send_message(chat_id=x, text='✅startup')

async def shutdown_fun():
    for x in list_admin:
        await bot.send_message(chat_id=x, text='♨️shutdown')
