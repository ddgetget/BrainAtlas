### 一、http协议

HTTP是客户端浏览器或其他程序与web服务器之间的应用层通信协议

HTTP是一个客户端和服务器请求和应答的标准

1. 请求体

客户端发送一个HTTP请求到服务器的请求消息包括

- 请求行(request line)
- 请求头(header)
- 空行
- 请求体


2. 响应体

服务器接受并处理客户端发过来的请求后会返回一个HTTP的响应消息

HTTP响应也是由四部分组成

状态行，响应头，空行和响应体

3. url

URL，、全称UniformResourceLocator,统一资源定位符

4. 请求方法

> 只有POST，PUT， DELETE，PATCH访问一个url地址时，才可以携带请求体数据，

### 二、web框架和web服务器之间的关系

| 服务器               | 框架                   |
| ----------------- | -------------------- |
| 解析请求报文，调用框架程序处理请求 | 路由分发(根据url找到对应的处理函数) |
| 组织响应报文，返回内容给客户端   | 进行业务的处理              |

Flask和Django中的request对象属性的对比

| Flask   | Django  | 说明              |
| ------- | ------- | --------------- |
| args    | GET     | 查询字符串参数         |
| form    | POST    | 请求体中的表单数据       |
| data    | body    | 请求体中的非表单数据      |
| method  | method  | 请求方法            |
| path    | path    | 请求的url地址(不含域名)  |
| headers | META    | 请求头             |
| cookies | COOKIES | 客户端发送的cookies信息 |
| files   | FILES   | 客户端上传的文件        |

### 三、web框架的学习方法

- 如何搭建工程程序
  - 工程的组建
  - 工程的配置
  - 路由定义
  - 视图函数定义
- 如何获取请求数据（操作request对象）
- 如何构造响应数据（构造response对象）
- 如何使用中间层
- 框架提供的其他功能组件的使用
  - 数据库
  - 模板
  - admin

### 四、Django框架

Django的**主要目的是简便、快速的开发数据库驱动的网站。**

这是一个重量级的框架，主要包括下面的一些常用功能

- 提供项目工程管理的自动化脚本工具


- 数据库ORM支持（对象关系映射，英语：Object Relational Mapping）
- 模板
- 表单
- Admin管理站点
- 文件管理
- 认证权限
- session机制
- 缓存

### 五、Django框架环境搭建

1. 创建虚拟环境

```haskell
mkvirtualenv django_py3_1.11 -p web_vir
```

2. 安装Django

```
pip install django
```

3. 虚拟环境和pip命令

```
# 虚拟环境
mkvirtualenv  # 创建虚拟环境
rmvirtualenv  # 删除虚拟环境
workon  # 进入虚拟环境、查看所有虚拟环境
deactivate  # 退出虚拟环境

# pip
pip install  # 安装依赖包
pip uninstall  # 卸载依赖包
pip list  # 查看已安装的依赖包
pip freeze  # 冻结当前环境的依赖包
```

### 六、Django项目工程创建

```
django-admin startproject web_demo
```

目录说明:

1. settings.py是项目的整体配置文件。
2. urls.py是项目的URL配置文件。
3. wsgi.py 是项目与WSGI兼容的Web服务器入口。
4. manage.py 是项目管理文件，通过它管理项目。

运行服务器

```
python manage.py runserver ip:port
```

> django默认工作在调式Debug模式下，如果增加、修改、删除文件，服务器会自动重启。
>
> 按ctrl+c停止服务器。

### 七、Django创建子应用

```python
python manage.py startapp user
```

目录说明

```
admin.py 文件跟网站的后台管理站点配置相关。
apps.py 文件用于配置当前子应用的相关信息。
migrations 目录用于存放数据库迁移历史文件。
models.py 文件用户保存数据库模型类。
tests.py 文件用于开发测试用例，编写单元测试。
views.py 文件用于编写Web应用视图。
```

在工程配置文件settings.py中，**INSTALLED_APPS**项保存当前子应用

```python
'user.apps.UserConfig',
```

### 八、视图函数的定义和url的配置

1. 创建

```python
from django.http import HttpResponse

def index(request):
    """
    index视图
    :param request: 包含了请求信息的请求对象
    :return: 响应对象
    """
    return HttpResponse("hello the world!")
```

> 第一个参数request必须定义，用于接受请求数据的HttpRequest对象
>
> 返回的相依对象，HTTPResponse对象，不是字符串

2. 定义路由

在user/urls.py文件中定义路由信息

```python
from django.conf.urls import url

from . import views

# urlpatterns是被django自动识别的路由列表变量
urlpatterns = [
    # 每个路由信息都需要使用url函数来构造
    # url(路径, 视图)
    url(r'^index/$', views.index),
]
```

