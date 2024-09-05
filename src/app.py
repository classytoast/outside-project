from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import SECRET_KEY, DATABASE_URI


main_app = Flask(__name__)
main_app.config['SECRET_KEY'] = SECRET_KEY
main_app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(main_app)
