
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}

SECRET_KEY = 'SECRET_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']
SITE_ID = 1
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '***'
EMAIL_HOST_PASSWORD = '***'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

DISQUS_API_KEY = '***'
DISQUS_WEBSITE_SHORTNAME = '***'

# No Recaptha SITE_KEY and SECRET KEY
# https://www.google.com/recaptcha
NORECAPTCHA_SITE_KEY = "***"
NORECAPTCHA_SECRET_KEY = "***"