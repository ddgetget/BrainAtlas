from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.


# 从url地址中提取参数
from django.urls import reverse


def profile(request, name, age):
    return HttpResponse("OK")


# 获取查询字符串参数
# /query/
def query_data(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')

    # 返回key的多个values
    c_list = request.GET.getlist(c)

    return HttpResponse('OK')


# 获取请求体表单数据
# /form/
def form_data(request):
    name = request.get('name')
    age = request.get('age')
    return HttpResponse('Ok')


# 获取请求体json数据
# /json/
def json_data(request):
    req_data = request.body
    # 注意：上面返回的是byte数据

    # bytes数据转为str
    json_str = req_data.decode()

    import json
    req_dict = json.loads(json_str)

    # 获取数据
    name = req_dict.get('name')
    age = req_dict.get('age')

    return HttpResponse('ok')


# 响应头对象的创建
# /get_response/
def get_response(request):
    response = HttpResponse('responses data', content_type='text/html', status=201)
    # 向响应头中添加数据
    response['Name'] = 'TuringEmmy'

    return response


# 响应是返回json数据
# /get_json/
def get_json(request):
    res_data = {
        'name': 'Turing',
        'age': 19
    }
    return JsonResponse(res_data)


# 响应时，页面重定向到/users/index/
# /redirect/
def redirect_demo(request):
    res_url = reverse('users:index')
    return redirect(res_url)


# /set_session/
def set_session(request):
    """设置session信息"""
    request.session['name'] = 'Turing'
    request.session['age'] = 23

    return HttpResponse('OK')


# /get_session/
def get_session(request):
    """获取session"""
    name = request.session.get('name')
    age = request.session.get('age')

    return HttpResponse("%s:%s" % (name, age))

# /del_session/
def del_session(request):
    """清楚session的信息"""
    # request.session.clear()
    request.session.flush()

    return HttpResponse("OK")
