# len， 统计字符串、列表、元组、字典的个数

my_str = "abc"
result = len(my_str)
print(result)

# 定义字典
my_dict = {"name": "杨钰莹", "age": 18, "sex": "女"}
result = len(my_dict)

print(result)

# 获取字典中所有的key值集合
result = my_dict.keys()
# 把dict_keys转成列表类型
result = list(result)
print(result, type(result))

# 获取字典中所有的value值
result = my_dict.values()
# 把dict_values转成列表
result = list(result)
print(result, type(result))


# 获取字典中的key和value值的键值对集合
my_items = my_dict.items()

# 把dict_items转成list
my_items_list = list(my_items)
print(my_items_list, type(my_items_list))