from django.shortcuts import render
from django.http import HttpResponse
from .models import user
from .models import member
from .models import visitor
from .models import comment
from .models import post
from .models import event
from .models import donation

# Create your views here.

def home(request):

    return render(request, 'home.html')

def sobre(request):

    return render(request, 'sobre.html')

def eventos(request):

    return render(request, 'eventos.html')

def guia(request):

    return render(request, 'guia.html')

def prj(request):

    return render(request, 'prj.html')

def voluntariado(request):

    return render(request, 'voluntariado.html')

def login(request):

    return render(request, 'login.html')


def custom_404_view(request, exception=None):
    return HttpResponseNotFound(render(request, '404.html'))

def test_500_view(request):
    raise Exception("Testing 500 error page")
