# _*_ coding:utf-8 _*_

# 定义类的格式
# class 类名:
#     # 属性
#     # 方法（def）

# 定义狗类
# 旧式类的定义方式， 在python3里面旧式类默认继承object， 在python2里面就没有父类
class Dog:
    # 属性（特征）
    # 方法（行为）
    def eat(self):
        print("狗吃食物")


# 定义猫类
# 新式类的定义方式
class Cat(object):
    def eat(self):
        print("猫吃老鼠")

# 查看子类继承的父类
obj = Dog.__bases__
print(obj)
obj = Cat.__bases__
print(obj)

