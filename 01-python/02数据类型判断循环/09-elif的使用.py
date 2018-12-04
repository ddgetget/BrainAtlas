# elif 可以判断多个条件，提示：如果某个条件成立，那么后面的条件就不会再判断了，条件判断语句就结束了

score = int(input("请输入您的分数:"))

if score >= 90 and score <= 100:
    print("优秀")
elif score >= 80 and score < 90:
    print("良好")
elif score >= 70 and score < 80:
    print("一般")
elif score >= 60 and score < 70:
    print("及格")
else:
    print("比较差，不及格")