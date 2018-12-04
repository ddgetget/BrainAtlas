# del魔法方法： 当前对象释放的时候会调用该方法

# 对象销毁: 1. 程序退出程序中的所有对象都会销毁  2. 对象没有变量使用的时候会销毁
import time

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self):
    #     return self.name + "," + str(self.age)

    # 查看对象释放销毁
    # 对象的引用计数为0会调用del方法
    def __del__(self):
        print("对象销毁了:", self)


# 创建对象
student = Student("张三", 18)
student1 = student
print(student)

# 删除变量, 会对应用计数减去1
del student
del student1

time.sleep(5)



# 引用计数： 内存地址使用的次数，当应用计数为0表示对象释放


