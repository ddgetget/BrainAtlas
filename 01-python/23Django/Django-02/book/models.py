
from django.db import models

# Create your models here.


# 图书管理模型
class BookInfo(models.Model):
    title = models.CharField(max_length=20,verbose_name='标题')
    pub_data = models.DateField(verbose_name='出版日期')
    read_count = models.IntegerField(default=0,verbose_name='阅读数量')
    comment_count = models.IntegerField(default=0,verbose_name='评论量')
    is_delete = models.BooleanField(default=False,verbose_name='删除标记')

    class Meta:
        db_table = 'books'