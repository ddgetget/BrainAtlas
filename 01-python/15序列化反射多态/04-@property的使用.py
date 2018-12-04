class Student(object):

    __slots__ = ["name", "__age"]

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # 获取年龄
    @property
    def age(self):
        return self.__age

    # 设置年龄
    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def sex(self):
        return "女"



    def show(self):
        print(self.name, self.__age)


student = Student("古力娜扎", 25)

# 使用属性设置年龄和获取年龄
# print(student.get_age)
# student.set_age = 20
# print(student.get_age)
print(student.age)
student.age = 20
print(student.age)
print(student.sex)



# student.sex = "女"
# student.show()
#
# student.set_age(26)
# age = student.get_age()
#
# print(age)



