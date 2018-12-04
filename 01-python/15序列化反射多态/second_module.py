def show():
    print("我是第二个模块函数")

class Student(object):
    def __init__(self):
        self.name = "李四"
        self.age = 20



# 在当前模块加载Student类
# __name__： 当前模块名，直接该模块是__main__
print(__name__, type(__name__))
module_obj = __import__(__name__)

class_name = getattr(module_obj, "Student")

print(class_name().name)
