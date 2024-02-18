import json
import aiohttp

async def get_request(url, descr='get_request') -> dict:
    """Get_request
    """
    try:
        # raise ValueError(f"Imitation error for {descr}")
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                return data
    except Exception as e:
        print(f"🔴Error upload data for {descr}: {e}")