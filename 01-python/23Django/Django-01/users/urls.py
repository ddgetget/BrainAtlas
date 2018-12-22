# author        TuringEmmy 
# createtime    18-10-15  下午6:18
# coding=utf-8
# doc           PyCharm
from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^say/$', views.say),
    url(r'^url_reverse/$', views.url_reverse),
]
