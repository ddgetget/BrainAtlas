class Person1(object):
    # 私有的类属性
    __country = "美国"

    # 定义修改类属性的对象方法
    def set_country(self, country):
        # Person.__country = country
        # 获取对象的对应的类
        print(self.__class__)
        self.__class__.__country = country

    def get_country(self):
        # return Person.__country
        return self.__class__.__country

xiao_hua = Person1()

xiao_hua.set_country("日本")
value = xiao_hua.get_country()
print(value)


# 对象方法比较 通用，可以修改类属性和对象属性