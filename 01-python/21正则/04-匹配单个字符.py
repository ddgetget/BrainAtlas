
# 代码	功能
# .	匹配任意1个字符（除了\n）
# [ ]	匹配[ ]中列举的字符
# \d	匹配数字，即0-9
# \D	匹配非数字，即不是数字
# \s	匹配空白，即 空格，tab键
# \S	匹配非空白
# \w	匹配非特殊字符，即a-z、A-Z、0-9、_、汉字
# \W	匹配特殊字符，即非字母、非数字、非汉字

import re

# 根据正则表达式从头在指定字符串中匹配数据
# .	匹配任意1个字符（除了\n）
match_obj = re.match("t.o", "two")

if match_obj:
    # 获取正则表达式匹配后的结果数据
    print(match_obj.group())
else:
    print("匹配失败")


# 葫芦娃1 2
# [ ]	匹配[ ]中列举的任意一个字符
match_obj = re.match("葫芦娃[12]", "葫芦娃3")

if match_obj:
    # 获取正则表达式匹配后的结果数据
    print(match_obj.group())
else:
    print("匹配失败")

# 匹配银行卡密码中的一位，银行卡密码都是数字

match_obj = re.match("[0-9]", "9")

if match_obj:
    # 获取正则表达式匹配后的结果数据
    print(match_obj.group())
else:
    print("匹配失败")

# \d  => [0-9]
match_obj = re.match("\d", "8")

if match_obj:
    # 获取正则表达式匹配后的结果数据
    print(match_obj.group())
else:
    print("匹配失败")

# \D	匹配非数字，即不是数字
match_obj = re.match("\D", "a")

if match_obj:
    # 获取正则表达式匹配后的结果数据
    print(match_obj.group())
else:
    print("匹配失败")



# 葫芦娃1 2
# \s表示匹配空白字符， 空格和tab键
match_obj = re.match("葫芦娃\s[12]", "葫芦娃 2")

if match_obj:
    # 获取正则表达式匹配后的结果数据
    print(match_obj.group())
else:
    print("匹配失败")


# 葫芦娃1 2
# \S表示匹配非空白字符， 空格和tab键
match_obj = re.match("葫芦娃\S[12]", "葫芦娃*2")

if match_obj:
    # 获取正则表达式匹配后的结果数据
    print(match_obj.group())
else:
    print("匹配失败")

# 匹配一位密码，密码的组成： 由字母，数字，下划线组成
match_obj = re.match("[a-zA-Z0-9_]", "D")

if match_obj:
    # 获取正则表达式匹配后的结果数据
    print(match_obj.group())
else:
    print("匹配失败")

# \w	匹配非特殊字符，即a-z、A-Z、0-9、_、汉字
match_obj = re.match("\w", "哈")

if match_obj:
    # 获取正则表达式匹配后的结果数据
    print(match_obj.group())
else:
    print("匹配失败")


# \W	匹配特殊字符，即非字母、非数字、非汉字
match_obj = re.match("\W", "a")

if match_obj:
    # 获取正则表达式匹配后的结果数据
    print(match_obj.group())
else:
    print("匹配失败")