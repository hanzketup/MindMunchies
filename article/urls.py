from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.rand),
    url(r'(?P<pk>\d+)/$', views.get)

]