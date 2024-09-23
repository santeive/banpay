# import this in development.py, production.py
from .base import *
import dj_database_url
#EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config("EMAIL_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_PASSWORD")
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "../", "mediafiles")

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "../", "staticfiles")

DATABASES["default"] = dj_database_url.parse("postgresql://banpay_django_render_user:W6KHzbOnd3tM7QKGXyFOTrz9psH0Y2yu@dpg-crnp8me8ii6s73eud0r0-a.oregon-postgres.render.com/banpay_django_render")