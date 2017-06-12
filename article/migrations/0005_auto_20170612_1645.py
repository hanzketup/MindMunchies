# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20170612_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='acat',
            field=models.ManyToManyField(to='article.Cat'),
        ),
        migrations.AddField(
            model_name='stat',
            name='post_id',
            field=models.ManyToManyField(to='article.Post'),
        ),
    ]