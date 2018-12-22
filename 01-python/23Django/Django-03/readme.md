### 一、数据库的模型

1. 模型的定义说明

```python
# class 模型类名(models.Model):
#     # 字段属性 = models.字段类型(选项参数)
#
#     class Meta:
#         db_table = '<表名>'
```

2. 外键的属性定义

在设置外键时，需要通过**on_delete**选项指明主表删除数据时，对于外键引用表数据如何处理，在django.db.models中包含了可选常量：

- **CASCADE** 级联，删除主表数据时连通一起删除外键表中数据
- **PROTECT** 保护，通过抛出**ProtectedError**异常，来阻止删除主表中被外键应用的数据
- **SET_NULL** 设置为NULL，仅在该字段null=True允许为null时可用

3. Django交互终端

```python
python manage.py shell
```

以便可以直接在终端中执行测试python语句。

4. mysql日志文件

导入两个模型类，以便后续使用

```
from booktest.models import BookInfo, HeroInfo
```

查看mysql数据库日志

```
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
```

把68，69行前面的#去除，然后保存并使用如下命令重启mysql服务。

```
sudo service mysql restart
```

使用如下命令打开mysql日志文件。

```
tail -f /var/log/mysql/mysql.log  # 可以实时查看数据库的日志内容
# 如提示需要sudo权限，执行
# sudo tail -f /var/log/mysql/mysql.log
```

### 二、数据库操作

1. 增加数据

**save**

```python
from datetime import date
book = BookInfo(
btitle='西游记',
bpub_date=date(1988,1,1),
bread=10,
bcomment=10
```

**create**

```python
HeroInfo.objects.create(
    hname='沙悟净',
    hgender=0,
    hbook=book
)
<HeroInfo: 沙悟净>
```

2. 查询函数(all,get,count)

all

```
# 1. 查询所有图书的数据
    # books = BookInfo.objects.all() # QuerySet类实例对象，类似于列表，查询集
    # print(books)
```

get

```python
# 2. 查询id为1的图书
book = BookInfo.objects.get(id=1) # 返回模型类对象
book = BookInfo.objects.get(pk=1) # 返回模型类对象
print(book)
```

count

```python
# 3. 查询所有图书的数量
res = BookInfo.objects.count()
print(res)
```

2. 查询条件(filter, exclude)

filter

```python
# 1. 查询书名包含'传'的图书。
books = BookInfo.objects.filter(btitle__contains='传') # QuerySet
print(books)

# 4. 查询编号为1或3或5的图书。
# select * from tb_books where id in (1, 3, 5);
# books = BookInfo.objects.filter(id__in=(1, 3, 5))
# print(books)
```

exclude

```python
# 6. 查询编号不等于3的图书。
books = BookInfo.objects.exclude(id=3) # QuerySet
print(books)
```

3. F对象和Q对象

```python
F(属性名)
Q(属性名__运算符=值)
# 2. 查询阅读量大于20，或编号小于3的图书。
books = BookInfo.objects.filter(Q(bread__gt=20) | Q(id__lt=3))
print(books)
# 2. 查询编号不等于3的图书。
books = BookInfo.objects.filter(~Q(id=3))
print(books)
```

4. 聚合和排序

**Avg** 平均，**Count** 数量，**Max** 最大，**Min** 最小，**Sum** 求和，被定义在django.db.models中。

```python
# 1. 查询图书的总阅读量。
res = BookInfo.objects.aggregate(Sum('bread')) # {'bread__sum': 136}
print(res)
# 2. 查询图书总数。
res = BookInfo.objects.aggregate(Count('id')) # {'id__count': 5}
print(res)
# 2. 对所有图书按照阅读量从大到小进行排序。
books = BookInfo.objects.order_by('-bread')
print(books)
```

### 三、数据库关联查询

1. 查询和对象关联的信息

