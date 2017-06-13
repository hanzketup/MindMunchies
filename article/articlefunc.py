import random
import re
import json
from models import Post,Cat


#Home functions

def homewell():
    mess = ['Welcome!','Hi!','Hey!','Hello!','Yo!','Wassup!','Howdy!','Hey you!']
    return random.choice(mess)

#Article functions
def diff(din):
    diff_dict = {1:['Beginner','icon-green'],2:['Intermediate','icon-blue'],3:['Advanced','icon-red']}
    return diff_dict[din]

def getrandom():
    obj = Post.objects.all()
    resp = []
    for i in obj:
        resp.append(i.pk)
    return random.choice(resp)

def timeicon(time):

    if time < 2:
        return 'icon-green'
    elif time > 2 and time < 8:
        return 'icon-blue'
    elif time > 8:
        return 'icon-red'
    else:
        return 'icon-green'

def getcat(r):
    val = r.acat.all()[0]
    catobj = Cat.objects.get(title=val)
    catobj.color
    return [val,catobj.icon,catobj.color]

def vidcheck(video):
    if len(video) < 5:
        return 'none'
    else:
        return 'block'

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

