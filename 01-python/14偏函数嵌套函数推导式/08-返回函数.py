def show():
    print()
    def show_line():
        print("---------------------")

    # 内部函数不要在这里执行,返回内部函数
    return show_line

# 获取返回的内部函数
# inner_func = show()
# print(inner_func,type(inner_func))
# inner_func()

show()()
