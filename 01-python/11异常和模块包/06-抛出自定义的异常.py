# 接收用户输入的数据，如果长度小于6位那么抛出异常
class CustomException(Exception):
    def __init__(self, current_len, min_len):
        self.current_len = current_len
        self.min_len = min_len

    def __str__(self):
        # 当前抛出异常的并在控制台输出异常对象的时候会自动调用__str__
        return "当前数据的长度是:%d 要求最小的长度是:%d" % (self.current_len, self.min_len)




# 接收用户的数据
msg = input("请输入您的数据:")
if len(msg) < 6:
    # 抛出异常, 提示： raise必须抛出的是异常类型
    raise CustomException(len(msg), 6)

    # 抛出停止迭代的异常， 提示： 如果只抛出StopIteration， 相当于StopIteration()
    # raise StopIteration("我要停止迭代了")
    # raise StopIteration()  => StopIteration
    # raise StopIteration
    # 这里是自己抛出的异常，可以指定异常信息
    # raise NameError("name 'name' is not defined")