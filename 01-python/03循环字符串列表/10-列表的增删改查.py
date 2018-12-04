my_list = ["小红"]

# 添加数据, 追加数据,append
my_list.append("小白")

print(my_list)

# 插入数据，根据下标插入指定数据
my_list.insert(0, "小雷")
print(my_list)

my_list = ['小雷', '小红', '小白']

my_list.insert(1, "小兰")
print(my_list)


my_list = ['小雷', '小红', '小白']

name_list = ['小黄', '小绿']

# my_list.append(name_list)
# print(my_list)

# for name in name_list:
#     my_list.append(name)
#
# print(my_list)

# extend： 给列表扩展一组数据，也就是说把某一组数据中的每一个元素(数据)添加指定的列表里面
my_list.extend(name_list)
print(my_list)


# 修改数据， 根据下标修改数据
my_list = ['小雷', '小红', '小白']
# 根据下标修改数据
my_list[1] = "小绿"
print(my_list)
# 根据切片可以修改多个值  -扩展
my_list[1:3] = ["小黄", "小黑"]
print(my_list)

# 删除数据
my_list = ['小雷', '小红', '小白']
# 根据指定元素删除数据
# my_list.remove("小红")
# print(my_list)

# 根据下标删除数据
# del my_list[2]
# print(my_list)

# 扩展-通过切片删除多个元素
# del my_list[0:2]
# print(my_list)

# pop删除数据, 根据下标删除会有下标对应的返回值
my_list = ['小雷', '小红', '小白']
result = my_list.pop(1)
print(result, my_list)

# 查找数据是否在列表里面
my_list = ['小雷', '小红', '小白']
result = "小红" in my_list

print(result)


result = "小白" not in my_list

print(result)
