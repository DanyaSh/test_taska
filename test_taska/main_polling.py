#from handlers import dp
#from aiogram import executor
#
#if __name__ == "__main__":
#    executor.start_polling(dp, skip_updates=True)

import asyncio
from aiogram import Bot, Dispatcher, types
import os
from dotenv import load_dotenv
from bot.handlers import user_handlers

#def register_handler(dp: Dispatcher) -> None:
#    register_user_handlers(dp)

async def main() -> None:
    """Entry point
    """
    load_dotenv('.env')
    
    token=os.getenv('TOKEN_BOT')
    bot=Bot(token=token, parse_mode="HTML")
    dp=Dispatcher()
    dp.include_routers(user_handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)

    try:
        await dp.start_polling(bot)
    except Exception as _ex:
        print(f"🔴Error -> {_ex}")

if __name__== "__main__":
    asyncio.run(main())