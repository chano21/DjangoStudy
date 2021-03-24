"""
Django settings for djangostudy project.
Generated by 'django-admin startproject' using Django 3.1.
For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

#import environ

import pymysql


# env = environ.Env(
#     # set casting, default value
#     DEBUG=(bool, False)
# )
# environ.Env.read_env()

# DEBUG = env("DEBUG")
DEBUG = True

# env = environ.Env

pymysql.install_as_MySQLdb()


pymysql.version_info = (1, 4, 0, "final", 0)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "i(#tpmus&8tk*nj+j8a1cgt!^w4+!kdb-@r!t%$x=($fa%==b0"


# SECURITY WARNING: don't run with debug turned on in production!

# ALLOWED_HOSTS = ['127.0.0.1','0.0.0.0','localhost']
ALLOWED_HOSTS = ["*"]

APPS = ["cafe", "board", "member", "comment"]
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "debug_toolbar",
    "django.contrib.staticfiles",
    "drf_yasg",
    "rest_framework",
    "django_celery_beat",
    "django_celery_results",
]

INSTALLED_APPS += APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "djangostudy.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "djangostudy.wsgi.application"

# JSON Render Settings

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ]
}

SWAGGER_SETTINGS = {}


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "djangostudy",  # DB명
        "USER": "root",
        "PASSWORD": "1234",  # 계정 비밀번호
        "HOST": "localhost",  # 데이테베이스 주소(IP)
        "PORT": "3306",  # 데이터베이스 포트(보통은 3306)
    }
}

# DATABASES = {"default": env.db()}
# CACHES = {"default": env.cache("REDIS_URL")}
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "devformat": {
            "format": "{levelname} {asctime} {module} {message} \n\n",
            "style": "{",
        },
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "devformat"},
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "api.logger": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": True,
        },
        "django.request": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
        "root": {"level": "INFO", "handlers": ["console"]},
    },
}


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_URL = "/static/"


DJANGO_SETTINGS_MODULE = "djangostudy.initialize.settings"
CELERY_ALWAYS_EAGER = True
CELERY_BROKER_URL = "redis://127.0.0.1:6379"
CELERY_RESULT_BACKEND = "mysql://root:1234@127.0.0.1:3306/djangostudy"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "Asia/Seoul"
DEBUG = True
REDIS_URL = "rediscache://127.0.0.1:6379/1?client_class=django_redis.client.DefaultClient&password=ungithubbed-secret"
DATABASE_URL = "mysql://root:1234@127.0.0.1:3306/djangostudy"


SCHEDULE_SECOND = 1
SCHEDULE_MINUTE = 60
SCHEDULE_HOUR = 60 * SCHEDULE_MINUTE
SCHEDULE_DAY = 24 * SCHEDULE_HOUR
SCHEDULE_WEEK = 7 * SCHEDULE_DAY
SCHEDULE_MONTH = 30 * SCHEDULE_DAY


# CELERY_ALWAYS_EAGER = True
# CELERY_BROKER_URL = env("CELERY_BROKER_URL")
# CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND")
# CELERY_ACCEPT_CONTENT = env("CELERY_ACCEPT_CONTENT")
# CELERY_TASK_SERIALIZER = env("CELERY_TASK_SERIALIZER")
# CELERY_RESULT_SERIALIZER = env("CELERY_RESULT_SERIALIZER")
# CELERY_TIMEZONE = env("CELERY_TIMEZONE")

# SCHEDULE_SECOND = 1
# SCHEDULE_MINUTE = 60
# SCHEDULE_HOUR = 60 * SCHEDULE_MINUTE
# SCHEDULE_DAY = 24 * SCHEDULE_HOUR
# SCHEDULE_WEEK = 7 * SCHEDULE_DAY
# SCHEDULE_MONTH = 30 * SCHEDULE_DAY
# CELERYBEAT_SCHEDULE = {"add": {"task": "member.tasks.add", "schedule": 5.0, "args": (4, 4)}}
