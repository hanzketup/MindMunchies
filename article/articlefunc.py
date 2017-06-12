import random
import re
from models import Post


def diff(din):
    diff_dict = {1:'Easy',2:'intermediate',3:'advanced'}
    return diff_dict[din]

def vid(vin):
    match = r'embed\/(\w+)'
    vidpr = re.search(match, vin)
    return vidpr.group(1)

def getrandom():
    obj = Post.objects.all()
    resp = []
    for i in obj:
        resp.append(i.pk)

    return random.choice(resp)