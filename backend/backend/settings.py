"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import firebase_admin
from firebase_admin import credentials

def getPath():
    #return Path(r'/mnt/c/Users/mli00/Desktop/Purdue/ECE 49595O/Boilermate-b3fcd-firebase-adminsdk-rwh4i-30e3b04f5c.json') # subject to change
    return Path(r'C:\Users\andre\Documents\boilermate.json') # subject to change

path = getPath()
cred = credentials.Certificate(path)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://boilermate-b3fcd-default-rtdb.firebaseio.com'
})

TIME_ZONE = 'UTC'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)($s&&en#j9+9r^mv5qq)hb)h&+@i(4-2tk_zn64@h())wcku8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['http://127.0.0.1:8000/', 'http://127.0.0.1:8000/firebase/parse-and-send', 'http://127.0.0.1:8000/firebase/call-api-view', 'http://127.0.0.1:8000/admin/']

ALLOWED_HOSTS = ["*"] # add firebase in here later

CORS_ORIGIN_WHITELIST = [
    'http://100.64.134.204:19000'
]

# Application definition

# REST_FRAMEWORK = {
#     'DEFAULT_THROTTLE_CLASSES': [
#         'boilermate_app.throttling.FirebaseThrottle',
#     ],
#     'DEFAULT_THROTTLE_RATES': {
#         'firebase_request': '150/second',
#     }
# }

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'corsheaders',
    'django.contrib.staticfiles',
    'django.core.management',
    'rest_framework',
    'firebase_api',
    'googlesearch',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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
            ],
        },
    },
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_ALLOW = True
CORS_ALLOW_ALL_ORIGINS = True

WSGI_APPLICATION = 'backend.wsgi.application'

YOUTUBE_API_KEY = 'AIzaSyBCWCmdRqhjI6LcZdwNtQEKbBqgbl18eqU'

OPENAI_API_KEY = 'sk-proj-GbBBhDQutQQcZtbn1SCRT3BlbkFJmZf2WyNOXxzcpJ4D6Mif'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'