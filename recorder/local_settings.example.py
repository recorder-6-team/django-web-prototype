# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#insert-key-here#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': '#Insert name of testing database#',
        'HOST': '#insert datatabase host here#',
        'PORT': '',
        'OPTIONS': {
            #'driver': 'ODBC Driver 17 for SQL Server',
            'driver': 'SQL Server Native Client 11.0',
        },
    }
}

ORGANISATION_NAME = '#Insert your name or your organisation name here#'

# Your 8 character Recorder licence Site ID.
SITE_ID = '#Insert your 8 character recorder licence site ID here#'


"""
Enable the following to log SQL queries to the console.
LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
}
"""