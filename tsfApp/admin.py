from django.contrib import admin
from .models import user
from .models import member
from .models import visitor
from .models import comment
from .models import post
from .models import event
from .models import donation

# Register your models here.
admin.site.register(post)
