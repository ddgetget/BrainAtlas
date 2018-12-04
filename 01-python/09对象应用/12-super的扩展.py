# 单继承的情况

# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Student(Person):
#     def __init__(self, subject):
#         # 调用父类的init方法
#         # super().__init__("李四", 20)
#
#         # 第一个参数表示创建那个父类的对象
#         super(Student, self).__init__("李四", 20)
#         self.subject = subject
#
#
# student = Student("python")
#
# print(student.name, student.age, student.subject)


# 多继承

class Father(object):
    def __init__(self, money):
        self.money = money

    def show(self):
        print("father show")


class Person(object):
    def __init__(self, name, age):
        # 调用Peron类的父类对象的init方法
        # 其实是获取的是指定类的类继承顺序中的下一个类
        super(Person, self).__init__(100)
        self.name = name
        self.age = age

    def show(self):
        print("Person show")

class Student(Person, Father):
    def __init__(self, subject):
        # 调用父类的init方法
        # super().__init__("李四", 20)

        # 第一个参数表示创建那个父类的对象
        super(Student, self).__init__("李四", 20)


        # 调用两个父类的init方法
        # Person.__init__(self, "李四", 20)
        # Father.__init__(self, 100)

        self.subject = subject

    def show(self):
        # 根据指定的类在类继承顺序中找下一个类的对象调用指定对象的方法
        super(Person, self).show()

student = Student("python")
# 方法的调用也是遵循mro类继承顺序的，
student.show()

# print(student.name, student.age, student.subject, student.money)


# 类的继承顺序mro()
# 提示一下： super调用父类对象的方法是遵循mro类继承顺序的， 最终是object
result = Student.mro()
print(result)



