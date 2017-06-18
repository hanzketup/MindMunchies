import random
import re
import json
from models import Post,Cat


#Home functions

def homewell(request):
    if request.user.is_authenticated():
        return 'Hi, ' + request.user.username + '!'
    else:
        mess = ['Welcome!','Hi!','Hey!','Hello!','Yo!','Wassup!','Howdy!','Hey you!']
        return random.choice(mess)

#Article functions
def diff(din):
    diff_dict = {1:['Beginner','#27ae60'],2:['Intermediate','#3498db'],3:['Advanced','#cc6055']}
    return diff_dict[din]

def getrandom():
    obj = Post.objects.all()
    resp = []
    for i in obj:
        resp.append(i.pk)
    return random.choice(resp)

def timeicon(time):

    if time < 2:
        return '#27ae60'
    elif time > 2 and time < 8:
        return '#3498db'
    elif time > 8:
        return '#cc6055'
    else:
        return '#27ae60'

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

def renderprev(pk,req): #needs stat conn
    rtn = []
    for i in pk:
        obj = Post.objects.get(pk=i.pk)
        stat = check_stat(art=obj,req=req)
        di = {
            'title':obj.title,
            'cat':getcat(obj)[1],
            'b1':timeicon(obj.time),
            'b2':getcat(obj)[2],
            'b3':diff(obj.diff)[1],
            'pk':obj.pk,
            'done':stat[0],
            'saved':stat[1],
        }
        rtn.append(di)
    return rtn


def check_stat(art,req):
    usr_pk = req.user.pk
    doneq = art.done_usr.filter(pk=usr_pk).exists()
    savedq = art.saved_usr.filter(pk=usr_pk).exists()

    return [doneq,savedq]