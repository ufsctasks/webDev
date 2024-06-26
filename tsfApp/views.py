from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import user
from .models import member
from .models import visitor
from .models import post
from .models import event
from .models import donation
from .models import project

# Create your views here.

def home(request):

    return render(request, 'home.html')

def sobre(request):

    return render(request, 'sobre.html')

def eventos(request):
    eventos   = event.objects.all()
    return render(request, 'eventos.html', {'eventos': eventos})

def guia(request):

    posts = post.objects.all()

    return render(request, 'guia.html', {'posts': posts})

def prj(request):
    projetos   = project.objects.all()

    return render(request, 'prj.html', {'projetos': projetos})

def voluntariado(request):

    return render(request, 'voluntariado.html')

def login(request):

    return render(request, 'login.html')

def register(request):
    username = request.POST.get('username')
    return render(request, 'register.html')

def recovery(request):
    email = request.POST.get('email')
    return render(request, 'recovery.html')


def projeto_detail(request, projeto_id):
    projeto = get_object_or_404(project, id=projeto_id)
    return render(request, 'projeto_detail.html', {'projeto': projeto})


#   Errors views

def custom_404_view(request, exception=None):
    return HttpResponseNotFound(render(request, '404.html'))

def test_500_view(request):
    raise Exception("Testing 500 error page")
