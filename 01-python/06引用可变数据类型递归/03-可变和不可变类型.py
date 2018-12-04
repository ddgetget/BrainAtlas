# 可变数据类型: 在原有数据的基础上对数据进行修改(添加，删除，修改)，那么内存地址不变. 比如: 列表、字典、集合(set)
# 不可变类型: 不能在原有数据的基础上对数据进行修改。 比如: 元组、字符串、数字

my_list = ['张三', '李四']
print(my_list, id(my_list))

my_list.append('王五')
my_list[0] = '赵六'
del my_list[1]

print(my_list, id(my_list))

my_dict = {'name': '小花', 'age': 18}

print(my_dict, id(my_dict))

my_dict['age'] = 20
del my_dict['name']
print(my_dict, id(my_dict))

my_tuple = (1, 2)
print(my_tuple, id(my_tuple))
# my_tuple[0] = 0
# 这里不是在原有数据的基础上进行修改，这里是给变量重新赋值了一个新的内存地址
my_tuple = (3, 5)

print(my_tuple, id(my_tuple))

my_str = 'abc'
print(my_str, id(my_str))
# my_str[1] = 'd'

my_str = 'adc'
print(my_str, id(my_str))


my_num = 5
print(my_num, id(my_num))
# my_num[0] = 1

my_num = 1
print(my_num, id(my_num))



