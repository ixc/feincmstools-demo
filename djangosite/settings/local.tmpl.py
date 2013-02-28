from default import *

DEBUG = True            # True/False
DEBUG_TOOLS = DEBUG     # Use debug toolbar
THUMBNAIL_DEBUG = DEBUG # Debug thumbnail errors
TEMPLATE_DEBUG = DEBUG

#TEMPLATE_STRING_IF_INVALID = "INVALID"

CACHE_BACKEND = 'locmem://' #drop-dead simple cacheing

# Additional apps (usually local development helpers)
INSTALLED_APPS += (
    'django_extensions',
)

DATABASES = {
    'default': {
        'NAME': '',
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Either 'django.db.backends.postgresql_psycopg2' or 'django.db.backends.sqlite3'.
        'HOST': '127.0.0.1', # homebrew-compatible
        'USER': '', # Your database username (not used for SQLite).
        'PASSWORD': '', # Your database password (not used for SQLite).
    }
}

SITE_ID = 1 #used by django.contrib.sites

# Fallbackserve grabs media from a staging server if necessary.
# Use these settings for your project:
#DEFAULT_FILE_STORAGE = 'fallbackserve.storage.FallbackStorage'
#FALLBACK_STATIC_URL = 'http://stg.site.com/media/'
#FALLBACK_STATIC_URL_USER = 'preview'
#FALLBACK_STATIC_URL_PASS = 'pass'
#FALLBACK_STATIC_PREFIXES = (
#    'uploads/',
#    'uploaded_img/',
#    'thumbs/'
#)
