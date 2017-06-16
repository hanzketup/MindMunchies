from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^munchie/$', views.rand),
    url(r'munchie/(?P<pk>\d+)/$', views.get),
    url(r'me$', views.me),
    url(r'^munchies$', views.munchies),
    url(r'^munchies/saved$', views.munchies_s),
    url(r'^munchies/done$', views.munchies_d),
    url(r'^achievements$', views.arr),
    url(r'^login/$', views.logg),
    url(r'^logout/$', views.loggout),

]
