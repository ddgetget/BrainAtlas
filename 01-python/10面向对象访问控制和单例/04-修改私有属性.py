class Student(object):
    def __init__(self):
        # 私有属性, 表示给对象添加了一个私有属性
        # 在python里面没有做到绝对私有，只是把私有属性的名字进行了一个伪装, 伪装的格式：_当前类名__当前的私有属性名
        self.__score = 90

    # 提供公有的方法，设置私有属性
    def set_score(self, score):
        self.__score = score

    # 提供公有的方法，访问私有属性的值
    def get_score(self):
        return self.__score

    def __show(self):
        print("我是一个私有方法")


student = Student()

# 私有属性不能访问
# print(student.__score)


# 查看对象的属性
print(student.__dict__)

# 直接对私有属性进行修改， 在这里不是修改私有属性只是添加了一个普通的__score的属性
# student.__score = 95
# print(student.__score)

student.set_score(95)
value = student.get_score()
print(value)

# 查看对象的属性
print(student.__dict__)


# 扩展-- 非常规手段, 直接修改私有属性
student._Student__score = 100
# 查看对象的属性
print(student.__dict__)



# 查看类里面的属性和方法
print(Student.__dict__)

# 使用伪装后的私有方法
student._Student__show()







