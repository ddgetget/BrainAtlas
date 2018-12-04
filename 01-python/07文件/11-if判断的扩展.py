# if 判断 bool类型， 数字类型， 容器类型(字符串，二进制数据，列表，元组，字典，集合)，not None

is_ok = True
if is_ok:
    print("条件成立")


# 数字是非0即真
num = -1
if num:
    print(num)
    print("条件成立")
else:
    print(num)
    print("条件不成立")

# 容器类型通常判断都是通过len获取内容个数进行判断
# 还可以直接判断，如果容器类型有数据条件成立，否则不成立

my_list = [1, 5]
if my_list:
    print(my_list)
    print("成立")
else:
    print(my_list)
    print("不成立")


if not None:
    print("条件成立")

else:
    print("不成立")