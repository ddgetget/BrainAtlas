# 调用函数传参使用的是引用传递或者是内存地址传递
def show(params):
    print(params, id(params))

    # int类型是不可变类型，不能再原有数据的基础上修改
    # params += params
    # 总结：对于赋值操作来说，不管是可变类型和不可变类型赋值操作变量保存的内存地址都会发生变化
    params = params + params
    print(params, id(params))


# 定义int类型的变量
# int类型是不可变类型
# num = 10
# print(num, id(num))

# 列表是可变类型，可以在原有数据的基础上进行修改，并且内存地址不变
my_list = [1, 2]
print(my_list, id(my_list))

show(my_list)

# 总结： 在python里面所有的赋值操作都是引用传递

