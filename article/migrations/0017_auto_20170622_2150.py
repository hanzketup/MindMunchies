# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_post_changes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='changes',
            field=models.ManyToManyField(blank=True, to='article.Msg'),
        ),
    ]
