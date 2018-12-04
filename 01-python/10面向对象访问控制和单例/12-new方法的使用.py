# 创建对象会执行两个方法，1. __new__： 创建对象  2. __init__: 给对象的添加属性及初始化


class Student(object):

    # 创建对象会执行__new__
    # 提示： 使用不定长参数兼容init方法里面的参数
    def __new__(cls, *args, **kwargs):
        print("new:", args, kwargs)
        print("创建对象会执行__new__方法")
        return object.__new__(cls)

    # # 给创建成功的对象添加属性及初始化
    # def __init__(self, name, age, sex):
    #     print("我是初始化init方法")
    #     self.name = name
    #     self.age = age
    #     self.sex = sex

    def __init__(self):
        print("我是初始化init方法")



# 创建学生对象
# xiao_bai = Student("李四", 20, "男")
# print(xiao_bai.name, xiao_bai.age)
#
# xiao_lan = Student(name="王五", age=18, sex="女")
# print(xiao_lan.name, xiao_lan.age, xiao_lan.sex)

stu = Student()
