from app import db


class Users(db.Model):
    """Таблица зарегистрированных пользователей"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(100), nullable=False)
    subscriptions = db.relationship('Mailing', backref='user', cascade='all,delete-orphan')


class Mailing(db.Model):
    """Таблица рассылок на Email'ы"""
    __tablename__ = 'mailing'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    location = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    first_forecast_day = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer)
    last_forecast_day = db.Column(db.DateTime)
    is_no_time_limit = db.Column(db.Boolean, nullable=False)
