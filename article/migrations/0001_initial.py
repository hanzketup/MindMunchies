# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 10:32
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('title', models.TextField(max_length=100)),
                ('vis', models.BooleanField()),
                ('short_desc', models.TextField()),
                ('time', models.IntegerField()),
                ('cat', models.IntegerField()),
                ('diff', models.IntegerField()),
                ('vid', models.CharField(max_length=100)),
                ('links', jsonfield.fields.JSONField()),
                ('long_desc', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField()),
                ('usr_id', models.IntegerField()),
                ('fav', models.BooleanField()),
                ('done', models.BooleanField()),
            ],
        ),
    ]
