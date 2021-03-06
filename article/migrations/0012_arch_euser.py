# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 09:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0011_auto_20170619_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=40)),
                ('icon', models.CharField(max_length=100)),
                ('color', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='EUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
