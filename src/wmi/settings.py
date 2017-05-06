"""
Django settings for wmi project.

Generated by 'django-admin startproject' using Django 1.10.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from wmi.settings_secret import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jm$hw2jg-q6=cxzirwcz=@gzv9c%_d5@$wp)c-ra_^^%0_^3as'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['ec2-35-167-98-158.us-west-2.compute.amazonaws.com', 'web-map-interface.geo-bias.com', 'www.web-map-interface.geo-bias.com', '172.31.27.194', '127.0.0.1']
#ALLOWED_HOSTS = ['172.31.27.194']

EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = 'adm.geobias@gmail.com'
#EMAIL_MAIN = 'adm.geobias@gmail.com'
EMAIL_HOST_PASSWORD = email_password
EMAIL_PORT = 587
EMAIL_USE_TLS = True



#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True


"""
How to send email 

from django.conf import settings
from django.core.mail import send_mail

send_mail("subject", "My app sends messages now. What are you doing for lunch?", settings.EMAIL_HOST_USER, ["jhartell@globalparametrics.com "], fail_silently = False)

"""

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin', # A place to manage data
    'django.contrib.auth', # Users
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'bootstrap3',

    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
  
    'maps',
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
  
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    
)

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
LOGIN_REDIRECT_URL = "/"

ACCOUNT_ADAPTER = 'maps.forms.email_adapter'

ALLOWED_DOMAIN = 'globalparametrics.com', 'wvi.org', 'vfi.org', 'gmail.com'

CRISPY_TEMPLATE_PACK = "bootstrap3"

ACCOUNT_SIGNUP_FORM_CLASS = 'maps.forms.SignupForm'

AUTH_USER_MODEL = 'auth.User'



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wmi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'wmi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'


AWS_ACCESS_KEY_ID = access_key
AWS_SECRET_ACCESS_KEY = secret_key
AWS_STORAGE_BUCKET_NAME = 'web-map-interface'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' #static files such as css.
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' #media uploads
S3_URL = '//%s.s3.amazonaws.com/' %AWS_STORAGE_BUCKET_NAME
MEDIA_URL = S3_URL + "media/"
STATIC_URL = S3_URL + "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")










