import json
import aiohttp

async def generate_image() -> str:
    """Generate cute animal img
    """ 
    cute_animal_url = "https://random.dog/woof.json"
    cat_404 = "https://img.freepik.com/premium-vector/404-error-web-page-template-with-cute-cat_540634-1.jpg?w=826"
    try:
        # raise ValueError("Imitation error")
        async with aiohttp.ClientSession()as session:
            async with session.get(cute_animal_url) as response:
                data = await response.json()
                return data['url']
    except Exception as e:
        print(f"🔴Error upload cute_animal: {e}")
        return cat_404