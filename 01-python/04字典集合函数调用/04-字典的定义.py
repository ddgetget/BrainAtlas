# 字典: 以大括号表现实现的数据集合就是字典，提示：大括号里面存放的是key-value 数据的集合

student_dict = {"name": "李白", "age": 18, "sex": "男"}

# 列表对应的数据类型: list
# 元组对应的数据类型: tuple
# 字典对应的数据类型： dict
print(student_dict, type(student_dict))


# 根据key取值的方式1
# 字典是通过key获取对应的value值
# name = student_dict["name"]
# print(name)
#
# # 使用中括号方式根据key获取对应的value，如果key在字典里面不存在那么会崩溃
# address = student_dict["address"]
# print(address)

print("--------------------------")
# 根据key取值的方式2

name = student_dict.get("name")
print(name)

# 使用get方式取值，如果key在字典里面不存在，那么获取的值是None(空值，没有值的意思)， 代码不会崩溃
address = student_dict.get("address")
print(address)

# 如果key对应的值不存在，可以提供默认值
address = student_dict.get("address", "北京")
print(address)