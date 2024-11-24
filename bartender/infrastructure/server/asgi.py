"""
ASGI config for t project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

environment = os.environ.get("ENVIRONMENT", "local")
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "bartender.infrastructure.settings.{}".format(environment)
)

application = get_asgi_application()