class Person(object):

    def study(self):
        print("正在学习")


class Student(Person):

    def __init__(self, name):
        self.name = name
    # 重写父类的方法，目标是对父类的方法进行扩展或者修改

    # 重写的前提是必须要有继承关系，方法名相同，但是功能实现不同
    def study(self):
        print("%s正在学习" % self.name)


student = Student("小红")
# 提示： 调用的时候先从本类去找，如果本类没有找父类，如果找不到则崩溃
student.study()