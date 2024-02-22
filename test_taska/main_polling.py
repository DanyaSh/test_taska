#from handlers import dp
#from aiogram import executor
#
#if __name__ == "__main__":
#    executor.start_polling(dp, skip_updates=True)

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils.chat_action import ChatActionMiddleware
import os
from dotenv import load_dotenv, find_dotenv
from bot.handlers import cmd_handlers, ib_handlers, txt_handlers, dif_handlers

#def register_handler(dp: Dispatcher) -> None:
#    register_user_handlers(dp)

async def main() -> None:
    """Entry point
    """
    load_dotenv(find_dotenv())
    
    token_bot=os.getenv('TOKEN_BOT')
    bot=Bot(token=token_bot, parse_mode="HTML")
    dp=Dispatcher()
    dp.include_routers(
        cmd_handlers.router,
        ib_handlers.router,
        txt_handlers.router,
        dif_handlers.router
    )
    dp.message.middleware(ChatActionMiddleware()) # for flags typing, upload photo...
    await bot.delete_webhook(drop_pending_updates=True)

    try:
        await dp.start_polling(bot)
    except Exception as _ex:
        print(f"🔴Error -> {_ex}")

if __name__== "__main__":
    asyncio.run(main())