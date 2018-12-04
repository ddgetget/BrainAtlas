# __slots__ ： 固定化对象属性，不让对象随便添加对象属性


class Student(object):

    # 添加一个魔法属性固定化对象属性
    __slots__ = ("name", "age", "__sex")

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__sex = "男"

    def get_sex(self):
        return self.__sex

# 创建对象
stu = Student("李四", 20)
# 添加了一个对象属性, 使用__slots__就不能随便添加额外的属性
# stu.sex = "男"
# 可以修改已有的属性，不能添加属性
stu.name = "王菲"

print(stu.name, stu.age)
print(stu.get_sex())


# stu1 = Student("王五", 21)
# print(stu1.name, stu1.age, stu1.sex)