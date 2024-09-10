import asyncio
import os
from collections import Counter

from aiohttp import ClientConnectorError
from python_weather.forecast import Forecast
import python_weather
from python_weather import Locale
from logger import log
from weather_api.custom_forecast_classes import CustomWeather
from dict_images import dict_images


async def getweather(location: str) -> Forecast:
    """
    Получить через API данные по погоде в указанной локации
    :return: объект с данными о погоде
    """
    async with python_weather.Client(locale=Locale.RUSSIAN) as client:
        weather: Forecast = await client.get(location)

        return weather


def run_getweather(location: str) -> tuple[CustomWeather | None, dict]:
    """
    Запуск асинхронной функции для получения данных через API
    по погоде в укаазанной локации

    :return: 1) объект с данными о погоде или None, если не удалось подключиться,
             2) словарь с данными о погоде в разрезе дней
    """
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    daily_data: dict = {}

    try:
        weather = asyncio.run(getweather(location))
        for daily in weather.daily_forecasts:
            daily_description = Counter(
                [h.description for h in daily.hourly_forecasts]
            ).most_common()[0][0]
            daily_data[daily.date] = {
                'description': daily_description,
                'hours_data': daily.hourly_forecasts,
                'max_temp': daily.highest_temperature,
                'min_temp': daily.lowest_temperature,
                'img': dict_images[daily_description]
            }

    except ClientConnectorError:
        weather = None
        log.warning('Произошла ошибка подключения к сервису погоды')

    return CustomWeather(weather), daily_data


if __name__ == '__main__':
    res = run_getweather('москва')
    print(res[0].description)