```python
# 1. 查询和id为1的图书关联的英雄人物信息。
heros = HeroInfo.objects.filter(hbook_id=1)
print(heros)
 # 2. 查询和`西游记`关联的英雄人物的信息
book = BookInfo.objects.get(btitle='雪山飞狐')
heros = book.heroinfo_set.all()
print(heros)

# 3. 查询和id为1的英雄人物关联的图书信息。
hero = HeroInfo.objects.get(id=1)
print(hero)

# 获取英雄人物所属图书的id
print(hero.hbook_id)

book = BookInfo.objects.get(id=hero.hbook_id)
print(book)
```

2. 通过模型类进行关联查询

```python
# 1. 查询图书，要求图书中英雄有"孙悟空"。
books = BookInfo.objects.filter(heroinfo__hname='孙悟空')
print(books)

# 2. 查询图书，要求图书中英雄的描述包含"八"。
books = BookInfo.objects.filter(heroinfo__hcomment__contains='八')
print(books)

# 3. 查询书名为“天龙八部”的所有英雄。
heros = HeroInfo.objects.filter(hbook__btitle='天龙八部')
print(heros)

# 4. 查询图书阅读量大于30的所有英雄。
heros = HeroInfo.objects.filter(hbook__bread__gt=30)
print(heros)
```

3. 更新和删除

```python
# 更新
hero = HeroInfo.objects.get(hname='猪八戒')
hero.hname = '猪悟能'
hero.save()

# 返回更新的行数
res = HeroInfo.objects.filter(hname='沙悟净').update(hname='沙僧')
print(res)

# 删除
hero = HeroInfo.objects.get(id=13)
hero.delete()

HeroInfo.objects.filter(id=14).delete()
```

4. 查询集特点和操作

**惰性执行**

创建查询集不会访问数据库，直到调用数据时，才会访问数据库，调用数据的情况包括迭代、序列化、与if合用

例如，当执行如下语句时，并未进行数据库查询，只是创建了一个查询集qs

```python
qs = BookInfo.objects.all()
```

继续执行遍历迭代操作后，才真正的进行了数据库的查询

```python
for book in qs:
    print(book.btitle)
```

**缓存**

```python
# 无法重用缓存，每次查询都会与数据库进行一次交互，增加了数据库的负载
[book.id for book in BookInfo.objects.all()]
[book.id for book in BookInfo.objects.all()]
# 经过存储后，可以重用查询集，第二次使用缓存中的数据。
qs=BookInfo.objects.all()
[book.id for book in qs]
[book.id for book in qs]
```

- all()：返回所有数据。
- filter()：返回满足条件的数据。
- exclude()：返回满足条件之外的数据。
- order_by()：对结果进行排序

查询集可以含有零个、一个或多个过滤器。过滤器基于所给的参数限制查询的结果。

**判断某一个查询集中是否有数据**：

- exists()：判断查询集中是否有数据，如果有则返回True，没有则返回False



### 四、admin站点

1. 本地化，创建管理员，注册模型类

创建管理员,按提示输入用户名、邮箱、密码。

```
python manage.py createsuperuser
```

浏览器打开

```
http://127.0.0.1:8000/admin/
```

2. Admin管理类定义和信息控制

定义管理类需要继承自**admin.ModelAdmin**类

```python
from django.contrib import admin

class BookInfoAdmin(admin.ModelAdmin):
    pass
```

在当前的admin文件里面进行注册

```
admin.site.register(BookInfo)
admin.site.register(HeroInfo)
```

**调整页面展示**

```
list_per_page=100
```

列表中国的列

```
list_display = ['id','btitle']
```

将方法作为列,在model文件的BookInfo中添加pub_date,修改BookInfoAdmin类如下

```python
def pub_date(self):
    # 返回图书的出版日期
    return self.bpub_date
# ---------------------------------------------------
list_display = ['id','btitle','pub_date']
```

但是此时不能最后这个字段不能排序,如果需要排序需要为方法指定排序依据。

