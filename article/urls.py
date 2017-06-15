from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^munchie/$', views.rand),
    url(r'munchie/(?P<pk>\d+)/$', views.get),
    url(r'me$', views.me),
    url(r'^my-munchies$', views.mymunchies),
    url(r'^login/$', views.logg),

]
