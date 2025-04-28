import os

from dotenv import load_dotenv

load_dotenv()


class Secrets:
    def __init__(self):
        self.ENV = os.getenv('ENV', 'LOCAL')
        self.SECRET_KEY = os.getenv('SECRET_KEY')

        self.DB_NAME = os.getenv('DB_NAME', 'backoffice_db')
        self.DB_USER = os.getenv('DB_USER', 'user')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD', 'user')
        self.DB_HOST = os.getenv('DB_HOST', 'localhost')
        self.DB_PORT = os.getenv('PORT', '5432')
