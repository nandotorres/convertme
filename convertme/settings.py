# Django settings for convertme project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Fernando', 'nandotorres@gmail.com'),
)

MANAGERS = ADMINS

APP_URL = '/'
APP_ROOT = '/app/convertme/app'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': APP_ROOT + '/database/convertme.db'
    }
}

TIME_ZONE = 'America/Sao_Paulo'

LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

SITE_URL = 'http://ec2-67-202-24-179.compute-1.amazonaws.com'

MEDIA_ROOT = APP_ROOT + '/media/'

MEDIA_URL = APP_URL + 'media/'

STATIC_ROOT = APP_ROOT + '/assets/'

STATIC_URL = APP_URL + 'assets/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

STATICFILES_DIRS = (
    ("css", APP_ROOT + "/assets/css"),
    ("img", APP_ROOT + "/assets/img"),
    ("js", APP_ROOT + "/assets/js"),
)

SECRET_KEY = '+-3xl4dj)r&amp;wf_#!9=dp1i2553a!hztx1yyi10v)n(di1hv-sd'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'convertme.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'convertme.wsgi.application'

TEMPLATE_DIRS = (
    APP_ROOT + '/templates/'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app'
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

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
