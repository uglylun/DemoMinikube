import sys
import time

from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY='atextforwirtedcraft',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFramOptionsMiddleware',
    ),
)

from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import JsonResponse

def index(request):
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return JsonResponse({'time': t})

urlpatterns = (
   url(r'^$', index),
)

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
