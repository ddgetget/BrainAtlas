# 多继承： 子类可以继承多个父类

# 动物类
class Animal(object):
    def __init__(self, age, speed):
        self.speed = speed
        self.age = age

    def eat(self):
        print("动物可以吃食物")


# 鱼类
class Fish(object):

    def swim(self):
        print("鱼可以游")

# 鲨鱼 , 多继承的一个表现
class Shark(Animal, Fish):
    pass

# 创建对象(调用父类的init方法)
shark = Shark(1, 20)
# 访问父类的属性
print(shark.age, shark.speed)
shark.eat()
shark.swim()


print(shark.speed)

