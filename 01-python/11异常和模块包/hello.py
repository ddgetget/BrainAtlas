try:
    msg = input("请输入数据:")

    int(msg)
except Exception as e:
    # print(e, type(e))
    print("请输入合法的数字")


