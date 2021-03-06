# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-19 08:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0010_auto_20180319_0720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('profile_photo', models.ImageField(blank=True, upload_to='photos/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='userprofile',
            new_name='profile',
        ),
    ]
