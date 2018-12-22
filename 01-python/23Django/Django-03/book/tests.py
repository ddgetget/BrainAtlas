from django.test import TestCase

# Create your tests here.
import os

if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day03.settings")

# 让django进行一次初始化操作
import django
django.setup()

from book.models import BookInfo,HeroInfo



# --------------------------------删除------------------------------

# if __name__ == "__main__":
    # # 更新
    # hero = HeroInfo.objects.get(hname='猪八戒')
    # hero.hname = '猪悟能'
    # hero.save()
    #
    # 返回更新的行数
    # res = HeroInfo.objects.filter(hname='沙悟净').update(hname='沙僧')
    # print(res)
    #
    # 删除
    # hero = HeroInfo.objects.get(id=13)
    # hero.delete()
    #
    # HeroInfo.objects.filter(id=14).delete()


# -----------------------通过模型类实现关联查询----------------------------------
# # if __name__ == "__main__":
# #     # 通过模型类实现关联查询
#     1. 查询图书，要求图书中英雄有"孙悟空"。
#     books = BookInfo.objects.filter(heroinfo__hname='孙悟空')
#     print(books)
#
#     2. 查询图书，要求图书中英雄的描述包含"八"。
#     books = BookInfo.objects.filter(heroinfo__hcomment__contains='八')
#     print(books)
#
#     3. 查询书名为“天龙八部”的所有英雄。
#     heros = HeroInfo.objects.filter(hbook__btitle='天龙八部')
#     print(heros)
#
#     4. 查询图书阅读量大于30的所有英雄。
#     heros = HeroInfo.objects.filter(hbook__bread__gt=30)
#     print(heros)





# ----------------------------------查询和对象关联的信息-----------------------------------
# if __name__ == "__main__":
    # 查询和对象关联的信息
    # 1. 查询和id为1的图书关联的英雄人物信息。
    # book = BookInfo.objects.get(id=1)
    #
    # heros = HeroInfo.objects.filter(hbook_id=1)
    # print(heros)

    # heros = book.heroinfo_set.all()
    # print(heros)

    # 2. 查询和`西游记`关联的英雄人物的信息
    # book = BookInfo.objects.get(btitle='雪山飞狐')
    # heros = book.heroinfo_set.all()
    # print(heros)

    # 3. 查询和id为1的英雄人物关联的图书信息。
    # hero = HeroInfo.objects.get(id=1)
    # print(hero)
    #
    # # 获取英雄人物所属图书的id
    # print(hero.hbook_id)
    #
    # book = BookInfo.objects.get(id=hero.hbook_id)
    # print(book)

    # 获取和英雄关联的图书对象
    # print(hero.hbook)

    # 4. 查询和`孙悟空`关联的图书信息
    # hero = HeroInfo.objects.get(hname='孙悟空')
    # print(hero.hbook)


# ------------------------------聚合-------------------------------------------
# if __name__ == "__main__":
#     # 聚合
#     from django.db.models import Sum, Max, Min, Avg, Count
#
#     # 1. 查询图书的总阅读量。
#     # res = BookInfo.objects.aggregate(Sum('bread')) # {'bread__sum': 136}
#     # print(res)
#
#     # 2. 查询图书总数。
#     # res = BookInfo.objects.aggregate(Count('id')) # {'id__count': 5}
#     # print(res)
#
#     # res = BookInfo.objects.count() # 返回数字
#     # print(res)
#
#     # 排序
#     # 1. 对所有图书按照阅读量从小到大进行排序。
#     # books = BookInfo.objects.order_by('bread')
#     # print(books)
#
#     # # 2. 对所有图书按照阅读量从大到小进行排序。
#     # books = BookInfo.objects.order_by('-bread')
#     # print(books)


# --------------------------------------F对象和Q对象---------------------------------
# if __name__ == "__main__":
    # F对象: 用于查询时字段之间的比较
    # from django.db.models import F

    # 1. 查询阅读量大于等于评论量的图书。
    # books = BookInfo.objects.filter(bread__gte=F('bcomment'))
    # print(books)

    # 2. 查询阅读量大于2倍评论量的图书。
    # books = BookInfo.objects.filter(bread__gte=F('bcomment')*2)
    # print(books)

    # Q对象: 用于查询时条件之间的逻辑关系
    # from django.db.models import Q

    # 1. 查询阅读量大于20，并且编号小于3的图书。
    # books = BookInfo.objects.filter(bread__gt=20, id__lt=3)
    # books = BookInfo.objects.filter(Q(bread__gt=20) & Q(id__lt=3))
    # print(books)

    # 2. 查询阅读量大于20，或编号小于3的图书。
    # books = BookInfo.objects.filter(Q(bread__gt=20) | Q(id__lt=3))
    # print(books)

    # # 3. 查询编号不等于3的图书。
    # books = BookInfo.objects.filter(~Q(id=3))
    # print(books)

# ---------------------------------------条件按查询---------------------------------
# if __name__ == "__main__":
    # 条件查询
    # 1. 查询编号为1的图书。
    # book = BookInfo.objects.get(id=1)
    # book = BookInfo.objects.get(id__exact=1)
    # print(book)

    # 2. 查询书名包含'传'的图书。
    # books = BookInfo.objects.filter(btitle__contains='传') # QuerySet
    # print(books)

    # 3. 查询书名不为空的图书。
    # books = BookInfo.objects.filter(btitle__isnull=False)
    # print(books)

    # 4. 查询编号为1或3或5的图书。
    # select * from tb_books where id in (1, 3, 5);
    # books = BookInfo.objects.filter(id__in=(1, 3, 5))
    # print(books)

    # 5. 查询编号大于3的图书。
    # books = BookInfo.objects.filter(id__gt=3)
    # print(books)

    # 6. 查询编号不等于3的图书。
    # books = BookInfo.objects.exclude(id=3) # QuerySet
    # print(books)

    # 7. 查询1980年发表的图书。
    # books = BookInfo.objects.filter(bpub_date__year=1980)
    # print(books)

    # 8. 查询1980年1月1日后发表的图书。
    # books = BookInfo.objects.filter(bpub_date__gt='1980-1-1')
    # print(books)

# -------------------------------------------查询学习---------------------------------------------------
# if __name__ == "__main__":
    # 1. 查询所有图书的数据
    # books = BookInfo.objects.all() # QuerySet类实例对象，类似于列表，查询集
    # print(books)

    # # 2. 查询id为1的图书
    # book = BookInfo.objects.get(id=1) # 返回模型类对象
    # book = BookInfo.objects.get(pk=1) # 返回模型类对象
    # print(book)

    # 3. 查询阅读量为10的图书
    # book = BookInfo.objects.get(bread=10)
    # print(book)

    # try:
    #     book = BookInfo.objects.get(id=6)
    # except BookInfo.DoesNotExist:
    #     print('图书不存在')
    #
    # # 4. 查询所有图书的数量
    # res = BookInfo.objects.count()
    # print(res)
