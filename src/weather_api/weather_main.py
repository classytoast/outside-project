import asyncio
import os

from python_weather.forecast import Forecast
import python_weather
from python_weather import Locale


async def getweather(location: str) -> Forecast:
    """
    Получить через API данные по погоде в укаазанной локации
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


def run_getweather(location: str) -> Forecast:
    """
    Запуск асинхронной функции для получения данных через API
    по погоде в укаазанной локации

    :return: объект с данными о погоде
    """
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    weather = asyncio.run(getweather(location))

    return weather


if __name__ == '__main__':
    # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    # for more details
    # if os.name == 'nt':
    #     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    #
    # asyncio.run(getweather('Moscow'))
    res = run_getweather('москва')
    print(res)
