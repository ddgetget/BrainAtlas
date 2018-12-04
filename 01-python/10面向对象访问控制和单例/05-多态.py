# 多态： 同一个方法的不同表现形式，不关心对象的类型，只关心对象的方法，不同对象调用同一个方法表现形式不一样


# 天鹅类
class Swan(object):
    def fly(self):
        print("天鹅翱翔的飞")


# 鸭子类
class Duck(object):
    def fly(self):
        print("鸭子沿着地面飞")

# 飞机类
class Plane(object):
    def fly(self):
        print("飞机呼呼的飞")


# 功能操作实现飞的功能
def fly(obj):
    # 这里使用了多态，关心对象的飞的功能，不关心对象的类型
    obj.fly()

duck = Duck()
plane = Plane()
swan = Swan()
fly(swan)

# 多态的好处： 代码更加通用，只关心对象的功能方法，不关心类型，具体的实现操作在指定类中实现