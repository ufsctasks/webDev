# Generated by Django 5.0.6 on 2024-07-01 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tsfApp', '0004_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_comments',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_comments',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_comments',
        ),
        migrations.DeleteModel(
            name='comment',
        ),
    ]