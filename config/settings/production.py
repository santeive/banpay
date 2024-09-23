# import this in development.py, production.py
from .base import *
import dj_database_url

# Redis Cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": config("REDIS_BACKEND"),
    },
}

DATABASES["default"] = dj_database_url.parse("postgresql://banpay_django_render_user:W6KHzbOnd3tM7QKGXyFOTrz9psH0Y2yu@dpg-crnp8me8ii6s73eud0r0-a.oregon-postgres.render.com/banpay_django_render")