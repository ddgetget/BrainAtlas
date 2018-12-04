def append_data(data, my_list=[]):

    my_list.append(data)
    print(my_list)


append_data(1)
append_data(2)
append_data(3, [])
append_data(4)

# 提示：缺省参数在函数定义的时候参数已经有值，如果不传入参数，那么所有的数据都会给默认的值
# 把数据添加到列表里面
