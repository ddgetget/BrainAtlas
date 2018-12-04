class Student(object):
    def study(self):
        print("好好学习，将来才能找到媳妇")

    def show_info(self):
        print("show:", self)
        # 显示对象属性信息
        print("我叫%s 年龄是%d 性别:%s 地址:%s" % (self.name, self.age, self.sex, self.address))


# 创建对象
student = Student()
print(student)
# 添加对象属性
student.name = "小白"
student.age = 18
student.sex = "男"
student.address = "北京"

# 调用对象方法
student.show_info()


# 创建对象
student1 = Student()
# 添加对象属性
student1.name = "小兰"
student1.age = 18
student1.sex = "女"
student1.address = "北京"

# 调用对象方法
student1.show_info()


