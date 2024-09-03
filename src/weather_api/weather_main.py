import asyncio
import os

from aiohttp import ClientConnectorError
from python_weather.forecast import Forecast
import python_weather
from python_weather import Locale
from logger import log


async def getweather(location: str) -> Forecast:
    """
    Получить через API данные по погоде в указанной локации
    :return: объект с данными о погоде
    """
    async with python_weather.Client(locale=Locale.RUSSIAN) as client:
        weather: Forecast = await client.get(location)

        # returns the current day's forecast temperature (int)
        # print(weather.temperature)
        # print(weather.coordinates)
        # for daily in weather.daily_forecasts:
        #     print(daily)
        #
        #     for hourly in daily.hourly_forecasts:
        #         print(f' --> {hourly!r}')

        return weather


def run_getweather(location: str) -> Forecast | None:
    """
    Запуск асинхронной функции для получения данных через API
    по погоде в укаазанной локации

    :return: объект с данными о погоде или None, если не удалось подключиться
    """
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    try:
        weather = asyncio.run(getweather(location))
    except ClientConnectorError:
        weather = None
        log.warning('Произошла ошибка подключения к сервису погоды')

    return weather


if __name__ == '__main__':
    res = run_getweather('москва')
    print(res)
