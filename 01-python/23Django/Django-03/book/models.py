from django.db import models





# 图书模型类
# 默认表名: booktest_bookinfo
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, verbose_name='标题')
    # btitle = models.CharField(max_length=20, db_column='title', verbose_name='标题')
    bpub_date = models.DateField(verbose_name='出版日期')
    # bpub_date = models.DateField(auto_now_add=True, verbose_name='出版日期')
    # bpub_date = models.DateField(auto_now=True, verbose_name='出版日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')

    image = models.ImageField(upload_to='book', verbose_name='图片', null=True)

    class Meta:
        # 指定表名
        db_table = 'tb_books'
        verbose_name = '图书'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.btitle

    def pub_date(self):
        # 返回图书的出版日期
        return self.bpub_date

    pub_date.short_description = '出版日期'
    pub_date.admin_order_field = 'bpub_date'


# 英雄人物模型类
class HeroInfo(models.Model):
    GENDER_CHOICES = (
        (0, '男'),
        (1, '女')
    )
    hname = models.CharField(max_length=20, verbose_name='名称')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='备注信息')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')
    # 外键关联属性
    # 表外键字段名格式: <外键关联属性名>_id
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE, verbose_name='所属图书')

    class Meta:
        db_table = 'tb_heros'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname

    # 这个关联是可以查询到1~n当中1里卖的内容
    def read(self):
        # 返回英雄人物所属图书的阅读量
        return self.hbook.bread

    read.short_description = '阅读量'
    read.admin_order_field = 'hbook__bread'