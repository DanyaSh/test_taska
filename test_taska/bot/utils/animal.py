from .api_utils import get_request

async def generate_image() -> str:
    """Generate cute animal img
    """ 
    dog_url = "https://random.dog/woof.json"
    cat_404 = "https://img.freepik.com/premium-vector/404-error-web-page-template-with-cute-cat_540634-1.jpg?w=826"
    data = await get_request(url=dog_url, descr='cute animal')
    return data['url'] if data else cat_404