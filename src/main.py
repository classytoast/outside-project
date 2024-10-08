import logging

import config
from app import main_app
import views  # noqa
from logger import configure_logging


def run():
    """Запуск сервера и всех приложений"""
    main_app.run(debug=config.DEBUG, host='0.0.0.0')


if __name__ == '__main__':
    configure_logging(level=logging.INFO)
    run()
