# import this in development.py, production.py
from .base import *
import dj_database_url

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config("EMAIL_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_PASSWORD")
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# Redis Cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": config("REDIS_BACKEND"),
    },
}

DATABASES["default"] = dj_database_url.parse("postgres://billy_app_postgres_user:2Rr9UIZvNMra6Si0r3tKkjce7IYE0iHc@dpg-covbic021fec73fi1hu0-a.oregon-postgres.render.com/billy_app_postgres")