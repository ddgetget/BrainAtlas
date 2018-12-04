def return_values():
    print("return_values开始执行了")
    return 1
    print("-----------")
    return 2

# 总结： 函数里面执行了return语句，那么表示函数执行结束，return后面有再多的代码也不会执行
# 提示： return只会返回一次值
result = return_values()
print(result)

# return可以返回一个容器类型(字符串， 列表， 元组， 字典)，完成返回多个值的操作
def return_more_values():
    # 提示： 返回元组可以省略小括号
    return 1, 2

result = return_more_values()
print(result, type(result))


# 提示一下： 如果想要某个函数符合某个条件函数执行结束，那么需要使用return语句


def show_info():
    i = 0
    while True:
        print(i)
        if i == 2:
            return
        i += 1

show_info()

# --扩展
def show_msg():
    print("哈哈哈")
    return

# 提示一下： 只有一个单独return表示函数执行完没有返回值，如果获取返回值结果的是空值(None)
result = show_msg()
print(result)



