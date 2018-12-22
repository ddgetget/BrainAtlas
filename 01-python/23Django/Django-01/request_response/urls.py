# author        TuringEmmy 
# createtime    18-10-15  下午7:36
# coding=utf-8
# doc           PyCharm
from django.conf.urls import url

from request_response import views

urlpatterns = [
    # url(r'^profile/([a-z]+)/(\d{4})/$', views.profile),
    url(r'^profile/(?P<name>[a-z]+)/(?P<age>\d{4})/$', views.profile),
    url(r'^query/$',views.query_data),
    url(r'^form/$',views.form_data),
    url(r'^json/$',views.json_data),
    url(r'get_response/$',views.get_response),
    url(r'get_json/$',views.get_json),
    url(r'redirect/$',views.redirect_demo),

    # 关于session的测试

    url(r'set_session/$',views.set_session),
    url(r'get_session/$',views.get_session),
    url(r'del_session/$',views.del_session),

]
