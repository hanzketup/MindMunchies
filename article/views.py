# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from models import Post

from 

def index(request):
    return render(request,"article/munchies.html")


def rand(request):
    obj = Post.objects.all()
    resp = ""
    for i in obj:
        resp += str(i.pk)

    return HttpResponse(resp)


def get(request, pk):
    r = Post.objects.get(pk=pk)
    if getart.vis:
        artvar = {'title':r.title,'short':r.short_desc,}

        return render(request,"article/article.html",)

    else:
        return HttpResponseRedirect()

