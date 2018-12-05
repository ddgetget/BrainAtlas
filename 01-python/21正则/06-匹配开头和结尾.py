import re

# 匹配以数字开头
match_obj = re.match("^\d.*", "3sdfkljsadfl;k")
if match_obj:
    print(match_obj.group())

else:
    print("匹配失败")


# 匹配以数字结尾
match_obj = re.match(".*\d$", "sdfkljsadfl;4")
if match_obj:
    print(match_obj.group())

else:
    print("匹配失败")


# 匹配以数字以数字结尾
match_obj = re.match("^\d.*\D$", "5sdfkljsadfl;")
if match_obj:
    print(match_obj.group())

else:
    print("匹配失败")


# 除了指定字符以外都匹配
match_obj = re.match("^\d.*[^0-9]$", "5sdfkljsadfl5")
if match_obj:
    print(match_obj.group())

else:
    print("匹配失败")

# 总结：
# ^: 如果^在中括号外面表示以指定字符串开头, ^a.*
# ^: 如果^在中括号里面表示除了指定字符外都匹配, 比如: [^aeiou]
match_obj = re.match("^\d.*[^\d]$", "5sdfkljsadfl")
if match_obj:
    print(match_obj.group())

else:
    print("匹配失败")

