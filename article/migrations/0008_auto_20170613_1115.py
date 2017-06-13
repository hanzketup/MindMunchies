# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20170612_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='vid',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='stat',
            name='post_id',
            field=models.ManyToManyField(to='article.Post'),
        ),
    ]
