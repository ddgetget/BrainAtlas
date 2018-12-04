# 多层继承: 多个层级的继承关系


class GrandFather(object):
    def open_flower_shop(self):
        print("开花店")


class Father(GrandFather):
    def open_hotel(self):
        print("开酒店")

# 对应Son类来说是多层继承
class Son(Father):
    def open_factory(self):
        print("开厂子")

son = Son()
son.open_factory()
son.open_hotel()
son.open_flower_shop()

