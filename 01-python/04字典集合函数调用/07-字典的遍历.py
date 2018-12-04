my_dict = {"name": "刘备", "age": 64, "sex": "男"}

# 使用for循环遍历的字典， 默认遍历字典是遍历key
for key_name in my_dict:
    print(key_name)

# 遍历字典中value值
for value in my_dict.values():
    print(value)

# 指名遍历字典中所有的key
for key in my_dict.keys():
    # 根据key获取对应的value值
    value = my_dict[key]
    print(key, value)

my_list = list(my_dict.items())
print(my_list)
# 遍历字典里面的key和value
for my_name in my_list:
    print(my_name)

# 通过items方法遍历字典中的key和value值
for key, value in my_dict.items():
    print(key, value)


