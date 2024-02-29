import logging
import sys
import asyncio
from pre_main import dp, bot, startup_fun, shutdown_fun


async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await startup_fun()
    
    try:
        await dp.start_polling(bot)
    except Exception as _ex:
        print(f"🔴Error -> {_ex}")
    finally:
        await shutdown_fun()


if __name__== "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())