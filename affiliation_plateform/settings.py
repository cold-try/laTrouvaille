import os
import dj_database_url
import psycopg2

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if 'VIRTUAL_ENV' in os.environ:
    SECRET_KEY = 'django-insecure-ofk!$6@jf3--mbpkh^+dz8qzaf%$o6_((f6@7t%nj^y4r1!+&k'
    DJANGO_STATIC_HOST = 'https://dudtfwleya78z.cloudfront.net'
    TEMPLATES_ACCESS = os.path.join(BASE_DIR, 'build/templates')
    MAIN_HOST = "127.0.0.1"
    DEBUG = False

    STATIC_URL = '/static/' 
    STATIC_ROOT = 'static/' 
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'build/static')]
    MEDIA_ROOT = os.path.join(BASE_DIR, 'build/static', 'img')
    MEDIA_URL = "/media/"
    LOGIN_URL = 'connexion'
    SECURE_SSL_REDIRECT = False

else:
    SECRET_KEY = os.environ['SECRET_KEY']
    DJANGO_STATIC_HOST = os.environ['DJANGO_STATIC_HOST']
    TEMPLATES_ACCESS = os.path.join(BASE_DIR, 'templates')
    MAIN_HOST = os.environ['MAIN_HOST']
    DEBUG = True

    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = 'latrouvaille'
    
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_DEFAULT_ACL = 'public-read'

    AWS_S3_HOST = "s3.eu-central-1.amazonaws.com"
    S3_USE_SIGV4 = True
    AWS_S3_REGION_NAME = "eu-central-1"
    AWS_LOCATION = 'static'
    AWS_PUBLIC_MEDIA_LOCATION = 'media'

    STATIC_ROOT = os.path.join(BASE_DIR, 'build', 'static') # le dossier où les fichiers statiques seront stockés après collectstatic
    STATIC_HOST = DJANGO_STATIC_HOST
    STATIC_URL = STATIC_HOST + '/static/' # URL qui servira les fichiers statiques
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'build')]  # liste des dossiers contenants des fichiers statiques suppl. en plus du dossier static de chaque app.

    DEFAULT_FILE_STORAGE = 'mn.storages.MediaStore'
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    DATABASES = {}
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

ALLOWED_HOSTS = [MAIN_HOST, DJANGO_STATIC_HOST, "localhost"]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'core'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'affiliation_plateform.urls'

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

WSGI_APPLICATION = 'affiliation_plateform.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'maktaba_opensource',
        'USER': 'koldd',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2,

    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],

    'DEFAULT_THROTTLE_RATES': {
        'anon': '5000/min',
        'user': '5000/min'
    }
}


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

ROOT_URLCONF = 'affiliation_plateform.urls'

STATIC_URL = '/static/' 
STATIC_ROOT = 'static/' 
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'build/static')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'build/static', 'img')
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 1
REST_SESSION_LOGIN = False 
CSRF_COOKIE_SECURE = False
CORS_ALLOW_CREDENTIALS = True 