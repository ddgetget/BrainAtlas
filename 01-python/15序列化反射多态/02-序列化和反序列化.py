# 序列化： 把程序中的数据写入到文件中，做到永久存储
# 反序列化: 把文件中的数据加载成一个python对象
import pickle

my_list = ["哈哈", 2, "嘻嘻"]

# 只把数据进行序列化不会自动把数据写入到文件找那个
# 1. 序列化的方式1
# result = pickle.dumps(my_list)
#
# print(result)
#
# # 打开文件写入序列化后的数据
# file = open("my_list.serialize", "wb")
# file.write(result)
# file.close()


# 打开文件
# file = open("my_list.serialize", "rb")
# # 反序列化
# my_list = pickle.load(file)
# print(my_list, type(my_list))
#
# # 关闭文件
# file.close()


# ----------------序列化方式2 直接把数据序列化（写入）到文件中---------------------------
class Person(object):
    def show_info(self):
        print("我是父类的方法")

class Student(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)


# 创建学生对象
# student = Student("李四", 20)
#
# file = open("student.serialize", "wb")
# # 把对象直接序列化到文件中
# pickle.dump(student, file)
# file.close()
#
# file = open("student.serialize", "rb")
# # 反序列化, 读取文件中的二进制数据，把二进制数据反序列化成一个python对象
# stu = pickle.load(file)
# print(stu, type(stu))
#
# # 使用对象中的方法
# stu.show()
# stu.show_info()
#
# # print(stu.__class__.mro())
#
# file.close()

# student = Student("李四", 20)
#
# data = pickle.dumps(student)
# print(data)
#
# stu = pickle.loads(data)
# stu.show()