# 自定义可迭代对象： 在类里面定义一个__iter__的方法创建的对象就是可迭代对象
from collections import Iterable
from collections import Iterator


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
        my_iterator = MyIterator(self.my_list)

        result = isinstance(my_iterator, Iterator)
        print("my_iterator:", result)
        return my_iterator


# 自定义迭代器对象: 在类里面定义一个__iter__和一个__next__的方法创建的对象就是迭代器对象
# 迭代器对象的作用： 记录数据的位置及根据这个位置获取对应的数据
class MyIterator(object):

    def __init__(self, my_list):
        self.my_list = my_list
        # 当前获取数据的下标
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.my_list):
            # 迭代器通过next方法获取数据对象中的下一个数据
            value = self.my_list[self.index]

            self.index += 1

            return value
        else:
            # 必须抛出一个停止迭代的异常
            raise StopIteration



# 创建了可迭代对象，能使用for循环遍历取值，可迭代对象是通过迭代器对象依次获取数据的
my_list = MyList()
my_list.add_data("hello")
my_list.add_data("world")

# result = isinstance(my_list, Iterable)
# print(result)

for value in my_list:
    print(value)
