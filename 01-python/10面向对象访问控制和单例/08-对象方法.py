class Person(object):
    def __init__(self, name, age):
        self.name = name
        # 私有属性， 提示： 私有属性只能在init方法里面定义
        self.__age = age

    # 定义对象方法
    def show(self):
        print(self.name, self.__age)

    # 对象方法的应用场景，可以对私有属性设置值和获取值
    def set_age(self, age):
        if age >= 0 and age <= 150:
            self.__age = age
        else:
            print("请输入合法的年龄范围")

    def get_age(self):
        return self.__age


# 创建对象
person = Person("王五", 20)
# person对象调用person对象的show方法
# person.show()


# 使用类调用对象方法, 不推荐这样去写， 意义不大
# Person.show(person)

# 设置年龄
person.set_age(60)
age = person.get_age()
print(age)

# 总结： 对象方法由对象来访问和操作，不需要使用类，因为类访问比较麻烦和啰嗦