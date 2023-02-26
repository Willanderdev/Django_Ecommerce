"""
Django settings for djangoecommerce project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from dotenv import load_dotenv
from pathlib import Path
import dj_database_url
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', '0').lower() in ['true', 't', '1']

ALLOWED_HOSTS = ['ecommerce-ugu7.onrender.com']

    

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'paypal.standard.ipn',
    'easy_thumbnails',
    'whitenoise.runserver_nostatic',
    'watson',

    'core',
    'catalog',
    'bootstrap5',
    'accounts',
    'checkout',

]

# csrf pra deploy na Railway
CSRF_TRUSTED_ORIGINS = [
    'https://web-production-4d4b.up.railway.app']


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'checkout.middleware.cart_item_middleware',
]


ROOT_URLCONF = 'djangoecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'catalog.context_processors.categories',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# configuração do postgresql pra deploy no Railway
# postgresql://postgres: NTq081M1EtDH826OuhEo@containers-us-west-68.railway.app: 6519/railway
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'railway',
#         'USER': 'postgres',
#         'PASSWORD': 'NTq081M1EtDH826OuhEo',
#         'HOST': 'containers-us-west-68.railway.app',
#         'PORT': '6519',
#     }
# }

# configuração Postgrsql local(desenvolvimento)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'Port-Ecommerce',
#         'USER': 'postgres',
#         'PASSWORD': 'Tr4der2404',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# set é pra setar a variave de ambiente DATABASE_URL
# set DATABASE_URL = postgres://ecommerce_nnmm_user:xYRpA73nlbKvQBawRplpYkX7bDcvko1G@dpg-cfbrm5kgqg4aqevg6000-a/ecommerce_nnmm

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'), conn_max_age=600),
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'
    

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'




# Email
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# login redirect
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'
AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.ModelBackend',
)
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

PAYPAL_TEST = True
PAYPAL_EMAIL = 'willanderguitar@hotmail.com'

# thumbnails configuração pra corte de imagens
THUMBNAIL_ALIASES = {
    '': {
        'prod_image': {'size': (285, 160), 'crop': True},
    },
}


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# configurações dos pictures
# PICTURES = {
#     "BREAKPOINTS": {
#         "xs": 576,
#         "s": 768,
#         "m": 992,
#         "l": 1200,
#         "xl": 1400,
#     },
#     "GRID_COLUMNS": 12,
#     "CONTAINER_WIDTH": 1200,
#     "FILE_TYPES": ["WEBP"],
#     "PIXEL_DENSITIES": [1, 2],
# }

# pra carregar os rquivos static no railway é preciso adcionar o whitenoise nos middleware... instalar o whitnoise e coletar os arquivos statics
