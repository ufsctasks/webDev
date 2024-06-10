from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    donation_value = models.IntegerField(default=0)

    def __str__(self):
        return self.phone

class member(user):
    created_at = models.DateTimeField(auto_now_add=True)
