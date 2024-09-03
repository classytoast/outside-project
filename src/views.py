from flask import render_template, request, redirect, url_for, flash
from python_weather.forecast import Forecast

from app import main_app
from weather_api.weather_main import run_getweather
from weather_api.translate import description, wind


@main_app.route("/", methods=["POST", "GET"])
def main_view():
    """
    Главная страница сайта
    """
    if request.method == "POST":
        return redirect(url_for('forecast_view', location=request.form['city']))

    return render_template('main.html',
                           title='Outside - узнай погоду')


@main_app.route("/forecast/<location>/")
def forecast_view(location: str):
    """
    Страница данных о прогнозе, для переданного города
    """
    forecast_data: Forecast | None = run_getweather(location)

    if forecast_data is None:
        flash("В данный момент наблюдаются проблемы с подключением к сервису погоды, попробуйте позже",
              "error")

    elif forecast_data.location != 'Ban Not':
        if forecast_data.description in description:
            description_data: str = description[forecast_data.description]
        else:
            description_data: str = forecast_data.description

        if str(forecast_data.wind_direction) in wind:
            wind_data: str = wind[str(forecast_data.wind_direction)]
        else:
            wind_data: str = str(forecast_data.wind_direction)

        return render_template('forecast.html',
                               title=f'{forecast_data.location}({forecast_data.country}): погода сейчас',
                               loc=forecast_data,
                               description=description_data,
                               wind=wind_data)

    else:
        flash("Не найдено такого города, проверьте правильность ввода", "error")

    return redirect(url_for('main_view'))


@main_app.route("/about/")
def about():
    pass


@main_app.route("/login/")
def login():
    pass


@main_app.route("/registry/")
def registry():
    pass
