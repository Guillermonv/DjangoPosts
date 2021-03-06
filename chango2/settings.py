"""
Django settings for chango2 project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ie2*!82$#zd)w0w!^m=q#tkf%vdobrvg1(0o4kq@re3%u*f)s5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['ec2-18-223-113-184.us-east-2.compute.amazonaws.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_mysql',
    'users',
    'posts',
    'comments',
    'django.contrib.sites', # new

    'allauth', # new
    'allauth.account', # new
    'allauth.socialaccount', # new
    'allauth.socialaccount.providers.google', # new
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


  #  'chango2.middelware.ProfileCompletionMiddelware',
]

libraries: {
    'tags': 'tags',

}

ROOT_URLCONF = 'chango2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': ['ec2-54-207-55-15.sa-east-1.compute.amazonaws.com' + os.path.join(BASE_DIR,'templates')],
        #'DIRS': ['templates'],
        #'DIRS': [BASE_DIR + "/templates", ],
        #'DIRS' : ['ec2-54-207-55-15.sa-east-1.compute.amazonaws.com/home/ubuntu/DjangoPosts/templates/'],
        'DIRS' : [os.path.join(BASE_DIR, 'templates')],
        #'DIRS' :[],
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

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)


WSGI_APPLICATION = 'chango2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '1s4',
       'PASSWORD': '1s4b3ll4',
        #'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'admin',
        'HOST': 'database-1.cf8l9xy80cyd.us-east-2.rds.amazonaws.com',


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

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True
APPEND_SLASH = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATICFILES_DIRS= (os.path.join(BASE_DIR,'static'),)

STACTICFILES_FINDER= [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL ='/media/'
LOGIN_URL = 'users/login'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # since you are using a gmail account
EMAIL_PORT = 587  # Gmail SMTP port for TLS
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'guillermo.varelli@gmail.com'
EMAIL_HOST_PASSWORD = '!S@b3ll4Va'


AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 2

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/users/login'
