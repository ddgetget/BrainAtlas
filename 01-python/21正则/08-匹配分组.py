# |	匹配左右任意一个表达式
# (ab)	将括号中字符作为一个分组
# \num	引用分组num匹配到的字符串
# (?P<name>)	分组起别名
# (?P=name)	引用别名为name分组匹配到的字符串
import re


# 水果列表
fruit_list = ["apple", "pear", "peach", "banana"]

for fruit in fruit_list:
    match_obj = re.match("apple|peach", fruit)
    if match_obj:
        print("%s是我想要吃的" % match_obj.group())
    else:
        print("%s不是我想要吃的" % fruit)

# 匹配出163、126、qq等邮箱
# (ab)	将括号中字符作为一个分组
match_obj = re.match("([a-zA-Z0-9_]{4,20})@(163|126|qq)\.com", "hello@126.com")
if match_obj:
    print(match_obj.group())
    # 获取第一个分组匹配到的数据
    result = match_obj.group(2)
    print(result)
else:
    print("匹配失败")

# qq:10345, 提示： 以后想要获取指定数据，可以把指定数据放到分组里面，以后可以通过分组获取对应的数据
match_obj = re.match("(qq:)([1-9]\d{4,10})", "qq:10345")
if match_obj:
    print(match_obj.group())
    # 获取第一个分组匹配到的数据
    result = match_obj.group(2)
    print(result)
else:
    print("匹配失败")


# <html>hh</html>, \\表示一个不同的反斜杠，不具备转义字符的功能
match_obj = re.match("<([a-zA-Z1-6]+)>.*</\\1>", "<html>hh</html>")
if match_obj:
    print(match_obj.group())

else:
    print("匹配失败")

# <html><h1>www.itcast.cn</h1></html>
# \num	引用分组num匹配到的字符串
match_obj = re.match("<([a-zA-Z1-6]+)><([a-zA-Z1-6]+)>.*</\\2></\\1>", "<html><h1>www.itcast.cn</h1></html>")
if match_obj:
    print(match_obj.group())

else:
    print("匹配失败")

# (?P<name>)	分组起别名
# (?P=name)	引用别名为name分组匹配到的字符串

match_obj = re.match("<(?P<n1>[a-zA-Z1-6]+)><(?P<n2>[a-zA-Z1-6]+)>.*</(?P=n2)></(?P=n1)>", "<html><h1>www.itcast.cn</h1></html>")
if match_obj:
    print(match_obj.group())

else:
    print("匹配失败")

