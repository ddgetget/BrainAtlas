# 可迭代对象有: 列表、字典、元组、字符串、range、集合等
from collections import Iterable

# 判断对象是否是指定类型
result = isinstance([1,2], Iterable)

print(result)


# 判断对象是否是指定类型
result = isinstance((1,2), Iterable)

print(result)


# 判断对象是否是指定类型
result = isinstance({"name": "李四"}, Iterable)

print(result)



# 判断对象是否是指定类型
result = isinstance("123", Iterable)

print(result)



# 判断对象是否是指定类型
result = isinstance(range(3), Iterable)

print(result)


# 判断对象是否是指定类型
result = isinstance({3, 5}, Iterable)

print(result)


# num = 5
#
# for value in num:
#     print(value)

# 判断对象是否是指定类型
result = isinstance(5, int)

print(result)



# def show(name):
#     if isinstance(name, str):
#         print("是字符串")
#     else:
#         print("不是字符串")
#
# 
# show("李四")

class A(object):
    pass

a = A()
result = isinstance(a, A)
print(result)
# for value in a:
#     print(value)

