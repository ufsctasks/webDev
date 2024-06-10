from django.db import models
from django.db.models.query import NamedValuesListIterable

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
    member_matricula = models.BigIntegerField(default=0)

    #perminssions

    comments_allowed = models.BooleanField(default=False)
    donation_allowed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class member(user):
    member_id = models.CharField(max_length=100)
    #perminssions

    events_allowed = models.BooleanField(default=True)
    settings_allowed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class visitors(models.Model):
    visitor_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)

    #perminssions

    donation_allowed = models.BooleanField(default=True)
    def __str__(self):
        return self.visitor_id

#backend funcionalities model

class comments(models.Model):
    comment_id = models.CharField(max_length=100)
    comment_user = models.ForeignKey(user, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_created_at = models.DateTimeField(auto_now_add=True)
    comment_deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_id
class posts(models.Model):
    post_id = models.CharField(max_length=100)
    post_user = models.ForeignKey(user, on_delete=models.CASCADE)
    post_text = models.TextField()
    post_image = models.ImageField(upload_to='post_images')
    post_comments = models.ForeignKey(comments, on_delete=models.CASCADE)
    post_created_at = models.DateTimeField(auto_now_add=True)
    post_deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_id

class events(models.Model):
    event_id = models.CharField(max_length=100)
    event_name = models.CharField(max_length=100)
    event_description = models.TextField()
    event_date = models.DateTimeField(auto_now_add=True)
    event_location = models.CharField(max_length=100)
    event_image = models.ImageField(upload_to='event_images')
    envent_user = models.ForeignKey(user, on_delete=models.CASCADE)
    event_comments = models.ForeignKey(comments, on_delete=models.CASCADE)
    event_created_at = models.DateTimeField(auto_now_add=True)
    event_deleted_at = models.DateTimeField(auto_now_add=True)
    event_hours_value = models.IntegerField(default=0)

    def __str__(self):
        return self.event_name

class donations(models.Model):
    donation_id = models.CharField(max_length=100)
    donation_user = models.ForeignKey(user, on_delete=models.CASCADE)
    donation_value = models.IntegerField()
    donation_created_at = models.DateTimeField(auto_now_add=True)
    donation_deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.donation_id
