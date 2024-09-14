from functools import wraps
from typing import Callable, Any

from sqlalchemy import and_

from app import db
import models as m
from logger import log


def decorator_exceptions(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            result: Any = func(*args, **kwargs)
            return result
        except Exception as e:
            log.error(f'Ошибка работы с БД - {e}')

    return wrapper


@decorator_exceptions
def create_user(name: str, email: str,
                psw: str, confirm_code: str) -> str:
    """Добавить нового пользователя в БД"""
    new_user = m.User(
        name=name,
        email=email,
        psw=psw,
        confirmation_code=confirm_code
    )
    db.session.add(new_user)
    db.session.commit()

    return 'success'


@decorator_exceptions
def get_user_by_id(user_id: int) -> m.User:
    """Получить данные о пользователе по его email
    :param user_id: id пользователя
    :return: запись о пользователе из БД
    """
    user = (
        db.session.query(
            m.User
        ).filter(
            m.User.id == user_id
        ).one()
    )
    return user


@decorator_exceptions
def get_user_by_email(email: str) -> m.User:
    """Получить данные о пользователе по его email
    :param email: email пользователя
    :return: запись о пользователе из БД
    """
    user = (
        db.session.query(
            m.User
        ).filter(
            m.User.email == email
        ).one()
    )
    return user


@decorator_exceptions
def get_user_by_confirm_code(code: str) -> m.User:
    """Получить данные о пользователе по его email
    :param code: code, который приходит пользователям на почту
    :return: запись о пользователе из БД
    """
    user = (
        db.session.query(
            m.User
        ).filter(
            and_(
                m.User.confirmation_code == code,
                m.User.is_confirmed.is_(False)
            )
        ).one()
    )
    return user


@decorator_exceptions
def confirm_email(user: m.User) -> None:
    """Подтвердить почту переданному пользователю"""
    user.is_confirmed = True
    db.session.commit()
