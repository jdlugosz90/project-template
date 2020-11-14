"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 2.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from . import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Allows React to make cross-site HTTP requests
    'corsheaders',
    # Allows communication between React & Django
    'rest_framework',
    # Package that provides token based authentication
    'rest_framework.authtoken',
    # Needed to rotate JWT refresh tokens and blacklist the old ones
    'rest_framework_simplejwt.token_blacklist',
    # Package to provide SPA endpoints
    'djoser',
    #Project apps
    'accounts',
]

MIDDLEWARE = [

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # ^^^ Allows React to make cross-site HTTP requests ^^^
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Use this for the frontend build
        # 'DIRS': [os.path.join(BASE_DIR, 'build')], 
        'DIRS': [],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


# --------- ADDITIONAL SETTINGS NOT INCLUDED BY DEFUALT --------

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'build/static')
]

# Location to the static root folder. STATIC_URL  is just the url to this folder
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000'
]
# Provides token & JWT based authentication
REST_FRAMEWORK = {
    #All views by default require user to be authenticated
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        
    ),
}

# Configure django-rest-framework-simplejwt to use the 
# Authorization: JWT <access_token> header:
SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
   'ROTATE_REFRESH_TOKENS': True,
   'BLACKLIST_AFTER_ROTATION': True,
}

# Djoser optional settings
DJOSER = {
    # Tells djoser we are using email authentication
    'LOGIN_FIELD': 'email',
    # User has to confirm password
    'USER_CREATE_PASSWORD_RETYPE': True,
    # If True, change username endpoints will send confirmation email to user.
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    # If True, change password endpoints will send confirmation email to user.
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    # If True, register or activation endpoint will send confirmation email to user.
    'SEND_CONFIRMATION_EMAIL': True,
    # If True, you need to pass re_new_password to /users/set_password/ endpoint, to validate password equality.
    'SET_PASSWORD_RETYPE': True,
    # URL to your frontend password reset page. It should contain {uid} and {token} placeholders, e.g. #/password-reset/{uid}/{token}. You should pass uid and token to reset password confirmation endpoint.
    # THIS IS REQUIRED
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
    # The link the user receives in the email
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {
        'user_create': 'accounts.serializers.UserCreateSerializer',
        'user': 'accounts.serializers.UserCreateSerializer',
        'user_delete': 'accounts.serializers.UserDeleteSerializer',
    }

}

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = config.EMAIL_HOST
EMAIL_HOST_USER = config.EMAIL_USR
EMAIL_HOST_PASSWORD = config.EMAIL_PSD
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'default from email'

# Tells django to use this custom user model defined in accounts
AUTH_USER_MODEL = 'accounts.UserAccount'