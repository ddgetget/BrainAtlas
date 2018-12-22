from django.apps import AppConfig


class BookConfig(AppConfig):
    name = 'book'
    # 确保菜单蓝线是中文'图书管理'
    verbose_name = '图书管理'
