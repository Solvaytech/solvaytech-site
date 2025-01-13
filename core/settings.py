import os
from unipath import Path
# import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY','solvaytech_2024')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False)

# load production server from .env
# ALLOWED_HOSTS = [config('HOST_1'), config('HOST_2'), 'localhost', '127.0.0.1']

ALLOWED_HOSTS = ['*', 'https://solvaytech-web-p7f2t.ondigitalocean.app', 'https://solvaytech.com.tr', 'https://www.solvaytech.com.tr']
CSRF_1 = os.environ.get('CSRF_1', 'https://solvaytech.com.tr')
CSRF_2 = os.environ.get('CSRF_1', 'https://www.solvaytech.com.tr')
CSRF_TRUSTED_ORIGINS = [CSRF_1 , CSRF_2]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.home'  # Enable the inner home (home)
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "home"  # Route defined in home/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in home/urls.py
TEMPLATE_DIR = os.path.join(CORE_DIR, "apps/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'myvckinc',
#         'USER': 'myvckinc',
#         'PASSWORD':'57_QGqkzRqlVz8rdIj9sF9ouqrGP8idc',
#         'HOST':'horton.db.elephantsql.com',
#         'PORT':'5432',
#     },
#     'Contact': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'xazbkywb',
#         'USER': 'xazbkywb',
#         'PASSWORD':'WRX_I5IN_laUr-S4zI5v9-7C7pWvVoGu',
#         'HOST':'horton.db.elephantsql.com',
#         'PORT':'5432',
#     },
#     'oldContact': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'qmigfxxk',
#         'USER': 'qmigfxxk',
#         'PASSWORD':'MvIolHpk1ituXm9jtBSOxX223TQeXDIW',
#         'HOST':'mel.db.elephantsql.com',
#         'PORT':'5432',
#     },
#     'stajDB': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'akbyvhxr',
#         'USER': 'akbyvhxr',
#         'PASSWORD':'5Jpu7LskivfPx9kFa5pqB4E0q-0yTBEj',
#         'HOST':'trumpet.db.elephantsql.com',
#         'PORT':'5432',
#     },
# }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# STATIC_ROOT = [BASE_DIR, 'staticfiles']

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(CORE_DIR, 'apps/static'),
      
]


# django_heroku.settings(locals())


# Extra places for collectstatic to find static files.
#STATICFILES_DIRS = (
#    os.path.join(CORE_DIR, 'apps/static'),
#)
#############################################################
#############################################################

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = ''
# EMAIL_PORT = 
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'