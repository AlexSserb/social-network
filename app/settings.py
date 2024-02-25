import os
from dotenv import load_dotenv


load_dotenv()

DATABASE_ADDRESS = os.getenv('DATABASE_ADDRESS')
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
SECRET_KEY = os.getenv('SECRET_KEY')
SESSION_REDIS = os.getenv('SESSION_REDIS')
