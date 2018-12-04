# 全局变量: 在函数外定义的变量叫做全局变量，全局变量可以在不同函数内使用，局部变量指定在某个函数内使用

# 定义全局变量
g_score = 100


# 显示分数信息
def show_msg():
    # 注意点： 局部变量的名字和全局变量的名字一样，那么这里的操作表示定义的是一个局部变量
    # 修改全局变量需要加上一个关键字：global
    # global表示声明需要对全局变量进行修改
    global g_score
    g_score = 90
    print("show_msg:", g_score)

# 显示学生信息
def show_student_info():
    print("我叫王晓峰 python的分数:%d" % g_score)


# 总结: 全局变量可以在不同函数内使用，并且可以完成数据的共享
show_msg()
show_student_info()

