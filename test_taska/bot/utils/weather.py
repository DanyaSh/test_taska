import os
from dotenv import load_dotenv, find_dotenv
from .api_utils import get_request

load_dotenv(find_dotenv())
token_weather = os.getenv('TOKEN_WEATHER')

def prepare_weather_data(d) -> str:
    """Prepare data from json to reply text for answer in telegram
    """
    icon = {'01d':'☀️', '01n':'🌙', '02d':'🌤', '02n':'🌤', '03d':'🌥', '03n':'🌥', '04d':'☁️', '04n':'☁️', '09d':'🌧', '09n':'🌧', '10d':'🌦', '10n':'🌦', '11d':'⛈', '11n':'⛈', '13d':'❄️', '13n':'❄️', '50n':'🌫', '50d':'🌫'}
    country = {'RU':'🇷🇺', 'US':'🇺🇸', 'GB':'🇬🇧', 'UA':'🇺🇦', 'TR':'🇹🇷', 'SE':'🇸🇪', 'ES':'🇪🇸', 'KR':'🇰🇷', 'PE':'🇵🇪', 'IT':'🇮🇹', 'IL':'🇮🇱', 'DE':'🇩🇪', 'GE':'🇬🇪', 'FR':'🇫🇷', 'AR':'🇦🇷', 'BR':'🇧🇷', 'CN':'🇨🇳', 'CA':'🇨🇦'}
    answer = f"{country[d['sys']['country']]} {d['name']}\n"
    answer+= f"{icon[d['weather'][0]['icon']]} {d['main']['temp']}°C feels like {d['main']['feels_like']}°C"
    return answer

async def get_weather_via_location(lat, lon) -> str:
    """Get weather data from open weather via location
    """
    weather_call = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={token_weather}&units=metric"
    data = await get_request(url=weather_call, descr='OpenWeather_location')
    return prepare_weather_data(data)

async def get_weather_via_city(city_id) -> str:
    """Get weather data from open weather via city
    """
    weather_call = f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={token_weather}&units=metric"
    data = await get_request(url=weather_call, descr='OpenWeather_city_id')
    return prepare_weather_data(data)