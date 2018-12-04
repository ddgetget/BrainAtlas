# 定义狗类
class Dog(object):
    # 方法
    # self参数不需要传参数，系统自动把当前对象(那个对象调用的)传入过去
    def eat(self):
        print(self)
        print("吃食物")


# 通过狗类创建对象
xiao_bei = Dog()
print(xiao_bei)
# 面向对象的开发方式
xiao_bei.eat()

# xiao_hua = Dog()
# print(xiao_hua)
# # 通过对象调用对应的功能方法
# xiao_hua.eat()


# 总结： 类可以创建多个对象，多个对象属于同一个类型