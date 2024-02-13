import settings
import redis
from datetime import timedelta
import os

class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = settings.SECRET_KEY

    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}' + \
        f'@{settings.DATABASE_ADDRESS}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}'
    )

    SESSION_TYPE = 'redis'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.from_url(settings.SESSION_REDIS)
    PERMANENT_SESSION_LIFETIME = timedelta(days=3)

    UPLOAD_FOLDER = os.path.join('static', 'images')
