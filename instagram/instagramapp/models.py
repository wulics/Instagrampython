
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class MiUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.CharField(max_length=100, null = True)

class Follow( models.Model ):
    usuario_sigue = models.ForeignKey(MiUsuario, related_name='%(class)s_usuario_sigue' )
    usuario_sigo = models.ForeignKey(MiUsuario, related_name='%(class)s_ususario_sigo' )

class Post(models.Model):
    photo = models.CharField(max_length=100, null = True)
    time = models.DateTimeField(default=datetime.now)
    description = models.CharField(max_length=100, null = True)
    creador = models.ForeignKey(MiUsuario)

#for item in MiUsuario.objects.all():
#print (item.usuario.username + '-' + str(item.usuario.id) + '-' + str(item.id))

class Comment(models.Model):
    text = models.CharField(max_length=100)
    creador = models.ForeignKey(MiUsuario)
    post_id = models.ForeignKey(Post)

class Like(models.Model):
    user_id = models.ForeignKey(MiUsuario)
    post_id = models.ForeignKey(Post)
