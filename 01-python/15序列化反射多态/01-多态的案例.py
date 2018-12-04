# 基类
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def dance(self):
        print("跳舞")

    # 开始跳舞的功能方法
    def play_dance(self):
        # 关注的是跳舞方法，不关心对象的类型
        self.dance()


# 老年人类
class OldMan(Person):
    def __init__(self, tx, name, age):
        super(OldMan, self).__init__(name, age)
        self.tx = tx

    # 跳舞的功能
    def dance(self):
        print("跳广场舞")


# 中年人类
class MiddleMan(Person):
    # 跳舞的功能
    def dance(self):
        print("跳交际舞")


# 少年类
class Boy(Person):
    # 跳舞的功能
    def dance(self):
        print("跳街舞, 很有动感")

if __name__ == '__main__':
    old_man = OldMan(True, "张三", 60)
    # old_man.dance()
    old_man.play_dance()
    middle_man = MiddleMan("李四", 40)
    # middle_man.dance()
    middle_man.play_dance()

    boy = Boy("王五", 20)
    # boy.dance()
    boy.play_dance()