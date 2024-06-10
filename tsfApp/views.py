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

def login(request):

    return render(request, 'login.html')
