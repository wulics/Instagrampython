from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
    url(r'^home/$', views.home, name='home'),
    url(r'^registro/$', views.registro, name='registro'),
]