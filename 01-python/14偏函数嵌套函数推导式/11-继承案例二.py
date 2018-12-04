class Person(object):
    def __init__(self, name, age, sex, country):
        # 添加对象属性
        self.name = name
        self.age = age
        self.sex = sex
        self.country = country

    # 吃饭
    def eat(self):
        print("人吃饭")

    # 睡觉
    def sleep(self):
        print("人睡觉")

    # 工作
    def work(self):
        print("人工作")


class Student(Person):
    def __init__(self, school_name, student_no):
        print(self.__class__.mro())
        # 调用父类里面的init方法，可以使用父类的属性
        super(Student, self).__init__("张三", 18, "男", "中国")
        self.school_name = school_name
        self.student_no = student_no

    def work(self):
        print("学生的工作就是学习")

class Worker(Person):
    def __init__(self, company, worker_age, name, age, sex, country):
        super(Worker, self).__init__(name, age, sex, country)
        self.company = company
        self.worker_age = worker_age

    def work(self):
        print("码代码")



stu = Student("北京一中", 1)
print(stu.student_no, stu.school_name, stu.name)
stu.work()


worker = Worker("传智", "2", "小张", 27, "男", "中国")
print(worker.company, worker.name)
worker.work()