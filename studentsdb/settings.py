from django.conf import global_settings
from db import DATABASES
"""
Django settings for studentsdb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

LANGUAGE_CODE='en'
MEDIA_URL='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j-wcrtozkd3_c9o(-#k7yqcbld&d)xgwcy#5$a1lo0mk!m#ikb'

TEMPLATE_CONTEXT_PROCESSORS = \
    global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    "django.core.context_processors.request",
    "studentsdb.context_processors.students_proc",
    "social.apps.django_app.context_processors.backends",
    "social.apps.django_app.context_processors.login_redirect",
    "students.context_processors.groups_processor",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

PORTAL_URL = 'http://localhost:8000'

LOGIN_URL = 'users:auth_login'
LOGOUT_URL = 'users:auth_logout'


CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Email settings

ADMIN_EMAIL = 'admin@studentsdb.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'vetal969696@gmail.com'
EMAIL_HOST_PASSWORD = '80639372656a'
EMAIL_USE_TLS = True
EMAIL_SSL = False



# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'students',
    'crispy_forms',
    'registration',
    'studentsdb',
    'django_coverage',
    'social.apps.django_app.default',
)

MIDDLEWARE_CLASSES = (
    'studentsdb.middleware.RequestTimeMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'studentsdb','templates'),
)

ROOT_URLCONF = 'studentsdb.urls'

WSGI_APPLICATION = 'studentsdb.wsgi.application'



AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'django.contrib.auth.backends.ModelBackend',
)



LOG_FILE = os.path.join(BASE_DIR,'studentsdb.log')

LOGGING = {
    'version':1,
    'disable_existing_loggers':True,
    'formatters':{
        'verbose':{
            'format':'%(levelname)s %(asctime)s %(module)s: %(message)s'
            },
        'simple':{
            'format':'%(levelname)s: %(message)s'
            },
    },
    'handlers':{
        'null':{
            'level':'DEBUG',
            'class':'logging.NullHandler',
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter':'verbose'
        },
        'file':{
            'level':'INFO',
            'class':'logging.FileHandler',
            'filename':LOG_FILE,
            'formatter':'verbose'
        },
    },
    'loggers':{
        'django':{
            'handlers':['console'],
            'propagate':True,
            'level':'INFO',
        },
        'students.signals':{
            'handlers':['console','file'],
            'level':'INFO',
        },
        'students.packets.contact_admin':{
            'handlers':['console','file'],
            'level':'INFO',
        }
    }
}


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REGISTRATION_OPEN = True

SOCIAL_AUTH_FACEBOOK_KEY='157159691729285'

SOCIAL_AUTH_FACEBOOK_SECRET='e5c2fef59822d3eb0854a35c6a2750e1'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
