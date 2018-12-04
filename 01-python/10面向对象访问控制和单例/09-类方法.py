class Person(object):

    # 定义类的私有属性
    __country = "中国"

    @classmethod  # 类方法的标识
    def show_country(cls):
        # cls： 表示当前类
        print(cls)

    # 类方法的应用场景，可以给私有类属性设置值和获取值

    @classmethod
    def set_country(cls, country):
        # cls -> Person, 好处是类名修改不会对这里产生影响
        cls.__country = country

    @classmethod
    def get_counry(cls):
        return cls.__country


# 通过类调用类方法
Person.show_country()
# print(Person.__country)

# 非常规手段
# print(Person.__dict__)
# # 私有属性伪装后的属性名： _Person__country
# Person._Person__country = "美国"
# print(Person.__dict__)

# 常规手段类方法的使用的操作
Person.set_country("美国")
country = Person.get_counry()
print(country, type(country))


# 对象访问类方法
person = Person()
# 扩展： 使用对象获取对应所对应的类
print("获取对象所对应的类:", person.__class__)


person.show_country()

# 提示： 对象可以调用类方法，前提需要创建对象


