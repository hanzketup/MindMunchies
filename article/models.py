# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField


class post(models.Model):
    title = models.TextField(max_length=100)
    created = models.DateTimeField(auto_created=True)
    vis = models.BooleanField()
    short_desc = models.TextField()
    time = models.IntegerField()
    cat = models.IntegerField()
    diff = models.IntegerField()

    vid = models.CharField(max_length=100)
    links = JSONField()

    def __str__(self):
        return self.title