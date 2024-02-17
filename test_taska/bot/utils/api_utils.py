import os
from dotenv import load_dotenv, find_dotenv
import json
import aiohttp

load_dotenv(find_dotenv())
token_weather = os.getenv('TOKEN_WEATHER')

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

def prepare_weather_data(d) -> str:
    """Prepare data from json to reply text for answer in telegram
    """
    icon = {'01d':'☀️', '01n':'🌙', '02d':'🌤', '02n':'🌤', '03d':'🌥', '03n':'🌥', '04d':'☁️', '04n':'☁️', '09d':'🌧', '09n':'🌧', '10d':'🌦', '10n':'🌦', '11d':'⛈', '11n':'⛈', '13d':'❄️', '13n':'❄️', '50n':'🌫', '50d':'🌫'}
    country = {'RU':'🇷🇺', 'US':'🇺🇸', 'GB':'🇬🇧', 'UA':'🇺🇦', 'TR':'🇹🇷', 'SE':'🇸🇪', 'ES':'🇪🇸', 'KR':'🇰🇷', 'PE':'🇵🇪', 'IT':'🇮🇹', 'IL':'🇮🇱', 'DE':'🇩🇪', 'GE':'🇬🇪', 'FR':'🇫🇷', 'AR':'🇦🇷', 'BR':'🇧🇷', 'CN':'🇨🇳', 'CA':'🇨🇦'}
    answer = f"{country[d['sys']['country']]} {d['name']}\n"
    answer+= f"{icon[d['weather'][0]['icon']]} {d['main']['temp']}°C feels like {d['main']['feels_like']}°C"
    return answer

async def get_weather(url) -> str:
    """Get data from OpenWeather
    """
    try:
        # raise ValueError("Imitation error inside get weather")
        async with aiohttp.ClientSession()as session:
            async with session.get(url) as response:
                data = await response.json()
                return prepare_weather_data(data)
    except Exception as e:
        print(f"🔴Error upload data from openweather: {e}")

async def get_weather_via_location(lat, lon) -> str:
    """Get weather data from open weather via location
    """
    weather_call = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={token_weather}&units=metric"
    return await get_weather(weather_call)

async def get_weather_via_city(city_id) -> str:
    """Get weather data from open weather via city
    """
    weather_call = f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={token_weather}&units=metric"
    return await get_weather(weather_call)