# 字符串: 使用引号（单引号、双引号、三个单引号、三个双引号）包起来的数据就是字符串

# 单引号字符串可以兼容双引号字符串
my_str1 = 'hello'
print(my_str1, type(my_str1))

# 双引号可以兼容单引号字符串
my_str2 = "你好"
print(my_str2, type(my_str2))

# 提示： 三引号可以兼容单引号和双引号
my_str3 = '''
今天天气'好晴"朗"！！
处处好风光
'''
print(my_str3, type(my_str3))

my_str4 = """
今天天气好晴朗！！
处处好风光 
"""
print(my_str4, type(my_str4))