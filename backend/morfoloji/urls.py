from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from . import views
# from main.views import (login_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    # url(r'^.*', TemplateView.as_view(template_name="index.html"), name="index")
]

urlpatterns += staticfiles_urlpatterns()
