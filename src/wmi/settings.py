"""
Django settings for wmi project.

Generated by 'django-admin startproject' using Django 1.10.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
#from wmi.settings_secret import *  #Dev only

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

#SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY'] #Production
#SECRET_KEY = secret_key #Dev only

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False #Production
#DEBUG = True #Dev only

ADMINS = [('Michael', 'adm.geobias@gmail.com')]

ALLOWED_HOSTS = ['ec2-52-38-83-227.us-west-2.compute.amazonaws.com', 'webmapinterface.com', 'www.webmapinterface.com', '172.31.35.202', '127.0.0.1']

EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = 'adm.geobias@gmail.com'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD'] #production
#EMAIL_HOST_PASSWORD = email_password #Dev only
EMAIL_PORT = 587
EMAIL_USE_TLS = True



#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True

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

ALLOWED_DOMAIN = 'globalparametrics.com', 'wvi.org', 'vfi.org'

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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'


AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID'] #Production
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY'] #Production
#AWS_ACCESS_KEY_ID = access_key #Dev
#AWS_SECRET_ACCESS_KEY = aws_secret_key #Dev
AWS_STORAGE_BUCKET_NAME = 'wmicopy'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' #static files such as css.
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' #media uploads
S3_URL = '//%s.s3.amazonaws.com/' %AWS_STORAGE_BUCKET_NAME
MEDIA_URL = S3_URL + "media/"
STATIC_URL = S3_URL + "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")










