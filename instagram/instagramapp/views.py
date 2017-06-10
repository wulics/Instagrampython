from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from instagramapp.models import *
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')
@login_required
def foto(request):
    return render(request, 'foto.html')

def index(request):
    return render(request, 'registro.html')

def registro(request):
    return render(request, 'registro.html')
@login_required
def perfil(request):
    curr_user = request.user
    media_user = Post.objects.filter( creador = curr_user.id );
    context = { 'curr_user' : curr_user, 'media_user' : media_user }
    return render(request, 'perfil.html', context)

def crear_usuario(request):
    _email = request.POST[ 'email' ]
    _username = request.POST[ 'username' ]
    _name = request.POST[ 'name' ]
    _password = request.POST[ 'password' ]
    print (_email)
    print (_username)
    print (_name)
    print (_password)
    user = User.objects.create_user(username=_username, password=_password, email=_email, first_name=_name)
    myUser= MiUsuario(usuario = user)
    myUser.save()
    print (user)
    print (user.password)
    return redirect('inicio')

@login_required
def uploadFile(request):
    curr_user = request.user
    my_user = MiUsuario.objects.get(pk = curr_user.id)
    post_user = Post.objects.filter(creador=my_user).count();
    mediaFile = request.FILES[ 'foto' ];
    newNameFile = curr_user.username + "-" + str(curr_user.id) + "-" + str(post_user);
    fs = FileSystemStorage()
    filename = fs.save(newNameFile, mediaFile)
    uploaded_file_url = fs.url(filename)
    photo = uploaded_file_url;
    description = request.POST[ 'description' ];
    newPost = Post( photo = photo, description = description, creador = my_user );
    newPost.save();
    media_user = Post.objects.filter( creador = curr_user.id );
    context = { 'curr_user' : curr_user, 'media_user' : media_user }
    return render(request, 'perfil.html', context)
