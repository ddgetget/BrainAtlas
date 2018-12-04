# 1.函数之间共享数据使用全局变量
g_num = 0


def modify_num():
    # 声明修改全局变量
    global g_num
    g_num = 10
    print("modify_num:", g_num)


def show_num():
    print(g_num)


modify_num()
show_num()


# 2. 通过返回值，完成函数之间数据的共享
def return_value():
    return 1

def show_info():
    # 目的是需要使用return_value函数返回的结果
    value = return_value()

    # 使用返回的结果，完成数据的共享
    print(value)

show_info()









