### 一、状态保持

1. Django中的cookies设置和获取

默认是开启的

```python
# 如果存储在数据库中，需要在项INSTALLED_APPS中安装Session应用。
    'django.contrib.sessions',
```

存储有下面几种方式，如果在mysql当中，对应的表是:django_session_

```python
# session存储在数据库当中，如下设置可以写，也可以不写，这是默认存储方式。
# 数据库，默认存储
# SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# 本地存储
# SESSION_ENGINE='django.contrib.sessions.backends.cache'
# # 混合存储
# SESSION_ENGINE='django.contrib.sessions.backends.cached_db'
```



2. 设置cookies的存储到redis

```python
# 在redis中保存session，需要引入第三方扩展，我们可以使用django-redis来解决
CACHES={
"default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
```

> 注：如果redis的ip地址不是本地回环127.0.0.1，而是其他地址，访问Django时，可能出现Redis连接错误

```haskell
# sudo vim /etc/redis/redis.conf
# sudo service redis-server restart
```

在redis.conf配置文件后面添加,配置项进行修改（如要添加10.211.55.5地址）

```
bind 127.0.0.1 10.211.55.5
```

3. session的设置获取清除

```python
request.session[key] = value	# 以键值对的格式写session
request.session.get(key,value)	# 根据键读取值
request.session.clear()			# 清除所有的session，只删除值
request.session.flush()			# 清除session数据，整条的删除
del reqeust.session[key]		# 删除指定键及值
request.session.set_expiry(value)		# 设置session的有效期
```

> value为None,session有效期采用默认值，默认两周.可以在setting.py中设置SESSION_COOKIE_AGE来设置全局默认值

### 二、类视图

1.  类视图简介

以函数的方式定义的视图称为**函数视图**，函数视图便于理解

2. 基本用法

- **代码可读性好**
- **类视图相对于函数视图有更高的复用性**

**配置路由时，使用类视图的as_view()方法来添加**。

```python
from django.views.generic import View

class RegisterView(View):
    """类视图：处理注册"""

    def get(self, request):
        """处理GET请求，返回注册页面"""
        return render(request, 'register.html')

    def post(self, request):
        """处理POST请求，实现注册逻辑"""
        return HttpResponse('这里实现注册逻辑')
```

3. 原理说明

参看源代码的as_view函数和dispatch方法

### 三、类视图装饰器

1. 类视图装饰器引入

```python
def my_decorator(func):
    def wrapper(request, *args, **kwargs):
        print('自定义装饰器被调用了')
        print('请求路径%s' % request.path)
        return func(request, *args, **kwargs)
    return wrapper
```



2. url配置时添加装饰器的行为

```python
urlpatterns = [
    # 类视图：注册
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
]
```

或者在类视图中使用

```python
# 为全部请求方法添加装饰器
@method_decorator(my_decorator, name='dispatch')
class DemoView(View):
    pass
# -------------------------------------------------------------
# 为特定请求方法添加装饰器
@method_decorator(my_decorator, name='get')
class DemoView(View):
    def get(self, request):
        print('get方法')
        return HttpResponse('ok')
```

**如果需要为类视图的多个方法添加装饰器，但又不是所有的方法（为所有方法添加装饰器参考上面例子），可以直接在需要添加装饰器的方法上使用method_decorator**

```python
class DemoView(View):

    @method_decorator(my_decorator)  # 为get方法添加了装饰器
    def get(self, request):
        print('get方法')
        return HttpResponse('ok')
        ....
```

3. Mixin扩展类说明&类视图

```python
class ListModelMixin(object):
    """
    list扩展类
    """
    def list(self, request, *args, **kwargs):
        ...

class CreateModelMixin(object):
    """
    create扩展类
    """
    def create(self, request, *args, **kwargs):
        ...

class BooksView(CreateModelMixin, ListModelMixin, View):
    """
    同时继承两个扩展类，复用list和create方法
    """
    def get(self, request):
        self.list(request)
        ...

    def post(self, request):
        self.create(request)
        ...

class SaveOrderView(CreateModelMixin, View):
    """
    继承CreateModelMixin扩展类，复用create方法
    """
    def post(self, request):
        self.create(request)
        ...
```

### 四、中间件

1. 中间件基本使用

```python
def simple_middleware(get_response):
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次。
    def middleware(request):
        # 此处编写的代码会在每个请求处理视图前被调用。
        response = get_response(request)
        # 此处编写的代码会在每个请求处理视图之后被调用。
        return response
    return middleware
```

2. 多个中间件调用的顺序

`请求前顺序，请求后逆序`

### 五、模板

1. 模板目录配置和使用

setting.py的TEMPLATES 进行 修改

