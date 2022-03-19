import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

import configurations   # noqa: E402

configurations.setup()

application = get_asgi_application()
