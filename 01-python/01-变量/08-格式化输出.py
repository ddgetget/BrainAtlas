age = 10
print("我今年%d岁" % age)
age = 11
print("我今年%d岁" % age)

pi = 3.1415926
# %f默认保留6位小数，并且会四舍五入
print("pi的值:%f" % pi)

# 保留两位小数并且会四舍五入
print("pi的值:%.2f" % pi)

student_name = '貂蝉'
student_age = 18

# 注意点： 如果有多个格式化占位符进行输出，那么传参数的时候多个参数需要加上小括号
# 0-9 a-f
print("美女的名字:%s 美女的年龄:%d" % (student_name, student_age))

num = 16
print("10对应的16进制的数据:%x" % num)




# ctr + / 快速注释和取消注释

# name = "itheima"
# qq = 10876
# print("== == == == == 我的名片 == == == == ==")
# print("姓名: %s" % name)
# print("QQ: %d" % qq)
# print("== == == == == == == == == == == == == =")
#
