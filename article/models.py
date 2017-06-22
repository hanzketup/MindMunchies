# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField

from django.contrib.auth.models import User

class Arch(models.Model):
    title = models.TextField(max_length=40)
    icon = models.CharField(max_length=100)
    color = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.title

class Cat(models.Model):
    title = models.TextField(max_length=40)
    icon = models.CharField(max_length=100)
    color = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.title

class EUser(models.Model):

    usr = models.OneToOneField(User)

    arch = models.ManyToManyField


class Msg(models.Model):

    name = models.TextField(blank=True)
    email = models.EmailField(blank=True)

    title = models.TextField()
    msg = models.TextField()

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

    done_usr = models.ManyToManyField(User,related_name ='user_done',blank=True)
    saved_usr = models.ManyToManyField(User,related_name ='user_saved',blank=True)

    author = models.TextField(blank=True)
    author_email = models.EmailField(blank=True)
    Post_comment = models.TextField(blank=True)

    changes = models.ManyToManyField(Msg,blank=True)

    def __str__(self):
        return self.title