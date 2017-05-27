from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.inicio, name='inicio'),
    url(r'^$', views.inicio, name='inicio'),
    url(r'^home/$', views.home, name='home'),
    url(r'^registro/$', views.registro, name='registro'),
    url(r'^perfil/$', views.perfil, name='perfil'),
    url(r'^crear_usuario/$', views.crear_usuario, name='crearusuario'),
]
