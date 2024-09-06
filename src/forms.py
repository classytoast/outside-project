from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegisterForm(FlaskForm):
    """Форма регистрации на сайте"""
    name = StringField(
        "Имя: ",
        validators=[
            Length(min=4, max=50, message="Имя должно быть от 4 до 50 символов")
        ]
    )
    email = StringField(
        "Email: ",
        validators=[
            Email("Некорректный email")
        ]
    )
    psw = PasswordField(
        "Пароль: ",
        validators=[
            DataRequired(),
            Length(min=4, max=100, message="Пароль должен быть от 4 до 100 символов")
        ]
    )
    psw2 = PasswordField(
        "Повтор пароля: ",
        validators=[
            DataRequired(),
            EqualTo('psw', message="Пароли не совпадают")
        ]
    )

    submit = SubmitField("Регистрация")


class LoginForm(FlaskForm):
    """Форма авторизации на сайте"""
    email = StringField(
        "Email: ",
        validators=[
            Email("Некорректный email")
        ]
    )
    psw = PasswordField(
        "Пароль: ",
        validators=[
            DataRequired(),
            Length(min=4, max=100, message="Пароль должен быть от 4 до 100 символов")
        ]
    )

    remember = BooleanField("Запомнить", default=False)
    submit = SubmitField("Войти")
