import random
from .models import Post,Cat

from django.contrib.auth.models import User

#Home functions

def homewell(request):
    if request.user.is_authenticated():
        return 'Hi, ' + str(request.user.username).capitalize() + '!'
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
    return [val,catobj.icon,catobj.color]

def catcall():
    cats = Cat.objects.all()
    catlady = ""
    for i in cats:
        catlady += '<option value=\"{}\">{}</option>'.format(i.pk,i.title)

    return catlady


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

def renderprev(pk,req):
    rtn = []


    for i in pk:
        d = False
        s = False
        obj = Post.objects.get(pk=i.pk)
        if req.user.is_authenticated():
            stat = check_stat(art=obj,usr=req.user.pk)
            d = stat[0]
            s = stat[1]



        di = {
            'title':obj.title,
            'cat':getcat(obj)[1],
            'b1':timeicon(obj.time),
            'b2':getcat(obj)[2],
            'b3':diff(obj.diff)[1],
            'pk':obj.pk,
            'done':d,
            'saved':s,
        }
        if obj.vis:
            rtn.append(di)
    return rtn


def check_stat(art,usr):
    usr_pk = User.objects.get(pk=usr)
    doneq = art.done_usr.filter(pk=usr_pk.pk).exists()
    savedq = art.saved_usr.filter(pk=usr_pk.pk).exists()

    return [doneq,savedq]

def set_state(req):
    type = req.POST.get('type')
    usr = req.POST.get('usr')
    art = req.POST.get('art')
    bool = req.POST.get('bool')

    usrobj = User.objects.get(pk=usr)
    artobj = Post.objects.get(pk=art)


    if type == 'saved' and bool == 'true':
        artobj.saved_usr.add(usrobj)

    if type == 'saved' and bool == 'false':
        artobj.saved_usr.remove(usrobj)

    if type == 'done' and bool == 'true':
        artobj.done_usr.add(usrobj)

    if type == 'done' and bool == 'false':
        artobj.done_usr.remove(usrobj)

def post_staging(request):
    pass