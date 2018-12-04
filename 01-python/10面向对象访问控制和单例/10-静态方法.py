class Person(object):
    __country = "中国"

    def __init__(self, name, age):
        self.name = name
        self.age = age


    @staticmethod  # 静态方法的标识
    def show(num1, num2):
        # 静态方法不能使用当前self对象
        # 静态方法不能使用当前cls类
        print("哈哈，我是一个静态方法")
        # print(self.name)
        # print(cls.name)
        result = num1 + num2
        return result

        # 提示： 以后这个方法的里面的操作和当前对象和当前类都没有关系可以定义成是一个静态方法

    @staticmethod
    def set_country(country):
        Person.__country = country


    @staticmethod
    def get_country():
        return Person.__country

    # @staticmethod
    # def set_name(person, name):
    #     person.name = name
    #
    # @staticmethod
    # def get_name(person):
    #     return person.name


# ----------使用类调用静态方法---------

# 使用类调用静态方法
result = Person.show(1, 3)
print(result)

Person.set_country("美国")
country = Person.get_country()
print(country)


# 一般不这样用

# person = Person("李四", 20)
# Person.set_name(person, "王五")
#
# print(person.name)
# name = Person.get_name(person)
# print(name)

# ----------使用对象调用静态方法---------
person = Person("李四", 20)
result = person.show(1, 3)
print(result)

person.set_country("美国")
value = person.get_country()
print(value)


# 静态方法可以使用类和对象进行访问