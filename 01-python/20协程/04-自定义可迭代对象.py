# 自定义可迭代对象： 在类里面定义一个__iter__的方法创建的对象就是可迭代对象
from collections import Iterable


class MyList(object):

    def __init__(self):
        # 创建空列表属性
        self.my_list = list()

    def add_data(self, data):
        # 把数据添加到指定列表里面
        self.my_list.append(data)

    def __iter__(self):
        # 返回迭代器，迭代器就是负责把数据依次获取出来的
        # 总结： 可迭代对象的本质是通过迭代器把数据依次获取出来的
        pass


my_list = MyList()
my_list.add_data("hello")
my_list.add_data("world")

result = isinstance(my_list, Iterable)
print(result)

for value in my_list:
    print(value)
