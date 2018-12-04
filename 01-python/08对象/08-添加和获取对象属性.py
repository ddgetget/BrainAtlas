class Dog(object):
    def eat(self):
        print("狗吃骨头")


hb = Dog()
# 添加对象属性
hb.name = "小黑"
hb.age = 1

# 获取对象的属性
print(hb.name)

hb.eat()



