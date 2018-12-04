
# 定义全局变量
g_version = 1.0


# 定义老师类
class Teacher(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return "我的名叫做:%s 年龄:%d 性别:%s" % (self.name, self.age, self.sex)


def show_msg():
    print("我是第二个模块里面的功能函数")


def calc_num(num1, num2):
    result = num1 + num2
    return result

print(__name__)

# 判断模块是否是主模块，直接执行的模块就主模块， 或者程序入口模块
# if __name__ == "__main__":

if __name__ == '__main__':

    # 测试计算数字的函数
    result = calc_num(1, 4)
    print(result)