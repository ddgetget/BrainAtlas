my_list = ["苹果电脑", "苹果手机", "iPad"]

# enumerate : 使用for循环遍历列表数据的时候能够获取数据的下标及对应的数据

result = enumerate(my_list)
print(result, list(result))

for index, value in enumerate(my_list):
    print(index, value)


office_list = [["张老师"], ["李老师"], ["王老师"]]


for office_index, office in enumerate(office_list):
    # 依次遍历每一个办公室
    print("办公室编号：%d %s" % (office_index + 1, office))


# for 字符串， 列表，，元组， 字典
for index, value in enumerate("abc"):
    print(index, value)


for index, value in enumerate(["abc", "bcd"]):
    print(index, value)


for index, value in enumerate(("abc", "bcd")):
    print(index, value)



for index, value in enumerate({"name": "李四", "age": 20, "sex":"男"}.values()):
    if index == 2:
        break
    print(index, value)









