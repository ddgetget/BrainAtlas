__all__ = ["Student", "sum_num"]  # 提示： 以后外面使用from 模块名 import * 的使用只能导入指定的功能代码，不会影响import导入的方式

# 第一个模块, 可以有类， 函数， 全局变量

# 定义关键变量
g_num = 10


# 定义类
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("我的名字:%s 年龄:%d" % (self.name, self.age))

# 定义函数
def sum_num(num1, num2):
    return num1 + num2


# 匿名函数
func_name = lambda x: True if x % 2 == 0 else False


