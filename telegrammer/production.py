import os

from .settings import ALLOWED_HOSTS, BASE_DIR

ALLOWED_HOSTS += ['*']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': os.getenv('DJANGO_DB_NAME', 'db'),
		'USER': os.getenv('DJANGO_DB_USER', 'user'),
		# should be same as uWSGI user so we can use PostgreSQL local peer authentication mod (not in docker)
		'PASSWORD': os.getenv('DJANGO_DB_PASSWD', 'pass'),
		# PASSWORD is not required in PostgreSQL local peer mod, but required while using docker
		'HOST': os.getenv('DJANGO_DB_HOST', 'db'),  # make sure this point to correct database host in docker
		'CONN_MAX_AGE': 600,  # persistent connection to improves performance
	}
}

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True