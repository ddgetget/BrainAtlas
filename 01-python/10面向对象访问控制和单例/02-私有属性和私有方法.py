# 私有属性和私有方法定义方式: 在属性名和方法名前面加上'__'定义的属性和方法就是私有属性和私有方法
# 私有属性和私有方法的特点：只能在类内部使用，不能在类外部使用


# 定义人类
class Person(object):
    # 给对象添加属性及对属性进行初始化（赋值）
    def __init__(self, name, age):
        # 默认对象属性是公有的，在类外部可以访问
        self.name = name
        # 私有属性的定义方式，在类外部不能使用，只能在类内部使用
        self.__age = age

    # 默认的提供的方法是公有方法
    def show(self):
        print("哈哈，今天天气好凉爽！！")
        # 在类内部访问私有属性
        print(self.__age)
        # 在类内部访问私有方法
        self.__show_msg()

    # 私有方法
    def __show_msg(self):
        print("我叫: %s 年龄: %d" % (self.name, self.__age))


# 创建对象
person = Person("zs", 20)


# print(person.name, person.age)
person.show()
# 私有属性和私有方法不能再外界使用，只能在类内部使用
# print(person.__age)
# person.__show_msg()

# 提示： 私有属性和私有方法使用对象在外界直接访问


