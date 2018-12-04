

# my_dict = {"name": "张三"}
#
# # 添加键值对，添加一个age=18的键值对
# my_dict["age"] = 18
# print(my_dict)
#
# # 修改键值对， 修改键值对，需要保证键值对要存在，否则是添加键值对
# my_dict["name"] = "李四"
# print(my_dict)
#
# # 添加和修改键值对的小结： 如果字典里面key存在，那么使用my_dict[key]表示修改键值对，如果字典里面key不存在
# # 那么使用my_dict[key]表示添加键值对
#
# # 添加键值对， 字典是无序的
# my_dict["sex"] = "男"
# print(my_dict)
#
# # 定义列表, 列表是有序的， 提示： 有序就是定义的数据顺序和输出数据的顺序保持一致
# my_list = ["苹果", "鸭梨"]
# my_list.append("橘子")
# print(my_list)
#
#
# # 删除字典里面的键值对
# del my_dict["age"]
# print(my_dict)
#
# # 随机删除一个键值对
# result = my_dict.popitem()
# print(result, my_dict)

# 根据key删除对应的键值对，并且获取对应的key的value值
my_dict = {"name": "张三", "age": 18, "address": "北京"}

result = my_dict.pop("age")
print(result, my_dict)

# 查询key是否在字典里面
result = "name" in my_dict
print(result)

result = "age" in my_dict
print(result)

result = "age" not in my_dict
print(result)

# 清空字典里面所有数据
my_dict.clear()
print(my_dict)

my_list = [1, 2, 3, 4]

# 清空列表中的所有数据
my_list.clear()

print(my_list)