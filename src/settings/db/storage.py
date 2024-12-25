"""
Database connection
"""
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

from src.settings import default
from src.settings.external.environs import env

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mydatabase",
    }
}

if default.APP_ENV == 'development':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            "NAME": "mydatabase",
        }
    }


if default.APP_ENV == 'production':
    DATABASES = {
        "default": {
            "ENGINE": env.str("DB_ENGINE"),
            "NAME": env.str("DB_NAME"),
            "USER": env.str("DB_USERNAME"),
            "PASSWORD": env.str("DB_PASSWORD"),
            "HOST": env.str("DB_HOST"),
            "PORT": env.int("DB_PORT"),
        }
    }
