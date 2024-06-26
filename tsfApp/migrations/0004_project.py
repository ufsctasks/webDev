# Generated by Django 5.0.6 on 2024-07-01 17:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsfApp', '0003_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=100)),
                ('project_description', models.TextField()),
                ('project_image', models.ImageField(upload_to='project_images')),
                ('project_created_at', models.DateTimeField(auto_now_add=True)),
                ('project_deleted_at', models.DateTimeField(auto_now_add=True)),
                ('project_comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tsfApp.comment')),
            ],
        ),
    ]
