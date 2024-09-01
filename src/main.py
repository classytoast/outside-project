from views import *


def run():
    """Запуск сервера и всех приложений"""
    main_app.run(debug=True, host='0.0.0.0')


if __name__ == '__main__':
    run()
