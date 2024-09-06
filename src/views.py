from datetime import date

from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash

from app import main_app
from forms import RegisterForm
from weather_api.weather_main import run_getweather
from weather_api.translate import description, wind
from db_queries import create_user


@main_app.route("/", methods=["POST", "GET"])
def main_view():
    """
    Главная страница сайта
    """
    if request.method == "POST":
        return redirect(
            url_for('forecast_view', location=request.form['city'])
        )

    return render_template(
        'main.html',
        title='Outside - узнай погоду'
    )


@main_app.route("/forecast/<location>/")
def forecast_view(location: str):
    """
    Страница данных о прогнозе, для переданного города
    """
    forecast_data, daily_data = run_getweather(location)

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

        date_today = daily_data[date.today()]

        return render_template(
            'forecast.html',
            title=f'{forecast_data.location}({forecast_data.country}): погода сейчас',
            loc=forecast_data,
            description=description_data,
            wind=wind_data,
            daily_data=daily_data,
            date_today=date_today
        )

    else:
        flash("Не найдено такого города, проверьте правильность ввода", "error")

    return redirect(url_for('main_view'))


@main_app.route("/about/")
def about():
    return render_template(
        'about.html',
        title='Коротко о сервисе погоды Outside'
    )


@main_app.route("/login/")
def login():
    pass


@main_app.route("/registry/", methods=["POST", "GET"])
def registry():
    """Страница регистрации на сайте"""
    form = RegisterForm()

    if form.validate_on_submit():
        hash_password = generate_password_hash(request.form['psw'])
        result = create_user(form.name.data, form.email.data, hash_password)

        if result == 'success':
            flash("регистрация прошла успешно", "success")
            return redirect(url_for('main_view'))
        else:
            flash("Ошибка при добавлении данных в БД", "error")

    return render_template(
        "register.html",
        title="Регистрация",
        form=form
    )
