class Person(object):
    def __init__(self):
        self.name = '李四'
        # 私有属性
        self.__age = 18

    def show(self):
        print(self.name, self.__age)

    # 私有方法
    def __show_msg(self):
        self.show()


class Student(Person):
    def student_info(self):
        print(self.name)

        # 在子类里面不可以访问父类里面的私有属性和私有方法的
        # print(self.__age)
        # self.__show_msg()

        # print(Person.__dict__)



student = Student()
# student.student_info()

# 访问父类的公有属性
# print(student.name)

# 访问父类的私有属性
# print(student.__age)

# student.show()

# student.__show_msg()

# student.student_info()

# print(Student.__dict__)

# 非常规手段
# 使用父类里面的私有方法
student._Person__show_msg()

# 子类继承父类不能使用父类的私有属性和私有方法
# 子类不能直接访问父类的私有属性和私有方法