class Person(object):
    def run(self):
        print("走路")


class Student(Person):

    # 重写父类的方法
    def run(self):
        # 如果调用父类的方法名和子类里面方法名相同，不需要这样调用，会出现递归死循环
        # self.run()

        # 2. 使用父类的类名
        Person.run(self)

        print("学生走路")


    def student_run(self):
        # 1. 调用父类里面的run方法， 提前是子类里面不能有父类里面的方法
        # self.run()
        # 2. 使用父类的名字调用父类的方法
        Person.run(self)

        print("跳着走")

student = Student()
student.run()
# student.student_run()


# # 调用父类的方法
# student.run()
# # 调用自己的方法
# student.student_run()