3. 在总路由web_dem/urls.py中添加子应用的路由数据

```python
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),  # django默认包含的
    # 添加
    url(r'^users/', include('users.urls')),
]
```



### 九、Django中url匹配的过程及末尾加/

Django中定义路由时，通常以斜线/结尾，其好处是用户访问不以斜线/结尾的相同路径时，Django会把用户重定向到以斜线/结尾的路径上，而不会返回404不存在

- 使用include来将子应用users里的全部路由包含进工程路由中；
- **r'^users/'** 决定了users子应用的所有路由都已**/users/**开头，如我们刚定义的视图index，其最终的完整访问路径为**/users/index/**。

### 十、子应用url的配置，匹配开头和结尾

见九

### 十一、url地址的反向解析

其中include里面添加namespace =‘users’,子应用添加name='index'

```
 url = reverse('users:index')  # 返回 /users/index/
```



### 十二、url总结

1. url路径参数

- 未命名参数按定义顺序传递， 如

  ```
  url(r'^weather/([a-z]+)/(\d{4})/$', views.weather),

  def weather(request, city, year):
      print('city=%s' % city)
      print('year=%s' % year)
      return HttpResponse('OK')

  ```

- 命名参数按名字传递，如

  ```
  url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather),

  def weather(request, year, city):
      print('city=%s' % city)
      print('year=%s' % year)
      return HttpResponse('OK')
  ```

### 十三、参数获取

1. Django中的QueryDic对象

- 方法get()：根据键获取值

```
dict.get('键',默认值)
可简写为
dict['键']
```

- 方法getlist()

```
dict.getlist('键',默认值)
```

3. 查询字符串Qyery String(形如?k1=v1&k2=v2&k2=v3)

```python
a = request.GET.get('k1')
b = request.GET.get('k2')
alist = request.GET.getlist('k2')  # 这个会把v2和v3拼接
```

3. 请求体

>  可以发送请求体数据的请求方有**POST**、**PUT**、**PATCH**、**DELETE**

如果使用postman进行测试需要关闭setting.py的csrf

4. FormData和NonFormData

```python
a = request.POST.get('a')
print(a)
# 对于非表单数据
{"a": 1, "b": 2}
import json

def get_body_json(request):
    json_str = request.body
    json_str = json_str.decode()  # python3.6 无需执行此步
    req_data = json.loads(json_str)
    print(req_data['a'])
    print(req_data['b'])
    return HttpResponse('OK')
```

5. 请求头

可以通过**request.META**属性获取请求头headers中的数据，**request.META为字典类型**。

常见请求头

- `CONTENT_LENGTH` – The length of the request body (as a string).
- `CONTENT_TYPE` – The MIME type of the request body.
- `HTTP_ACCEPT` – Acceptable content types for the response.
- `HTTP_ACCEPT_ENCODING` – Acceptable encodings for the response.
- `HTTP_ACCEPT_LANGUAGE` – Acceptable languages for the response.
- `HTTP_HOST` – The HTTP Host header sent by the client.
- `HTTP_REFERER` – The referring page, if any.
- `HTTP_USER_AGENT` – The client’s user-agent string.
- `QUERY_STRING` – The query string, as a single (unparsed) string.
- `REMOTE_ADDR` – The IP address of the client.
- `REMOTE_HOST` – The hostname of the client.
- `REMOTE_USER` – The user authenticated by the Web server, if any.
- `REQUEST_METHOD` – A string such as `"GET"` or `"POST"`.
- `SERVER_NAME` – The hostname of the server.
- `SERVER_PORT` – The port of the server (as a string).

```python
print(request.META['CONTENT_TYPE'])
```

6. 其他常用HttpRequest对象属性

| 对象属性     | 解释                                     |
| -------- | -------------------------------------- |
| method   | 一个字符串，表示请求使用的HTTP方法，常用值包括：'GET'、'POST' |
| user     | 请求的用户对象                                |
| path     | 一个字符串，表示请求的页面的完整路径，不包含域名和参数部分。         |
| encoding | 一个字符串，表示提交的数据的编码方式(可自行修改)              |
| FILES    | 一个类似于字典的对象，包含所有的上传文件                   |

### 十四、Django的常用配置

1. BASE_DIR

```
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
```

2. DEBUG

默认初始值为True

- 修改代码，程序自动重启
- Django程序出现异常，向前端显示详细错误追踪信息

3. 本地语言与时区

```
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
```

### 十五、Django中的静态文件

setting.py中修改鼎泰文件的参数

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),				# 这是文件地址的拼接，static是动态文件夹的名字
]
```



###
