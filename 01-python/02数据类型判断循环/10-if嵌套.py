# if嵌套：在if语句里面再使用一个if语句

# 默认男生找女朋友

sex = input("请输入您的性别:")

if sex == "女":
    print("性别ok")

    age = int(input("请输入您的年龄:"))
    if age >= 18 and age <= 28:
        print("找到了心目中的女神!!!")
    else:
        print("驾驭不了！！！")

else:
    print("其它性别不考虑")

