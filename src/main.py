import logging

from views import *
from logger import configure_logging


def run():
    """Запуск сервера и всех приложений"""
    main_app.run(debug=True, host='0.0.0.0')


if __name__ == '__main__':
    configure_logging(level=logging.INFO)
    run()
