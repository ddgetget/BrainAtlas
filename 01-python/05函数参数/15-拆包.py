# 拆包：把容器类型中的每一个数据使用不同变量保存
my_str = 'abc'
# 对字符串进行拆包
a, b, c = my_str
print(a, b, c)

# 对列表进行拆包
my_list = [1, 2, 4]
num1, num2, num3 = my_list
print(num1, num2, num3)

# 对元组进行拆包
my_tuple = (1, 2, 4)
num1, num2, num3 = my_tuple
print(num1, num2, num3)

# 对字典进行拆包
my_dict = {"name": "张三", "age": 18}

key1, key2 = my_dict
print(key1, key2)

my_dict = {"name": "张三", "age": 18}.values()

value1, value2 = my_dict
print(value1, value2)

result = {"name": "张三", "age": 18}.items()
print(result)

item1, item2 = result

print(item1[0],item1[1], item2[0], item2[1])

# 对字典中每项数据进行拆包
for key, value in (item1, item2):
    # print(item)
    print(key,value)


# 拆包
for key, value in {"name": "张三", "age": 18}.items():
    print(key, value)



