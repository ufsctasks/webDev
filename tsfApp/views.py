from django.shortcuts import render
from django.http import HttpResponse
from .models import user
from .models import member
from .models import visitors
from .models import comments
from .models import posts
from .models import events
from .models import donations

# Create your views here.

def home(request):
    posts1 = posts()
    posts1.post_id = '1'
    posts1.post_title = 'Post 1'
    posts1.post_text = 'This is the first post'
    posts1.post_created_at = '2021'

    posts2 = posts()
    posts2.post_id = '2'
    posts2.post_title = 'Post 2'
    posts2.post_text = 'This is the second post'
    posts2.post_created_at = '2021'

    enevt1 = events()
    enevt1.event_id = '1'
    enevt1.event_title = 'Event 1'
    enevt1.event_text = 'This is the first event'
    enevt1.event_created_at = '2021'

    enevt2 = events()
    enevt2.event_id = '2'
    enevt2.event_title = 'Event 2'
    enevt2.event_text = 'This is the second event'
    enevt2.event_created_at = '2021'

    return render(request, 'home.html', {'posts': [posts1, posts2], 'events': [enevt1, enevt2]})

def login(request):

    return render(request, 'login.html')
