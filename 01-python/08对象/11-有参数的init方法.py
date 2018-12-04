# __init__方法：是一个魔法方法，对象创建的时候会自动调用，作用就是给对象添加属性及给对象的属性进行初始化

# 魔法方法: 以__开始，然后以__结束的方法就是魔法方法， 当前需要完成某种功能的时候自动调用该魔法方法


class Student(object):

    # 提供__init__方法，给对象添加属性
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def show(self):
        print("哈哈， 我一个好学生")
        print(self.name, self.age)


student = Student("李四")
student.show()


student1 = Student("王五")
student1.show()

student2 = Student(name='赵六', age=20)
student2.show()

