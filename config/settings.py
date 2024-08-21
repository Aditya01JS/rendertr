"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
# Import dj-database-url at the beginning of the file.
import dj_database_url

from pathlib import Path
# import django_heroku
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ov#r^^&xv&^0vmc(zj&h_t^$*52@8jicn=%*z*@s-=li!s_p@='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOWED_ORIGINS = ['http://localhost:3000', 'http://127.0.0.1:3000', 'https://frontend-electric-views.herokuapp.com']

X_FRAME_OPTIONS = '*'
CORS_ORIGIN_ALLOW_ALL = True
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000/','https://freshzestjuice.netlify.app']

# Application definition

INSTALLED_APPS = [
    # To allow CORS (Cross-origin resource sharing)
    'corsheaders',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.posts',
    'apps.users', 
    'apps.carts', 
    'apps.orders',
    'apps.items',
    'cloudinary',
    'django_filters',
]

MIDDLEWARE = [
    # To allow CORS (Cross-origin resource sharing)
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# Heroku Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'unique_gqab',
#         'USER': 'unique_gqab_user',
#         'PORT': 5432,
#         'HOST': 'dpg-cqdakit6l47c73frqehg-a',
#         'PASSWORD': 'ism18OeCQiyj6t5LHCepO5ZrdxOfWCyU',
#     }
# }

# Host name - dpg-cr2pe0jv2p9s739b82d0-a
# Data base - braindb100
# User name - braindb_user
# passkey - sukZeff1JTyQGbA5pkMNz7qDTLs6g7Px
# internal db url - postgresql://braindb_user:sukZeff1JTyQGbA5pkMNz7qDTLs6g7Px@dpg-cr2pe0jv2p9s739b82d0-a/braindb100
# external db url - postgresql://braindb_user:sukZeff1JTyQGbA5pkMNz7qDTLs6g7Px@dpg-cr2pe0jv2p9s739b82d0-a.oregon-postgres.render.com/braindb100
# psql command - PGPASSWORD=sukZeff1JTyQGbA5pkMNz7qDTLs6g7Px psql -h dpg-cr2pe0jv2p9s739b82d0-a.oregon-postgres.render.com -U braindb_user braindb100


# Local Database
# Replace the SQLite DATABASES configuration with PostgreSQL:
DATABASES = {
    'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        # postgresql://unique_gqab_user:ism18OeCQiyj6t5LHCepO5ZrdxOfWCyU@dpg-cqdakit6l47c73frqehg-a.oregon-postgres.render.com/unique_gqab`
        default='postgresql://braindb_user:sukZeff1JTyQGbA5pkMNz7qDTLs6g7Px@dpg-cr2pe0jv2p9s739b82d0-a.oregon-postgres.render.com/braindb100',
        conn_max_age=600
    )
}



# Heroku PostgreSQL Database
# django_heroku.settings(locals())


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# This setting informs Django of the URI path from which your static files will be served to users
# Here, they well be accessible at your-domain.onrender.com/static/... or yourcustomdomain.com/static/...
STATIC_URL = '/static/'

# This production code might break development mode, so we check whether we're in DEBUG mode
if not DEBUG:
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


cloudinary.config(
    cloud_name="www-techis-io",
    api_key="891747999686865",
    api_secret="seWq_dLQRcb7O5eMY-XdAuznU_w",
    secure=True
)

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}






# Host name - dpg-cr2pe0jv2p9s739b82d0-a
# Data base - braindb100
# User name - braindb_user
# passkey - sukZeff1JTyQGbA5pkMNz7qDTLs6g7Px
# internal db url - postgresql://braindb_user:sukZeff1JTyQGbA5pkMNz7qDTLs6g7Px@dpg-cr2pe0jv2p9s739b82d0-a/braindb100
# external db url - postgresql://braindb_user:sukZeff1JTyQGbA5pkMNz7qDTLs6g7Px@dpg-cr2pe0jv2p9s739b82d0-a.oregon-postgres.render.com/braindb100
# psql command - PGPASSWORD=sukZeff1JTyQGbA5pkMNz7qDTLs6g7Px psql -h dpg-cr2pe0jv2p9s739b82d0-a.oregon-postgres.render.com -U braindb_user braindb100
