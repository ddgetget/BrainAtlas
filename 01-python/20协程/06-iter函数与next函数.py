# iter函数获取可迭代对象的迭代器，会调用可迭代对象身上的__iter__方法
# next函数获取迭代器对象的下一个值，会调用迭代器对象身上的__next__方法

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
        # print("next")
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


# 使用iter函数获取可迭代对象身上的迭代器对象， 会调用可迭代对象的__iter__方法
my_iterator = iter(my_list)

print(my_iterator)


# 使用next函数获取迭代器中的下一个值，会调用迭代器对象身上的__next__方法

# value = next(my_iterator)
# print(value)
#
# value = next(my_iterator)
# print(value)
#
# value = next(my_iterator)
# print(value)

# while 循环内部没有捕获停止迭代的异常，需要自己处理
# while True:
#     try:
#         value = next(my_iterator)
#         print(value)
#     except StopIteration:
#         break
#

# 总结： for循环的本质
# 如果for循环遍历的是可迭代对象那么先通过iter函数获取可迭代对象身上的迭代器，然后在通过next函数一次获取迭代器中每一个值
# 如果for循环遍历的是迭代器，那么直接通过next函数异常获取迭代器中的每一个值
# for循环内部自己捕获停止的迭代的异常，程序员不需要自己捕获异常

# 使用for循环直接遍历迭代器
for value in my_iterator:
    print(value)