```
'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 此处修改
```

2. 模板的完整步骤

找到模板 loader.get_template-->渲染模板模板对象.render(context=None, request=None)

3. 模板渲染的本质

这里就可以明显的区分前后端分离还是部分离，将html读取到服务器渲染后，整体送到客户端的是前后端不分离的

4. 模板变量%控制语句&过滤器&继承

```
{{变量}}
# ---------------------
{% for item in 列表 %}

循环逻辑
{{forloop.counter}}表示当前是第几次循环，从1开始
{%empty%} 列表为空或不存在时执行此逻辑

{% endfor %}
# --------------------------------
{% if ... %}
逻辑1
{% elif ... %}
逻辑2
{% else %}
逻辑3
{% endif %}
# -----------------------------

```

> ```python
> {% if a == 1 %}  # 正确
> {% if a==1 %}  # 错误
> ```

过滤器和Flask不一样

```
变量|过滤器:参数
```

- **safe**，禁用转义，告诉模板这个变量是安全的，可以解释执行


- **length**，长度，返回字符串包含字符的个数，或列表、元组、字典的元素个数。

- **default**，默认值，如果变量不存在时则返回默认值。

  ```
  data|default:'默认值'
  ```

- **date**，日期，用于对日期类型的值进行字符串格式化，常用的格式化字符如下：

  - Y表示年，格式为4位，y表示两位的年。
  - m表示月，格式为01,02,12等。
  - d表示日, 格式为01,02等。
  - j表示日，格式为1,2等。
  - H表示时，24进制，h表示12进制的时。
  - i表示分，为0-59。
  - s表示秒，为0-59。

  ```
  value|date:"Y年m月j日  H时i分s秒"
  ```

  ​

### 六、数据库

1. ORM框架的介绍

O是object，也就**类对象**的意思，R是relation，翻译成中文是关系，也就是关系数据库中**数据表**的意思，M是mapping，是**映射**的意思。

1. 数据库的配置

```
# 1. 使用MySQL数据库首先需要安装驱动程序
pip install PyMySQL

#　2.在Django的工程同名子目录的__init__.py文件中添加如下语句
from pymysql import install_as_MySQLdb
install_as_MySQLdb()
#　作用是让Django的ORM能以mysqldb的方式来调用PyMySQL。

#　3．修改DATABASES配置信息

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'mysql',  # 数据库用户密码
        'NAME': 'database_name'  # 数据库名字
    }
}
```



3. 模型定义&数据库的迁移

```python
class BookInfo(models.Model):
    title = models.CharField(max_length=20, verbose_name='名称')
    pub_date = models.DateField(verbose_name='发布日期')
    class Meta:
        db_table = 'book'
```

字段介绍

| 类型               | 说明                                       |
| ---------------- | ---------------------------------------- |
| AutoField        | 自动增长的IntegerField，通常不用指定，不指定时Django会自动创建属性名为id的自动增长属性 |
| BooleanField     | 布尔字段，值为True或False                        |
| NullBooleanField | 支持Null、True、False三种值                     |
| CharField        | 字符串，参数max_length表示最大字符个数                 |
| TextField        | 大文本字段，一般超过4000个字符时使用                     |
| IntegerField     | 整数                                       |
| DecimalField     | 十进制浮点数， 参数max_digits表示总位数， 参数decimal_places表示小数位数 |
| FloatField       | 浮点数                                      |
| DateField        | 日期， 参数auto_now表示每次保存对象时，自动设置该字段为当前时间，用于"最后一次修改"的时间戳，它总是使用当前日期，默认为False； 参数auto_now_add表示当对象第一次被创建时自动设置当前时间，用于创建的时间戳，它总是使用当前日期，默认为False; 参数auto_now_add和auto_now是相互排斥的，组合将会发生错误 |
| TimeField        | 时间，参数同DateField                          |
| DateTimeField    | 日期时间，参数同DateField                        |
| FileField        | 上传文件字段                                   |
| ImageField       | 继承于FileField，对上传的内容进行校验，确保是有效的图片         |

选项介绍

| 选项          | 说明                                       |
| ----------- | ---------------------------------------- |
| null        | 如果为True，表示允许为空，默认值是False                 |
| db_column   | 字段的名称，如果未指定，则使用属性的名称                     |
| db_index    | 若值为True, 则在表中会为此字段创建索引，默认值是False         |
| default     | 默认                                       |
| primary_key | 若为True，则该字段会成为模型的主键字段，默认值是False，一般作为AutoField的选项使用 |
| unique      | 如果为True, 这个字段在表中必须有唯一值，默认值是False         |

迁移命令

```
python manage.py makemigrations
python manage.py migrate
```


