# 高阶函数：当定义的函数调用的时候能够接受另外一个函数或者返回一个函数，那么你定义的这个函数就是高阶函数

# def show(func):
#     # 调用外界传入过来的函数
#     func()
#
#
# show(lambda:print("哈哈"))


# 接收一个函数
def show(func):

    def inner():
        print("-----")
        func()

    # 返回一个函数
    return inner

inner = show(lambda : print("哈哈"))

inner()