```
admin_order_field=模型类字段
```

并在相应的模型类当中

```python
pub_date.short_description = '发布日期'
pub_date.admin_order_field = 'bpub_date'
```

**关联对象**

1）打开book/models.py文件，修改HeroInfo类如下：

```python
class HeroInfo(models.Model):
    ...
    def read(self):
        return self.hbook.bread

    read.short_description = '图书阅读量'
```

2）打开book/admin.py文件，修改HeroInfoAdmin类如下：

```python
class HeroInfoAdmin(admin.ModelAdmin):
    ...
    list_display = ['id', 'hname', 'hbook', 'read']
```

> 这个关联是可以查询到1~n当中1里字段的内容(通过外键实现的)

**右侧栏过滤器**

这里使用到了`list_filter=[]`

打开book/admin.py文件，修改HeroInfoAdmin类如下：

```
class HeroInfoAdmin(admin.ModelAdmin):
    ...
    list_filter = ['hbook', 'hgender']
```

**实现搜索框**

搜索框用到了`search_fields=[]`

1）打开book/admin.py文件，修改HeroInfoAdmin类如下：

```
class HeroInfoAdmin(admin.ModelAdmin):
    ...
    search_fields = ['hname']
```

3. 调整编辑页面

显示字段`fields=[]`

打开book/admin.py文件，修改BookInfoAdmin类如下：

```
class BookInfoAdmin(admin.ModelAdmin):
    ...
    fields = ['btitle', 'bpub_date']
```

> 注意:这里不能使用模型类里面的方法名

分组显示:

```
fieldset=(
    ('组1标题',{'fields':('字段1','字段2')}),
    ('组2标题',{'fields':('字段3','字段4')}),
)
```

打开book/admin.py文件，修改BookInfoAdmin类如下：

```
class BookInfoAdmin(admin.ModelAdmin):
    ...
    # fields = ['btitle', 'bpub_date']
    fieldsets = (
        ('基本', {'fields': ['btitle', 'bpub_date']}),
        ('高级', {
            'fields': ['bread', 'bcomment'],
            'classes': ('collapse',)  # 是否折叠显示
        })
    )
```

关联对象

在一对多的关系中，可以在一端的编辑页面中编辑多端的对象，嵌入多端对象的方式包括表格、块两种。

- 类型InlineModelAdmin：表示在模型的编辑页面嵌入关联模型的编辑。
- 子类TabularInline：以表格的形式嵌入。
- 子类StackedInline：以块的形式嵌入

1）打开book/admin.py文件，创建HeroInfoStackInline类。

```
class HeroInfoStackInline(admin.StackedInline):
    model = HeroInfo  # 要编辑的对象
    extra = 1  # 附加编辑的数量
```

2）打开book/admin.py文件，修改BookInfoAdmin类如下：

```
class BookInfoAdmin(admin.ModelAdmin):
    ...
    inlines = [HeroInfoStackInline]
```

其他的内嵌方式只需要更换所继承的类即可实现

**调整站点信息**

- **admin.site.site_header** 设置网站页头
- **admin.site.site_title** 设置页面标题
- **admin.site.index_title** 设置首页标语

在bookt/admin.py文件中添加一下信息

```
from django.contrib import admin

admin.site.site_header = '这个是浏览器的标题'
admin.site.site_title = '这个是菜单栏的标题'
admin.site.index_title = '这个是页面的标题'
```
**图片上传**

使用到了`pillow`

1. setting.py中设置

````
MEDIA_ROOT=os.path.join(BASE_DIR,"static/media")
````

2. 为模型类添加ImageField字段

```
class BookInfo(models.Model):
    ...
    image = models.ImageField(upload_to='book', verbose_name='图片', null=True)
```

3. 使用admin站点上传图片,添加image字段

```
('基本', {'fields': ['btitle', 'bpub_date','image']}),
```

