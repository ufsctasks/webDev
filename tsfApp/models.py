from django.db import models

# Create your models here.

#backend user model

class user(models.Model):
    user_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    donation_value = models.IntegerField(default=0)
    member_matricula = models.BigIntegerField(max_length=20)

    #perminssions

    comments_allowed = models.BooleanField(default=False)
    donation_allowed = models.BooleanField(default=False)

    def __str__(self):
        return self.phone

class member(user):
    member_id = models.CharField(max_length=100)
    #perminssions

    events_allowed = models.BooleanField(default=True)
    settings_allowed = models.BooleanField(default=False)

class visitors(models.Model)
    visitor_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    #perminssions

    donation_allowed = models.BooleanField(default=True)


#backend funcionalities model
