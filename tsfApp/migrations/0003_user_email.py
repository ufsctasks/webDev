# Generated by Django 5.0.6 on 2024-06-26 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsfApp', '0002_remove_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
