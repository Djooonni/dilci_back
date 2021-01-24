from django.urls import path

from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.work, name='work'),
    # path('work', views.work, name='work'),
    # path('haqqimizda', views.about, name='about'),
    # # viewdan goturub import edir ve adlar eyni olmali
    # path('contact', views.contact, name='contact'),
    # # viewdan goturub import edir ve adlar eyni olmali
    # path('main', views.index, name='index'),
    # path('login', views.login_view, name='login'),
    path('morfoloji', views.morf_view, name='morf'),
    path('yarat', views.yarat_view, name='yarat'),
    path('metn', views.metn_view, name='metn'),
    # path('luget', views.luget_view, name='luget'),

]
