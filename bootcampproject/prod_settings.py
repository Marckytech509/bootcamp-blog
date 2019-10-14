from .settings import *

TEMPLATE_DEBUG = DEBUG
# DEBUG = False

SECRET_KEY = '4i&u(!%shd*0-3$ls)fohsjsc48t(gu%1-ch_wyzk7@#n3bd8e'

ALLOWED_HOSTS = ['bootcamp-blogger.herokuapp.com']

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
