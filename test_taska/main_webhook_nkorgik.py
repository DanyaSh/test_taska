from aiogram import Bot, Dispatcher, types
from aiohttp import web

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
token = os.getenv('TOKEN_BOT')

bot = Bot(token=token)
Bot.set_current(bot)

dp = Dispatcher(bot)
app = web.Application()

webhook_path = f"/{token}"
url = "https://example.com"

async def set_webhook():
    webhook_uri = f"{url}{webhook_path}"
    await bot.set_webhook(webhook_uri)

async def on_startup(_):
    pass

async def handle_webhook(request):
    url = str(request.url)
    index = url.rfind('/')
    token_input = url[index+1:]

    if token_input == token:
        request_data = await request.json()
        update = types.Update(**request_data)

        await dp.process_update(update)

        return web.Response()
    else:
        return web.Response(status=403)

app.router.add_post(f"/{token}", handle_webhook)

if __name__ == "__main__":
    app.on_startup.append(on_startup)

    web.run_app(
        app,
        host="0.0.0.0",
        port=8080
    )