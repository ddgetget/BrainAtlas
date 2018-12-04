import sys

# my_dict = {"a": 1, "b": 2}
#
# for key, value in my_dict.items():
#     print(key, value)

# 本质通过for循环把数据组装成一个key:value这样的键值对就可以了
# new_dict = {value: key for key, value in my_dict.items()}

# print(new_dict)


# my_dict = {"a": 1, "b": 2, "A": 10, "z": 20}

# a = my_dict.get("Z", 0)
#
# print(a)
# new_dict = {
#     key.lower(): my_dict.get(key.lower(), 0) + my_dict.get(key.upper(), 0)
#     for key in my_dict.keys()
# }
# print(new_dict)

my_list1 = ["name", "age"]
my_list2 = ["张三", 18]
# my_list3=[23,90]
print(sys.getsizeof(my_list1))
# print(sys.getsizeof(my_list3))
print(sys.getsizeof(my_list2))



# 使用字典推导式
result = {my_list1[i]: value for i, value in enumerate(my_list2)}
print(result)




# {"name": "张三", "age":18}

# 压缩数据的，把内存占用空间变小
result = zip(my_list1, my_list2)
print(sys.getsizeof(result))
# for value in result:
#     print(value)

result = dict(result)
print(result)

# result = list(result)
#
# print(result)

# result = set(result)
# print(result)

# my_tuple = tuple(result)
# print(my_tuple)