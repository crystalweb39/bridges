import os
import sys
import site

path = '/Users/chaol/workspace/bridges/'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'bridges.settings-mac'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

import bridges.monitor
bridges.monitor.start(interval=1.0)
