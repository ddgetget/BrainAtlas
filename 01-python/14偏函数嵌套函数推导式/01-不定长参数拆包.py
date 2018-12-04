# --------------不定长位置参数------------------

# def show(*args):
#     # args: 元组
#     print(args, type(args))
#
# # show(1, 2, 5)
#
# my_tuple = (1, 2, 5)# [1, 2, 5]
# # show(my_tuple)
# # show(my_tuple[0], my_tuple[1], my_tuple[2])
#
# # 对元组进行拆包, 对元组进行拆包，使用位置方式传参
# show(*my_tuple)

# -------------不定长关键字参数----------------
def msg(**kwargs):
    # kwargs: 字典
    print(kwargs, type(kwargs))


# msg(a=1, b=2)
my_dict = {"name": "张三", "age": 29}

# msg(a=my_dict)

# msg(name="张三", age=29)

# 对字典进行拆包，使用关键字方式传参
msg(**my_dict)








