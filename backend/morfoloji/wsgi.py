# -*- coding: utf-8 -*-

import os
import sys
import platform

#путь к проекту manage.py
sys.path.insert(0, '/home/c/cu79127/Dilciaz/public_html/Dilci/backend')
#путь к фреймворку settings.py
sys.path.insert(0, '/home/c/cu79127/Dilciaz/public_html/Dilci/backend/morfoloji')
#путь к виртуальному окружению
sys.path.insert(0, '/home/c/cu79127/Dilciaz/myenv/lib/python{0}/site-packages'.format(platform.python_version()[0:3]))
os.environ["DJANGO_SETTINGS_MODULE"] = "morfoloji.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


