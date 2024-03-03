import logging
import sys
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from pre_main import dp, bot, startup_fun, shutdown_fun
from os import getenv
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
WEBHOOK_SECRET   = getenv('WEBHOOK_SECRET')
WEBHOOK_PATH     = getenv('WEBHOOK_PATH')
WEB_SERVER_HOST  = getenv('WEB_SERVER_HOST')
WEB_SERVER_PORT  = int(getenv('WEB_SERVER_PORT'))
BASE_WEBHOOK_URL = getenv("BASE_WEBHOOK_URL")


async def on_startup(bot: bot) -> None:
    await bot.set_webhook(f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}", secret_token=WEBHOOK_SECRET)
    await startup_fun()

async def on_shutdown(bot: bot) -> None:
    await shutdown_fun()

def main() -> None:
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=WEBHOOK_SECRET
    )
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main()
