# set:表示一个数据的集合，表示形式是一个{}，但是里面放入不是键值对

# 空set集合不能这样定义，{}表示给字典使用
# my_set = {}
# print(my_set, type(my_set))

my_set = set()
print(id(my_set))

print(my_set, type(my_set))

my_set.add("hello")
print(my_set, type(my_set))
my_set.add(2)
print(my_set, type(my_set))
my_set.add(4.15)
print(my_set, type(my_set))
# 提示： 字典和集合都是无序的
# 注意点: 集合里面不能有重复数据
my_set.add(True)
print(id(my_set))
print(my_set, type(my_set))

my_set.add(2)
print(my_set, type(my_set))
# 总结： 集合是可以添加任意类型数据

# 删除数据, 注意点：如果值不存在那么会崩溃
# my_set.remove(5)

# 删除指定数据，如果数据不存在不会崩溃
my_set.discard(2)
print(id(my_set))
print(my_set)

# 获取数据, 注意点:不能根据下标获取数据
# result = my_set[0]
#
# print(result)


# # 修改数据
# my_set[1] = 4
# print(my_set)

# 可以使用for循环的方式获取set集合中的每一个值
for value in my_set:
    print(value)

print(id(my_set))

# 集合是可变类型

# 使用集合可以把我们去除重复数据

my_set = set()

my_list = [1, 2, 3, 1, 2, 3]

for value in my_list:
    my_set.add(value)

print(my_set)




# # 创建空的字典
# my_dict = dict()
# print(my_dict, type(my_dict))
#
# my_list = list()
# print(my_list, type(my_list))
#
# my_tuple = tuple()
# print(my_tuple, type(my_tuple))
#
# my_str = str()
# print(my_str, type(my_str))