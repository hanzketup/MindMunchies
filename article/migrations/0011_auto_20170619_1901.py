# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 19:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20170617_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Post_comment',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='author_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='post',
            name='done_usr',
            field=models.ManyToManyField(blank=True, related_name='user_done', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='saved_usr',
            field=models.ManyToManyField(blank=True, related_name='user_saved', to=settings.AUTH_USER_MODEL),
        ),
    ]
