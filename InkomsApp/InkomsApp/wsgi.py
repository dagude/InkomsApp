"""
WSGI config for InkomsApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InkomsApp.settings')

application = get_wsgi_application()

# whitenoise - se incluye

from whitenoise import WhiteNoise

# from InkomsApp import wsgi

# application = WhiteNoise(application, root="/path/to/static/")
# application.add_files("/path/to/more/static/", prefix="more-files/")