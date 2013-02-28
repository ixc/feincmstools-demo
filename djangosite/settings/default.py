import sys, os

# First settings to change ====================================================

SITE_URL = 'http://example.com'
SITE_NAME = 'IC Site'
SITE_ID = 1

TEMPLATE_CONSTANTS = {
    #values here are passed into the context of every template with django-generic.context_processors.generic
    #This dictionary is updated with SITE_URL and SITE_NAME in __init__.py
#    'GOOGLE_MAPS_API_KEY': 'xxx',
}

# Make this unique, and don't share it with anybody.
#SECRET_KEY = '+foqsr#f$vvq=*^divex*9vr72(pmb_4m1d3$xxi%$7z9&amp;5vgi'


# Path settings ===============================================================

# Absolute paths for where the project and templates are stored.
SETTINGS_ROOT = os.path.realpath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.realpath(os.path.join(SETTINGS_ROOT, os.path.pardir)) #the path of 'djangosite'
SITE_ROOT = os.path.realpath(os.path.join(PROJECT_ROOT, os.path.pardir)) #normally git checkout. manage.py lives here
PROJECT_NAME = os.path.basename(PROJECT_ROOT) #'djangosite'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(SITE_ROOT, 'static/')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Workaround for admin-tools' use of deprecated tag. FIXME: update admin-tools when available.
ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.abspath(os.path.join(SITE_ROOT, 'static_extra')),
)

# Apps, middleware, context processors, etc ===================================

INSTALLED_APPS = (
    # Django-admin-tools: needs to be declared before contrib.admin.

    # Core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.messages',

    'south',
    'easy_thumbnails',
    'compressor',

    'generic',
    'markitup',

    'debug_toolbar',

    'oembed',

    'mptt',
    'feincms',
    'feincms.module.medialibrary',
    'feincmstools',
    'adminboost',
#    'oembed',
    'singleton_models',

    'djangosite.meetups',
    'djangosite.magazine',

)

## south config for page model
#SOUTH_MIGRATION_MODULES = {
#    'page': 'djangosite.feincms_conf.feincms_page_migrations',
#}


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.csrf',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'generic.context_processors.generic',
    'djangosite.context_processors.site_section',
    'flatblocks.context_processors.flatblocks',
)

MIDDLEWARE_CLASSES = (
    # Uncomment the next line (and the line further down) to turn on site-wide
    # cacheing
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Uncomment the next line for Profiling
    # 'generic.middleware.ProfileMiddleware',
    # Uncomment the next line to turn on site-wide cacheing
    # 'django.middleware.cache.FetchFromCacheMiddleware',
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_PROFILE_MODULE = "accounts.Profile"
ANONYMOUS_USER_ID = -1 #Syncdb to create the user
#LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
#LOGIN_URL = '/accounts/signin/'
#LOGOUT_URL = '/accounts/signout/'

# A boolean that specifies whether to output the "Etag" header. This saves
# bandwidth but slows down performance. This is used by the CommonMiddleware
# and in the Cache Framework
USE_ETAGS = True

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}



# App-specific settings =======================================================

# Django-admin-tools ------------------
ADMIN_TOOLS_INDEX_DASHBOARD = 'djangosite.settings.admin.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'djangosite.settings.admin.dashboard.CustomAppIndexDashboard'
ADMIN_TOOLS_MENU = 'djangosite.settings.admin.menu.CustomMenu'
#ADMIN_TOOLS_THEMING_CSS = 'ixc-admin/theming.css'

# Debug Toolbar -----------------------
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.cache.CacheDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

INTERNAL_IPS = ('127.0.0.1',) # Add your ip to this (for the debug toolbar)

# FeinCMS -----------------------------
FEINCMS_JQUERY_NO_CONFLICT = True
FEINCMS_TREE_EDITOR_INCLUDE_ANCESTORS = True

# Django-markitup ---------------------
MARKITUP_FILTER = ('django.contrib.markup.templatetags.markup.textile', {})
MARKITUP_SET = 'markitup/sets/textile'

# Settings that rarely change =================================================

#TEST_RUNNER = 'djangosite.testrunner.CustomTestRunner'
TEST_RUNNER = 'djangosite.testrunner.UnitTest2TestDiscovery'  # Find in project

# Override unittest2 default 'test*.py' to find tests in 'test(s)' dirs
TEST_DISCOVER_PATTERN = 'test*'

ROOT_URLCONF = 'djangosite.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'djangosite.wsgi.application'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    # ('django.template.loaders.cached.Loader', ( #uncomment me to enable template cacheing
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
#        'django.template.loaders.eggs.Loader',

    # )), #uncomment me to enable template cacheing
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_ROOT, 'templates'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

ADMINS = (
    ('Interaction Consortium Admins', 'admins@interaction.net.au'),
)
MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be avilable on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Australia/Sydney'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-AU'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

FILE_UPLOAD_PERMISSIONS = 0755

# SMTP settings for sending emails
EMAIL_USE_TLS = True             # True/False
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ixc.test123@gmail.com'
EMAIL_HOST_PASSWORD = 'intheplacetobe1'
EMAIL_PORT = '587'                # Numeric value
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME # just a default value

DEFAULT_FROM_EMAIL = SERVER_EMAIL = ''

LOGIN_REDIRECT_URL = '/' # Django default: '/accounts/profile/'

# Put all the thumbnails in a thumbs/ folder
THUMBNAIL_BASEDIR = "thumbs"

# Django-compressor
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', os.path.join(os.getenv("VIRTUAL_ENV"), "bin", "pyscss") + " --load-path={inpath} {infile}"),
)
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_URL = STATIC_URL

# Flatblocks
# If set to True, this causes a Get or Create behaviour when retrieving flatblocks.
FLATBLOCKS_AUTOCREATE_STATIC_BLOCKS = True
FLATBLOCKS_STRICT_DEFAULT_CHECK = True
FLATBLOCKS_STRICT_DEFAULT_CHECK_UPDATE = True
