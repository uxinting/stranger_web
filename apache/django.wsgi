import os
import sys

path = '/home/djangoapps/work/stranger'

if path not in sys.path:
    sys.path.insert(0, '/home/djangoapps/work/stranger')

os.environ['DJANGO_SETTINGS_MODULE'] = 'stranger.settings'

#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
