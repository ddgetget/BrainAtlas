# 2 len(item)	计算容器中元素个数
# 3	max(item)	返回容器中元素最大值
# 4	min(item)	返回容器中元素最小值
# 5	del(item)	删除变量


# cmp(1, 2)

# len: 可以统计字符串，列表，字典，元组
result = len("abc")
print(result)

result = len(["abc"])
print(result)

result = len({"name": "abc", "age": 19})
print(result)

result = len(("abc"))
print(result)

# max： 获取容器中最大值
result = max("123")

print(result)

result = max((1, 2, 4))

print(result)

result = min((1, 2, 4))
print(result)

result = max("hello")
print(result)

result = min("hello")
print(result)

# name = "关羽"
# # del函数函数对应的变量名，后续不能再使用
# del(name)
# print(name)

result = len(("abc",))
print(result)
