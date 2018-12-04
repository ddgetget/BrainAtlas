import random

# 接收用户出拳信息
user = int(input("请出拳 剪刀(0) 石头(1) 布(2):"))
print(user)


# 随机产生0-2之间的一个随机数
# 电脑随机出拳信息
computer = random.randint(0, 2)

print(computer, type(computer))


# 出现的结果，你赢了 ， 你和电脑平局， 你输了电脑赢了

if (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
    print("你赢了")
elif user == computer:
    print("平局")
else:
    print("你输了，电脑赢了")



