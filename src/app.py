from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from config import SECRET_KEY, DATABASE_URI, MAIL_USERNAME, MAIL_DEFAULT_SENDER, MAIL_PASSWORD

main_app = Flask(__name__)
main_app.config['SECRET_KEY'] = SECRET_KEY
main_app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
main_app.config['MAIL_SERVER'] = 'smtp.yandex.ru'
main_app.config['MAIL_PORT'] = 465
main_app.config['MAIL_USE_SSL'] = True
main_app.config['MAIL_USERNAME'] = MAIL_USERNAME
main_app.config['MAIL_DEFAULT_SENDER'] = MAIL_DEFAULT_SENDER
main_app.config['MAIL_PASSWORD'] = MAIL_PASSWORD

db = SQLAlchemy(main_app)

login_manager = LoginManager(main_app)
login_manager.login_view = 'login'
login_manager.login_message = "Авторизуйтесь для доступа к закрытым страницам"
login_manager.login_message_category = "success"

mail = Mail(main_app)
