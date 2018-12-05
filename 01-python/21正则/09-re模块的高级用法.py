import re


# 根据正则表达式在指定字符串中查找指定数据, 只查找1次
match_obj = re.search("\d+", "苹果10个 鸭梨5个")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

# 根据正则表达式在指定字符串中查找多个数据， 可以查找多次
result = re.findall("\d+", "苹果10个 鸭梨5个 总共15个")
print(result)

# 替换

# 1. 正则
# 2. 替换后的内容
# 3. 要匹配的字符串
# 4. count=1: 替换的次数，默认是全部替换,默认是0
result = re.sub("\d+", "200", "阅读数:10, 评论数据:1", count=1)
print(result)

# match_obj:表示根据正则表达式匹配的结果对象，这个参数不需要程序员传入，系统自己传入
def replace_str(match_obj):
    # 获取匹配结果
    value = match_obj.group()
    print(type(value))
    value = int(value) + 1
    # 返回的数据类型必须是字符串
    return str(value)

result = re.sub("\d+", replace_str, "阅读数:10")
print(result)

my_fruit = "苹果:鸭梨,香蕉:桃子"

# 1. 正则
# 2. 要匹配的字符串
# 3. maxsplit默认值是0，表示全部分割， maxsplit=1：表示分割1次
result = re.split(":|,", my_fruit, maxsplit=1)

print(result)
