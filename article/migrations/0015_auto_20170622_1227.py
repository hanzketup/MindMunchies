# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_auto_20170620_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='msg',
            name='name',
            field=models.TextField(blank=True),
        ),
    ]