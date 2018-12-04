class Person(object):
    def show(self):
        print("哈哈，我是一个好人")


class Student(Person):

    def student_show(self):
        # 调用父类的方式1
        # 需要使用父类里面的方法
        # self.show()  # 如果子类有这个方法这样调用不可以
        # 调用父类的方式2
        # 存在的问题是如果父类修改了名字那么这里面的代码需要进行修改
        # Person.show(self)
        # 调用父类的方式3
        # 父类对象调用父类的方法
        super().show()
        print("我是一个好学生")


student = Student()
student.student_show()