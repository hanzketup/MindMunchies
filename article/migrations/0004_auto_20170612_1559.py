# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 15:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_cat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='name',
            new_name='title',
        ),
    ]
