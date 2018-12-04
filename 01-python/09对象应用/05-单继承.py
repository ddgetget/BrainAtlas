# 单继承： 子类只继承一个父类，可以使用父类的属性和方法
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.money = "100万"

    def show(self):
        print(self.name, self.age)


# 学生类
class Student(Person):
    pass


# 创建学生对象
student = Student("李四", 20)
student.show()

print(student.name, student.age, student.money)