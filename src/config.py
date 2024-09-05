import os

from dotenv import load_dotenv


load_dotenv()


SECRET_KEY = os.environ.get('SECRET_KEY')
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_DBNAME = os.environ.get('DB_DBNAME')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')

DATABASE_URI = f'postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DBNAME}'

DEBUG = os.environ.get('DEBUG', False) == 'True'
