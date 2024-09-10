from python_weather.forecast import Forecast
from dict_images import dict_images


class CustomWeather:

    def __init__(self, weather: Forecast) -> None:
        self.weather: Forecast = weather
        self.img: str = dict_images[weather.description]

    def __getattr__(self, item):
        return self.weather.__getattribute__(item)
