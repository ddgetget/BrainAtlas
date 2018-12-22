
### Django基本

##### 1. django框架简介

1）重量级框架

2）MVT模式

##### 2. 使用Django创建项目和子应用

1）创建Django项目工程

```bash
django-admin startproject 项目名称
```

2）创建Django子应用

```
python manage.py startapp 子应用名称
```

> 注: 子应用创建之后需要进行注册 settings.py配置文件中INSTALLED_APPS

##### 3. Django中定义视图和url配置

1）定义视图

在子应用下面views.py文件定义视图函数

```python
# /index/
def index(request):
	# 返回响应对象
	return HttpResponse('index')
```

2）进行url配置

在子应用中进行url配置

```python
# urls.py

urlpatterns = [
	url(r'^index/$', views.index), 
]
```

在总的urls文件中进行包含

```python
urlpatterns = [
    url(r'^', include('users.urls')),
]
```

> 注: 
>
> 1. Django中默认url地址风格: 末尾加/
> 2. 建议在子应用中进行url配置时，严格匹配开头和结尾

##### 4. url地址反向解析

在子应用中进行url配置指定name

```python
# urls.py
urlpatterns = [
	url(r'^index/$', views.index, name='index'), 
]
```

在总的urls文件中进行包含指定namespace

```python
urlpatterns = [
    url(r'^', include('users.urls', namespace='users')),
]
```

> reverse('namespace:name')，配合页面重定向使用

##### 5. 请求

客户端向服务器传递参数的途径：

1. 通过url地址传递参数

2. 查询字符串 ?a=1&b=2&c=3

3. 通过请求体传递数据

4. 通过请求头传递参数

   ```
   $.ajax({
       'headers': {
           'X-CSRFToken': 'token'
       },
       ...
   }
   ```

##### 6. 响应

1）构造响应对象

```python
response = HttpResponse('响应体', content_type='响应数据类型', status='响应状态码')

# 向响应头加数据
response['<key>'] = '<value>'
```

2）返回json数据

```python
return JsonResponse(<dict>)
```

3）页面重定向

```python
return redirect('重定向的url地址')
```


