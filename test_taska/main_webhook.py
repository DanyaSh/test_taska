import logging
import sys

from aiohttp.web import run_app
from aiohttp.web_app import Application
from routes import check_data_handler, demo_handler, send_message_handler

from aiogram import Bot, dp
from aiogram.types import MenuButtonWebApp, WebAppInfo
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from bot.handlers import cmd_handlers, ib_handlers, txt_handlers, dif_handlers

from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
TOKEN_BOT       = getenv('TOKEN_BOT')
WEBHOOK_SECRET  = getenv('WEBHOOK_SEKRET')
WEBHOOK_PATH    = getenv('WEBHOOK_PATH')
WEB_SERVER_HOST = getenv('WEB_SERVER_HOST')
WEB_SERVER_PORT = getenv('WEB_SERVER_PORT')
APP_BASE_URL    = getenv("APP_BASE_URL")

async def on_startup(bot: Bot, base_url: str):
    await bot.set_webhook(f"{base_url}/{WEBHOOK_PATH}")
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(text="Open Menu", web_app=WebAppInfo(url=f"{base_url}/demo"))
    )

def main() -> None:
    bot = Bot(token=TOKEN, parse_mode="HTML")
    dp = dp()
    dp["base_url"] = APP_BASE_URL
    dp.startup.register(on_startup)

    dp.include_routers(
        cmd_handlers.router,
        ib_handlers.router,
        txt_handlers.router,
        dif_handlers.router
    )
    
    app = Application()
    app["bot"] = bot

    app.router.add_get("/demo", demo_handler)
    app.router.add_post("/demo/checkData", check_data_handler)
    app.router.add_post("/demo/sendMessage", send_message_handler)
    SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    ).register(app, path=WEBHOOK_PATH)
    setup_application(app=app, dispatcher=dp, bot=bot)

    run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main()