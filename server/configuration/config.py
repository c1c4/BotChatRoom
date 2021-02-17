from os import path, environ

from dotenv import load_dotenv

base_dir = path.abspath(path.dirname(__name__))
load_dotenv(path.join(base_dir, '.env'))


STOOQ_API = environ.get('STOOQ_API')
CHAT_USER = environ.get('CHAT_USER')
CHAT_PASS = environ.get('CHAT_PASS')
RABBIT_URL = environ.get('RABBIT_URL')
HOST = environ.get('HOST')
PORT = environ.get('PORT')

class Config:
    SECRET_KEY = environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
