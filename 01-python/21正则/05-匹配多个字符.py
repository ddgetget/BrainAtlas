# *	匹配前一个字符出现0次或者无限次，即可有可无
# +	匹配前一个字符出现1次或者无限次，即至少有1次
# ?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
# {m}	匹配前一个字符出现m次
# {m,n}	匹配前一个字符出现从m到n次

import re


# 1. pattern: 正则表达式
# 2. string: 要匹配的字符串
# *	匹配前一个字符出现0次或者无限次，即可有可无
match_obj = re.match("t.*o", "twfo")
if match_obj:
    # 获取匹配结果
    print(match_obj.group())
else:
    print("匹配失败")

# +	匹配前一个字符出现1次或者无限次，即至少有1次
match_obj = re.match("t.+o", "twfo")
if match_obj:
    # 获取匹配结果
    print(match_obj.group())
else:
    print("匹配失败")

# +	匹配前一个字符出现1次或者无限次，即至少有1次
match_obj = re.match("https?", "http")
if match_obj:
    # 获取匹配结果
    print(match_obj.group())
else:
    print("匹配失败")

# {m}	匹配前一个字符出现m次
match_obj = re.match("ht{2}p", "htttp")
if match_obj:
    # 获取匹配结果
    print(match_obj.group())
else:
    print("匹配失败")

# {m,n}	匹配前一个字符出现从m到n次

match_obj = re.match("tc{1,3}p", "tcccp")
if match_obj:
    # 获取匹配结果
    print(match_obj.group())
else:
    print("匹配失败")

# {m,}	匹配前一个字符至少出现m次
match_obj = re.match("tc{1,}p", "tccccp")
if match_obj:
    # 获取匹配结果
    print(match_obj.group())
else:
    print("匹配失败")