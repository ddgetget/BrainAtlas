# import first_module, second_module  # 不推荐大家这样导入，因为不符合PEP8规范

# -------------------------- import方式导入--------------------------

# import first_module
# import second_module
#
#
# result = first_module.sum_num(1, 2)
# print(result)
#
# second_module.show_msg()

# -------------------------- from方式导入--------------------------
# from first_module import sum_num
# from second_module import Teacher
#
#
# result = sum_num(2, 4)
# print(result)
#
# teacher = Teacher("小郭老师", 18, "男")
# print(teacher)

# -------------------------- import 导入给模块起别名--------------------------
# import first_module as first  # 给模块起别名
# result = first.func_name(1)
# print(result)

# -------------------------- from 导入给功能代码起别名--------------------------
# from first_module import sum_num as calc_num
# from second_module import Teacher as MyTeacher
#
# result = calc_num(1, 2)
# print(result)
#
# my_teacher = MyTeacher("雒老师", 17, "女")
# print(my_teacher)

#  -------------------------- from 导入模块中的所有的功能代码--------------------------
# from first_module import *
#
# print(g_num)
# Student("李四", 20).show()
# result = func_name(2)
# print(result)
#
# result = sum_num(1, 2)
# print(result)


#  -------------------------- from 模块名 import * 导入指定的功能代码--------------------------

from first_module import *

Student("哈哈", 20).show()
result = sum_num(1, 2)
print(result)
# print(g_num)
# func_name(1)