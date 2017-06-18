# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from article.models import Post,Cat

admin.site.register(Post)
admin.site.register(Cat)