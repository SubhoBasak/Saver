"""
WSGI config for saver project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

sys.path.insert(0, '/home/ubuntu/Saver/')
sys.path.append('/home/ubuntu/Saver/venv/lib/python3.10/site-packages/')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saver.settings')

application = get_wsgi_application()
