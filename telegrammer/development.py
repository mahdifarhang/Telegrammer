import os

from .settings import ALLOWED_HOSTS, BASE_DIR

ALLOWED_HOSTS += ['*']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Celery Settings
CELERY_BROKER_URL = "redis://127.0.0.1:6375"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6375"

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'telegrammer_database',
		'USER': 'telegrammer_database_user',
		# should be same as uWSGI user so we can use PostgreSQL local peer authentication mod (not in docker)
		'PASSWORD': 'telegrammer_database_password',
		# PASSWORD is not required in PostgreSQL local peer mod, but required while using docker
		'HOST': '127.0.0.1',  # make sure this point to correct database host in docker
		'PORT': 5429,
		'CONN_MAX_AGE': 600,  # persistent connection to improves performance
	}
}
