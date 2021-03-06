# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse,Http404
from .articlefunc import *

from .models import Msg


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
        dif = diff(r.diff)
        cat = getcat(r)
        artvar = {'title':r.title,
                  'pk':r.pk,
                  'short':r.short_desc,
                  'time':r.time,'timeicon':timeicon(r.time),
                  'cat':cat[0], 'caticon':cat[1],'catcolor':cat[2],
                  'diff':dif[0], 'diffcolor':dif[1],
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
    if request.method == 'POST':
        post_staging(request)
        return redirect('/new-munchie/thanks')
    else:
        return render(request,'meta/new.html', {'cats':catcall()})

def new_thanks(request):
    return render(request,'meta/new_thanks.html')


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

#Meta views

def about(request):
    return render(request,'meta/about.html')

def quest(request):

    if request.method == 'POST':
        new_msg = Msg(
            name=request.POST['name'],
            email=request.POST['email'],

            title=request.POST['title'],
            msg=request.POST['msg']

        )
        new_msg.save()
        return redirect('/question/thanks')
    else:
        return render(request,'meta/quest.html')


def quest_thanks(request):
    return render(request,'meta/thanks.html')


def change(request):
    if request.method == 'POST':
        new_msg = Msg(
            name=request.POST['name'],
            email=request.POST['email'],

            title=request.POST['title'],
            msg=request.POST['msg']

        )
        new_msg.save()

        pk = request.POST['pk']
        postobj = Post.objects.get(pk=pk)
        postobj.changes.add(new_msg)

        return redirect('/change/thanks')
    else:
        artid = request.GET.get('id')
        return render(request,'meta/change.html', {'id':artid})


def change_thanks(request):
    return render(request,'meta/change_thanks.html')