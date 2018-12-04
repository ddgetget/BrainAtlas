class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

class Student(Person):
    # 注意点： 如果子类提供了init方法那么不会自动调用父类的init方法
    def __init__(self, name, age, subject):
        # 自己主动调用父类init方法
        # 1. 父类的名字调用
        # Person.__init__(self, name, age)
        # 2. 使用super调用父类的init方法
        # 调用父类的init方法
        super().__init__(name, age)
        self.subject = subject

    # 由于父类满足不了子类的需求，那么进行重写
    def show(self):
        print(self.name, self.age ,self.subject)

# 子类提供了init方法
student = Student("张三", 19, "python")

student.show()


student = Student("王三", 20, "人工智能")

student.show()





# 子类不提供init方法
# student = Student("张三", 18)
# print(student.name, student.age)
# student.show()