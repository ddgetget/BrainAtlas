import random


# 使用列表存储8位老师
teacher_list = ["郭老师", "宋老师", "雒老师", "张老师", "李老师", "赵老师", "毛老师", "周老师"]

# 办公室列表， 每一个办公室就是一个小列表
office_list = [[], [], []]

# 遍历老师列表
for teacher in teacher_list:
    # print(teacher)
    # 随机产生一个0-2之间的一个随机数, 注意：2是包含
    index = random.randint(0, 2)
    print(index)
    # 根据下标获取对应的办公室
    office = office_list[index]
    # 把老师添加到指定办公室里面
    office.append(teacher)


# print(office_list)

# 显示每一个办公室的老师的个数及老师的信息
office_no = 1
for office in office_list:
    print("办公室%d的人数:%d" % (office_no, len(office)))

    # 遍历办公室的获取每一个老师信息
    for teacher in office:
        print(teacher + " ", end="")
    # 代码执行到此说明这个办公室里的老师循环完成
    print("")

    office_no += 1







