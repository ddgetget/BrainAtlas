# 函数嵌套： 在函数里面在定义一个函数
def show():
    print("嘻嘻，我是外层函数")
    def inner():
        print("哈哈，我是内部函数")

    # 调用内部函数
    inner()

# show()
# 未来使用闭包的时候需要用函数嵌套

# result = show()
# print(result.inner())

