# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from models import Post

from articlefunc import *

def index(request):
    return render(request,"article/munchies.html")


def rand(request):
    rpk = getrandom()
    #fix for production
    rurl = 'http://127.0.0.1:8000/munchie/' + str(rpk)
    return HttpResponseRedirect(rurl)


def get(request, pk):
    r = Post.objects.get(pk=pk)
    if r.vis:
        artvar = {'title':r.title,
                  'short':r.short_desc,
                  'time':r.time,
                  'cat':'',
                  'diff':diff(r.diff),
                  ' ':' ',}

        return render(request, "article/article.html")

    else:
        return rand()
