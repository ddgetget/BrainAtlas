# 学生的信息可以使用字典存储
# 管理学生可以使用列表
import os

# 定义全局变量学生列表
student_list = [] # list()
print("全局变量：", id(student_list))

# 添加学生的功能函数
def add_student():
    # 定义一个空的字典
    student_dict = {}  # dict()
    # 接收用户输入的信息
    name = input("请输入您的姓名:")
    age = input("请输入您的年龄:")
    sex = input("请输入您的性别:")
    # 把学生信息添加到字典里面
    student_dict["name"] = name
    student_dict["age"] = age
    student_dict["sex"] = sex

    # global: 表示要修改全局变量的内存地址
    # 对于可变类型来说，如果没有进行赋值操作那么global关键字可以不用加，但是对于不可变类型来说需要加上global
    # 如果全局变量的内存地址需要改变必须加上global，否则不需要

    # global student_list
    # student_list = [{"name": "王五", "age": "19", "sex": "男"}]
    # print("全局变量：", id(student_list))
    # 把添加的每一个学生字典信息存放到一个指定列表里面
    student_list.append(student_dict)


# 修改学生信息
def modify_student():
    # 1. 先根据学号找到学生
    student_no = int(input("请输入您要修改学生的学号:"))
    # 根据学号获取对应的下标
    index = student_no - 1

    if index >= 0 and index < len(student_list):
        # 根据下标获取学生字典信息
        student_dict = student_list[index]

        # 2. 根据学生的字典信息进行数据的修改
        name = input("请输入您修改后的姓名:")
        age = input("请输入您修改后的年龄:")
        sex = input("请输入您修改后的性别:")

        # 修改字典信息
        student_dict["name"] = name
        student_dict["age"] = age
        student_dict["sex"] = sex
    else:
        print("学号有问题，请重新输入！")


# 删除学生信息
def remove_student():
    # 接收用户输入的学号
    student_no = int(input("请输入您要删除的学生的学号:"))
    # 根据学号获取下标
    index = student_no - 1

    # 判断下标的范围
    if index >= 0 and index < len(student_list):
        # 下标合法
        del student_list[index]
    else:
        print("学号有问题，请重新输入！")


# 显示所有学生信息
def show_all_student():
    for index, student_dict in enumerate(student_list):
        print("学号: %d 姓名: %s 年龄:%s 性别:%s" % (index + 1, student_dict["name"], student_dict["age"],
                                             student_dict["sex"]))


# 查询学生函数
def search_student():
    # 接收用户信息
    name = input("请输入您要查询的学生姓名:")

    # 遍历列表获取每一个学生信息
    for index, student_dict in enumerate(student_list):
        if student_dict["name"] == name:
            # 条件成立表示找到了
            print("学号: %d 姓名: %s 年龄:%s 性别:%s" % (index + 1, student_dict["name"], student_dict["age"],
                                                 student_dict["sex"]))
            # 找到就跳出当前循环
            break

    else:
        # shift+tab: 往左边缩进， tab： 往右边缩进
        print("没有找到这个学生信息")


# 保存数据到文件的函数
def save_data():
    file = open("student_list.data", "w", encoding="utf-8")
    # 把列表转成字符串
    student_list_str = str(student_list)
    file.write(student_list_str)
    file.close()


# 加载文件中的数据
def load_data():

    # result = os.path.exists("DDD/1.txt")
    # print(result)
    # 判断文件或者文件夹是否存在
    if os.path.exists("student_list.data"):
        # 代码执行到此说明文件存在

        file = open("student_list.data", "r", encoding="utf-8")
        # 读取文件中的数据
        file_content = file.read()


        # global student_list
        # # 获取字符串中原始数据
        # student_list = eval(file_content)

        # 修改全局变量的内容数据
        student_list.extend(eval(file_content))

        print(file_content, type(file_content))
        file.close()


# 显示功能菜单函数
def show_menu():
    print("-----学生管理系统 V1.0-----")
    print("1. 添加学生")
    print("2. 修改学生")
    print("3. 删除学生")
    print("4. 查询学生")
    print("5. 显示所有学生信息")
    print("6. 退出")


# 程序入口函数
def main():

    # 加载文件中的数据
    load_data()
    while True:
        show_menu()

        # 获取用户输入的功能选项
        menu_option = input("请输入功能选项:")

        if menu_option == "1":
            # 添加学生
            # pass # 空实现
            add_student()
        elif menu_option == "2":
            # 修改学生信息
            # pass
            modify_student()
        elif menu_option == "3":
            # 删除学生信息
            # pass
            remove_student()
        elif menu_option == "4":
            # 查询学生信息
            # pass
            search_student()
        elif menu_option == "5":
            # 显示所有学生信息
            # pass
            show_all_student()
        elif menu_option == "6":
            # 退出
            # pass
            # 退出之前保存数据到文件中
            save_data()
            print("退出")
            break
        else:
            # 选项输入有误
            # pass
            print("选项输入有误")

# 执行程序入口函数
main()