from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

# /class/register/
class RegisterView(View):
    """the first view"""
    def get(self,request):
        print('get方法被调用')
        return HttpResponse('返回注册页面')

    def post(self, request):
        print('post方法被调用')
        return HttpResponse('进行注册处理')

    def put(self, request):
        print('put方法被调用')
        return HttpResponse('OK')

# 自定义一个装饰器
def decorator(func):
    def wrapper(request,*args,**kwargs):
        print('装饰器函数被调用')
        print('请求方式为%s'%request.method)
        return func(request,*args,**kwargs)
    return wrapper


# /class/demoview/
# @method_decorator(decorator, name='dispatch')
@method_decorator(decorator, name='get')
class DemoView(View):
    @method_decorator(decorator)
    def get(self, request):
        print('get方法被调用')
        return HttpResponse('OK')

    def post(self, request):
        print('post方法被调用')
        return HttpResponse('OK')
