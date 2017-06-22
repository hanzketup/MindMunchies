from django.conf.urls import url

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^munchie/$', views.rand),
    url(r'munchie/(?P<pk>\d+)/$', views.get),
    url(r'me$', views.me),
    url(r'^munchies$', views.munchies),
    url(r'^achievements$', views.arr),

    url(r'^new-munchie$', views.new),
    url(r'^new-munchie/thanks$', views.new_thanks),
    url(r'^change$', views.change),
    url(r'^change/thanks$', views.change_thanks),
    url(r'^about$', views.about),
    url(r'^question$', views.quest),
    url(r'^question/thanks$', views.quest_thanks),

    url(r'^login/$', views.logg),
    url('^register/', CreateView.as_view(
        template_name='registration/register.html',
        form_class=UserCreationForm,
        success_url='/login'
    )),

    url(r'^logout/$', views.loggout),

    url(r'^stat/$', views.stat),



]
