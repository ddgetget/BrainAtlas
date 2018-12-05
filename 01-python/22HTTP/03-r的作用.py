import re

my_str = "c:\\a\\b\\c"
print(my_str)


# match_obj = re.match("c:\\\\a\\\\b\\\\c", my_str)

match_obj = re.match(r"c:\\a\\b\\c", my_str)

if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

# r: 表示的是使用原始字符串，只对反斜杠起作用，反斜杠不需要再转义了，r里面的反斜杠是一个真正的反斜杠
# 建议： 以后再使用正则表达式的时候可以在前面加上r，这样正则表达式的兼容性更强
# \1
match_obj = re.match(r"<([a-zA-Z1-6]+)>.*</\1>", "<html>hh</html>")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

match_obj = re.match(r"\.", ".")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")