from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def index(request):
    """
    第一个视图函数
    :param request:
    :return:
    """
    # 返回的HttpResponse响应对象
    return HttpResponse("hello ,my name is TuringEmmy")

# 访问say函数
# /users/say
def say(request):
    return HttpResponse(' talk something')

# url反向解析：根据视图火球对应的url地址
# /users/url_reverse/
def url_reverse(request):
    res_url = reverse('users:index')
    return HttpResponse(res_url)