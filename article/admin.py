# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from article.models import Post,Cat,EUser,Arch,Msg

admin.site.register(EUser)

admin.site.register(Post)
admin.site.register(Cat)
admin.site.register(Arch)

admin.site.register(Msg)