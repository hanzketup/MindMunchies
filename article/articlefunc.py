import random
import re
import json
from models import Post,Cat


def diff(din):
    diff_dict = {1:['Beginner','icon-green'],2:['Intermediate','icon-blue'],3:['Advanced','icon-red']}
    return diff_dict[din]

def getrandom():
    obj = Post.objects.all()
    resp = []
    for i in obj:
        resp.append(i.pk)
    return random.choice(resp)

def getcat(r):
    val = r.acat.all()[0]
    catobj = Cat.objects.get(title=val)
    catobj.color
    return [val,catobj.icon,catobj.color]

def parselinks(inp):
    snd = ""
    for k,v in inp.items():
        snd += "<li><a href=" + str(v) + ">" + str(k) + "</a></li>"
    return snd

def parsetxt(inp):
    snd = ""
    for k,v in inp.items():
        snd += "<h1>" + str(k) + "</h1><p>" + str(v) + "</p>"
    return snd

