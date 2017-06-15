# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,HttpResponseRedirect
from models import Post
from articlefunc import *


def index(request):
    topage = {
        'title':homewell(),
    }
    return render(request,"article/home.html", topage)


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
                  'time':r.time,'timeicon':timeicon(r.time),
                  'cat':getcat(r)[0], 'caticon':getcat(r)[1],'catcolor':getcat(r)[2],
                  'diff':diff(r.diff)[0], 'diffcolor':diff(r.diff)[1],
                  'vid':r.vid,'vidvis':vidcheck(r.vid),
                  'links':parselinks(r.links),
                  'long':parsetxt(r.long_desc),
                  'wrap':'back',#META
                  }
        return render(request, "article/article.html", artvar)
    else:
        return rand()

def me(request):

    if request.user.is_authenticated():

        return render(request,"registration/me.html")
    else:
        return redirect('/login')

def mymunchies(request):
    if request.user.is_authenticated():

        return render(request,"article/munchies.html")
    else:
        return redirect('/login')


def logg(request):
    if request.method == 'GET':
        return render(request,'registration/login.html')

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request,'registration/login.html',{'borderstyle':'rgba(231, 76, 60,1.0)','msg':'Incorrect username/password!'})