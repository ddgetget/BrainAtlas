# author        TuringEmmy 
# createtime    18-10-16  下午4:19
# coding=utf-8
# doc           PyCharm
from django.conf.urls import url

from classview import views

urlpatterns = [
    url(r'register/$', views.RegisterView.as_view()),
    url(r'demoview/$', views.DemoView.as_view()),

]
