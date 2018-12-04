# 不定长参数: 不确定用户给函数传入多少参数， 可能传入0个参数也可能是多个参数

# 不定长参数分为： 不定长位置参数和不定长关键字参数

# *args表示不定长位置参数
def sum_num(*args):
    # 把外界的位置参数封装成一个元组类型，元组里面存放的是外界按照位置方式传入的参数
    print(args, type(args))

    result = 0
    for value in args:
        # print(value)
        result += value

    return result

# 按照不定长位置方式传参
# value = sum_num(1, 2, 5)
#
# print(value)


# 不定长关键字参数
def show_info(**kwargs):
    # kwargs把外界的关键字参数封装到字典里面
    print(kwargs, type(kwargs))
    for key, value in kwargs.items():
        print(key, value)



show_info(a=1, b=2)