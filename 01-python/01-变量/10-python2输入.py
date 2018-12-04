# _*_ coding:utf-8 _*_
# 方式1 input
# msg = input("请求输入数据:")
# print(msg, type(msg))


# 方式2 raw_input
# 总结： raw_input相当于python3里面input，在python2里面接收数据一般raw_input
# raw_input返回的数据类型都是字符串(str)
msg = raw_input("请输入数据:")
print(msg, type(msg))