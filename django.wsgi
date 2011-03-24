import os
import sys
sys.path.append('/home/ec2-user/')
sys.path.append('/home/ec2-user/fsgames/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'fsgames.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()


