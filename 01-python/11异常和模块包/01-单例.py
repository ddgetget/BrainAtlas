# 单例： 不管对象创建多少次，那么对象实例只有一个，不会创建多个实例
class Singleton(object):

    # 类属性
    __singleton = None
    # 是否第一次初始化
    __is_ok = True

    # 创建对象会执行new方法
    def __new__(cls, *args, **kwargs):
        # if cls.__singleton == None:
        if not cls.__singleton:
            # 创建对象
            cls.__singleton = object.__new__(cls)

        return cls.__singleton

    def __init__(self, name, age):
        # 提示： init初始化操作这步可以省略，但是new方法里面的判断不能省略
        if self.__class__.__is_ok:
            # 建议以后如果自己提供了init方法需要调用父类的init方法，防止出现问题
            super(Singleton, self).__init__()
            self.name = name
            self.age = age
            # 初始化完成
            self.__class__.__is_ok = False


s1 = Singleton("张三", 18)
s2 = Singleton("李四", 20)
print(s1, s2)
print(s1.name, s1.age)
print(s2.name, s2.age)

# class Student(object):
#     pass
#
# stu = Student()
# stu.name = "李四"
#
# stu1 = stu
# print(stu, stu1)
# stu1.name = "张三"
# print(stu, stu1, stu.name)
