"""
Django settings for WEB project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path
import dj_database_url
import sys


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w*-q%j_b=xhvw323we-lpaoh$c3q-1r%zurc_0s)!*nv$%!@c-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tienda',
    'articulos',
    'contacto',
    'aatienda',
    'mayoristas',
    'blog',
    'carrito',
    'checkout',
]   

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    
]

ROOT_URLCONF = 'WEB.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'carrito.context_processor.monto_total',
            ],  
        },
    },
]

WSGI_APPLICATION = 'WEB.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
from decouple import config
DATABASES = {
    'default':dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es-eu'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_URL= '/media/'

MEDIA_ROOT =  os.path.join(BASE_DIR,'media')

Cliente_Id="AT57_peUjz_M_FNOHo5Qbmgc16ft_-9YLpFQy85W51RoBlmwuw5fNDkeOx9G7uOMr3CrIr04Mx2Vgm_I"
Cliente_Secret_Key="EM60643zxtyTJqzrvrYqRed4BPXlph7RdQDIhBJbAprmzC5NdZ0dwKFVqfa6Qp8xkmkrSFy69Q39ryJt"

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST= 'smtp.googlemail.com'
EMAIL_PORT= 587
EMAIL_HOST_USER = 'joyapanbackend@gmail.com'
EMAIL_HOST_PASSWORD = 'Rmpv54321'
EMAIL_USE_TLS=True
STRIPE_PUBLISHABLE_KEY ='pk_test_51IfVw7EoHQQLz8ZTPLwDGo3EY9nrWhEUI4aEiDqAiP1cZapE9pvp38BmRDIrLVsDfIZZjnvQVc1NKpt8NixbCkGC00ufXbNSA3'
STRIPE_SECRET_KEY = 'sk_test_51IfVw7EoHQQLz8ZTC41QPlFihvKvTBs9ez5HUdV1cYsCVm0UIJ65vPjQb1qpC3nLJGP652CYHz4wBoYzc0DqhTIk00kysXrKGC'
STRIPE_WEBHOOK_SECRET = ""
