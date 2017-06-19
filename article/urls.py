from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^munchie/$', views.rand),
    url(r'munchie/(?P<pk>\d+)/$', views.get),
    url(r'me$', views.me),
    url(r'^munchies$', views.munchies),
    url(r'^achievements$', views.arr),

    url(r'^new-munchie$', views.new),

    url(r'^login/$', views.logg),
    url(r'^logout/$', views.loggout),

    url(r'^stat/$', views.stat),

]
