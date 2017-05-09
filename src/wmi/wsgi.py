"""
WSGI config for wmi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, site, sys

site.addsitedir('/home/ubuntu/myproject/wmi_env/lib/python3.5/site-packages')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, '..'))

os.environ["DJANGO_SETTINGS_MODULE"] = "wmi.settings"

 
#application = get_wsgi_application()

from django.core.wsgi import get_wsgi_application

env_variables_to_pass = ['AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY', 'EMAIL_HOST_PASSWORD', 'SECRET_KEY',]

def application(environ, start_response):
	os.environ['foo'] = 'bar'
	return get_wsgi_application()(environ, start_response)

