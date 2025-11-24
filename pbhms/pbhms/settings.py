"""
Django settings for pbhms project.
"""

import os
import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------
# SECURITY
# ---------------------------

SECRET_KEY = os.environ.get("SECRET_KEY", "development-secret-key")
DEBUG = os.environ.get("DEBUG", "True") == "True"

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "192.168.1.8",
    ".onrender.com",        # allow any Render hostname
    "quadcorehotels.onrender.com",  # your exact hostname
]

# Render deployment hostname
RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# ---------------------------
# INSTALLED APPS
# ---------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your apps
    'theme',
    'tailwind',
    'django_browser_reload',
    'dashboard',
    'billing',
    'guests',
    'rooms',
    'services',
]

# ---------------------------
# MIDDLEWARE
# ---------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # Required for Render static files
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # Uncomment  below middleware if you want auto-reload
    # Do not push django browser auto reload in production
    # 'django_browser_reload.middleware.BrowserReloadMiddleware',
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Add browser reload only in DEBUG mode
if DEBUG:
    MIDDLEWARE.append("django_browser_reload.middleware.BrowserReloadMiddleware")

TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ['127.0.0.1']

ROOT_URLCONF = 'pbhms.urls'

# ---------------------------
# TEMPLATES
# ---------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pbhms.wsgi.application'

# ---------------------------
# DATABASE
# ---------------------------

# Default SQLite (local)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Render PostgreSQL (if DATABASE_URL exists)
db_url = os.environ.get("DATABASE_URL")
if db_url:
    DATABASES["default"] = dj_database_url.parse(db_url, conn_max_age=600)

# ---------------------------
# PASSWORD VALIDATION
# ---------------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ---------------------------
# INTERNATIONALIZATION
# ---------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# ---------------------------
# STATIC & MEDIA
# ---------------------------

STATIC_URL = '/static/'

# Production static directory (Render)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Dev static folder
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'theme', 'static'),
]

# Allow whitenoise to serve compressed static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

NPM_BIN_PATH = "D:/nodejs/npm.cmd"

# ---------------------------
# DEFAULT PRIMARY KEY FIELD
# ---------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
