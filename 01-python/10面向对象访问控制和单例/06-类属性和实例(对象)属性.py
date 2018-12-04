# 类属性： 在类里面在方法外定义的属性叫做类属性
# 实例(对象)属性： 在init方法里面定义的属性叫做实例(对象)属性


class Person(object):
    # 类属性
    country = "中国"
    # 使用init方法提供实例(对象)属性
    def __init__(self, name, age):
        # 实例(对象)属性
        self.name = name
        self.age = age


# -----------------对象属性的相关操作--------------------------
# 创建person对象
person = Person("李四", 20)

# person对象访问实例（对象）属性
print(person.name, person.age)
# 使用对象修改对象属性
person.name = "张三"
person.age = 40
print(person.name, person.age)

# 提示： 使用类不能修改对象属性
# print(Person.name)

# print(person.__dict__)

# 这里不是修改对象属性是给类添加了一个类属性
# Person.name = "哈哈"
# print(Person.name)

# print(person.__dict__)
# print(Person.__dict__)

# 提示： 对象属性的操作使用对象来完成，不要使用类进行操作，防止产生错误
# 提示： 类不能访问对象属性， 类不能修改对象属性，本质上添加了一个类属性



# -----------------类属性的相关操作--------------------------
# 查看类里面的属性和方法
print(Person.__dict__)
# 访问类属性
print(Person.country)

# 修改类属性
Person.country = "美国"

print(Person.country)
# 查看类里面的属性和方法
print(Person.__dict__)


# 提示： 对象可以访问类属性
print(person.country)

# 使用对象修改类属性，不可以， 其实是添加了一个对象属性
print(person.__dict__)
person.country = "日本"
print(person.country)
print(person.__dict__)

print(Person.__dict__)

# 总结： 想要保住对属性的操作不会出现问题，对象属性使用对象来操作，类属性使用类来操作
# 只不过有一点： 对象可以访问类属性，类不能访问对象属性
