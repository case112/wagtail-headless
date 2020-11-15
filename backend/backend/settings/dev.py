from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$c_0h@so!qsl-wnrl4^x8*0l**3*pqnq55i3+=odq)wq(c7-@t'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/v2/'

HEADLESS_PREVIEW_CLIENT_URLS = {
    'default': 'http://localhost:8020/',
}


try:
    from .local import *
except ImportError:
    pass
