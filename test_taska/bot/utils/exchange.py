import os
from dotenv import load_dotenv, find_dotenv
from .api_utils import get_request

load_dotenv(find_dotenv())
token_exchange = os.getenv('TOKEN_EXCHANGE')

async def get_rate(first, second) -> str:
    """Get rate 
    """
    exchange_call = f"https://v6.exchangerate-api.com/v6/{token_exchange}/latest/{first}"
    data = await get_request(url=exchange_call, descr='exchange')
    return data['conversion_rates'][second]