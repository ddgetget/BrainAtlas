# 引用：数据在内存中的地址，简称内存地址

a = 10  # 变量a保存的是数据10在内存中的地址

b = a  # 变量b保存的是a存储的内存地址

# 代码执行到此，说明变量a和变量b保存的内存地址相同

print(a, b)

# 获取变量保存的内存地址
a_address = id(a)
b_address = id(b)

# 获取到的数据不是16进制是10进制的数据
print(a_address, b_address)

# 使用hex函数把数据转成16进制
a_address = hex(a_address)
b_address = hex(b_address)

print(a_address, b_address)


