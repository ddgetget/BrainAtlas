# author        TuringEmmy 
# createtime    18-10-16  下午5:22
# coding=utf-8
# doc           PyCharm
from django.conf.urls import url

from template_demo import views

urlpatterns=[
    url(r'use_template/$',views.TemplateView.as_view())
]