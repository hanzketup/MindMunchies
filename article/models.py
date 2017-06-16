# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField

from django.contrib.auth.models import User

class Cat(models.Model):
    title = models.TextField(max_length=40)
    icon = models.CharField(max_length=100)
    color = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.title

class Post(models.Model):

    title = models.TextField(max_length=100)
    created = models.DateTimeField(auto_created=True)
    vis = models.BooleanField()

    short_desc = models.TextField()
    time = models.IntegerField()
    acat = models.ManyToManyField(Cat)
    diff = models.IntegerField()

    vid = models.CharField(max_length=100,blank=True)
    links = JSONField()
    long_desc = JSONField()

    def __str__(self):
        return self.title

class Stat(models.Model):
    post_id = models.ManyToManyField(Post)
    usr_id = models.ManyToManyField(User)
    fav = models.BooleanField(default=False)
    done = models.BooleanField(default=False)