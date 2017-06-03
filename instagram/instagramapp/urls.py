from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^upload/$', views.foto, name='subirfoto'),
    url(r'^registro/$', views.registro, name='registro'),
    url(r'^perfil/$', views.perfil, name='perfil'),
    url(r'^crear_usuario/$', views.crear_usuario, name='crearusuario'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='inicio.html', redirect_authenticated_user=True), name= 'inicio'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='registro.html'), name= 'salir'),
]
