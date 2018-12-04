# +	[1, 2] + [3, 4]	[1, 2, 3, 4]	合并	字符串、列表、元组
# *	['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	复制	字符串、列表、元组
# in	3 in (1, 2, 3)	True	元素是否存在	字符串、列表、元组、字典
# not in	4 not in (1, 2, 3)	True	元素是否不存在	字符串、列表、元组、字典

my_str1 = "hello"
my_str2 = "world"

result = my_str1 + my_str2
print(result)

my_list1 = [1, 2]
my_list2 = [3, 4]

result = my_list1 + my_list2
print(result)

my_tuple1 = (1, 2)
my_tuple2 = (5,)

result = my_tuple1 + my_tuple2
print(result)

# 复制
my_str = "AB"
result = my_str * 4
print(result)

my_list = [1, 3]

result = my_list * 2
print(result)

my_tuple = (2, 4)

result = my_tuple * 3
print(result)

result = 'f' in 'abcd'
print(result)

result = 'a' in ['a', 'b', 'c']
print(result)

result = 'a' in ('a', 'b', 'c')
print(result)

# 默认找的是key
result = 'name' not in {"name": "李四"}
print(result)

result = '李四' not in {"name": "李四"}.values()
print(result)