from functools import wraps
from typing import Callable, Any

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
def create_user(name: str, email: str, psw: str) -> str:
    """Добавить нового пользователя в БД"""
    new_user = m.Users(
        name=name,
        email=email,
        psw=psw
    )
    db.session.add(new_user)
    db.session.commit()

    return 'success'
