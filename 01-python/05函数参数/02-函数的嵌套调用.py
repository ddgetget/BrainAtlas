# 函数的嵌套调用: 在函数里面有调用了其它函数


# 定义第一个函数
def first():
    print("---1--")
    print("first")
    print("---1--")


# 定义第二个函数
def second():
    print("---2--")
    print("second")
    # 在函数2里面调用函数1的代码，这里可以称为函数的嵌套调用
    first()
    print("---2--")


# 调用函数执行函数体里面的代码
second()