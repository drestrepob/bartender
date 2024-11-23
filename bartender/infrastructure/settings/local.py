from bartender.infrastructure.settings.base import *
from bartender.infrastructure.settings.utils import get_secret


def show_toolbar(request):
    """
    The default callback checks if the IP is internal, but docker's IP
    addresses are not in INTERNAL_IPS, so we force the display in dev mode
    :param request: The intercepted request
    :return: True OR False
    """
    return get_secret('DEBUG_TOOLBAR') == str(True)


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = get_secret('SECRET_KEY')

ALLOWED_HOSTS = ['*']

DEV_APPS = [
    'corsheaders',
    'debug_toolbar',
]

INSTALLED_APPS += DEV_APPS

DEV_MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS middleware should be at the top of the list
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

MIDDLEWARE = MIDDLEWARE + DEV_MIDDLEWARE

CORS_ORIGIN_ALLOW_ALL = True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    'SKIP_TEMPLATE_PREFIXES': (
        'django/forms/widgets/',
        'admin/widgets/',
        'menus/',
        'pipeline/',
    ),
}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
