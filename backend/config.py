from os import path, environ
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


SECRET_KEY = environ.get("SECRET_KEY") or "hard to guess string"
DEBUG = True
MYSQL_HOST = environ.get("MYSQL_HOST")
MYSQL_USER = environ.get("MYSQL_USER")
MYSQL_PASSWORD = environ.get("MYSQL_PASSWORD")
MYSQL_DATABASE = environ.get("MYSQL_DATABASE")