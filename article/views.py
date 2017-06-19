# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse,Http404
from .articlefunc import *


def index(request):
    topage = {'title':homewell(request),}
    return render(request,"article/home.html", topage)


def rand(request):
    rpk = getrandom()
    return redirect('/munchie/' + str(rpk))


def get(request, pk):
    r = Post.objects.get(pk=pk)
    d = False
    s = False

    if request.user.is_authenticated():
        stat = check_stat(art=r, usr=request.user.pk)
        d = stat[0]
        s = stat[1]

    if r.vis:
        artvar = {'title':r.title,
                  'pk':r.pk,
                  'short':r.short_desc,
                  'time':r.time,'timeicon':timeicon(r.time),
                  'cat':getcat(r)[0], 'caticon':getcat(r)[1],'catcolor':getcat(r)[2],
                  'diff':diff(r.diff)[0], 'diffcolor':diff(r.diff)[1],
                  'vid':r.vid,'vidvis':vidcheck(r.vid),
                  'links':parselinks(r.links),
                  'long':parsetxt(r.long_desc),

                  'done': d,
                  'saved': s,

                  'wrap':'back',#META
                  }
        return render(request, "article/article.html", artvar)
    else:
        return rand()

def me(request):

    if request.user.is_authenticated():

        return render(request,"article/me.html")
    else:
        return redirect('/login')

def munchies(request):
        o = Post.objects.all()
        cont = {
            'a':'drop-hover',
            'b':' ',
            'c':' ',
            'art':renderprev(o, request),

        }
        return render(request,"article/munchies.html", cont)


def arr(request):
    return render(request,'article/arr.html')

def new(request):


    return render(request,'meta/new.html', {'cats':catcall()})



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

def loggout(request):
    logout(request)
    return redirect('/')

def stat(request):
    if request.is_ajax() and request.POST:
        set_state(request)
        data = {'success': True}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404