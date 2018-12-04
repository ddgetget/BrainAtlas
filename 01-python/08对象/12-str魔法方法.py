# __str__ ： 当使用print显示对象信息的时候会自动调用str方法，str方法需要返回一个字符串信息

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

    # 返回对象的描述信息
    def __str__(self):
        msg = "我叫:%s 年龄:%d" % (self.name, self.age)
        return msg



# 创建对象
person1 = Person("小乔", 27)

# person1.show()

print(person1)