# 函数的四种类型
# 1. 无参数无返回值
# 2. 无参数有返回值
# 3. 有参数无返回值
# 4. 有参数有返回值


# 1. 无参数无返回值
def show_info():
    print("哈哈，今天的天气好凉爽！")

# 调用函数
show_info()


# 2. 无参数有返回值
def return_info():
    return "哈哈，今天的天气好凉爽！"

# 调用有返回值的函数
msg = return_info()
print(msg)

# 3. 有参数有返回值
def show_msg(info):
    print(info)

# 调用有参数的函数
show_msg("大家好，我是大家的授课老师！")

# 4. 有参数有返回值
def sum_num(num1, num2):
    result = num1 + num2
    # 把result变量返回给外界使用
    return result

# 调用有参数有返回值的函数
value = sum_num(1, 2)
print(value)
