# 反射: 根据字符串动态加载一个python对象
#
# # 接收用户输入的模块名
# module_name = input("请输入您要导入的模块名:")
#
# # 根据模块名字符串反射成一个模块对象
# module_obj = __import__(module_name)
# print(module_obj)
#
# # 接收用户输入的功能操作
# menu = input("请输入您要操作的功能名称:")
# print(menu)
#
# # 根据功能名在指定模块对象里面反射出来功能对象
# msg = getattr(module_obj, menu)
#
# print(msg)
# msg()

# ------------第二个模块的操作---------------------

# 接收用户输入的模块名
module_name = input("请输入您要导入的模块名:")

# 根据模块名字符串反射成一个模块对象
module_obj = __import__(module_name)
print(module_obj)

# 接收用户输入的功能操作
menu = input("请输入您要操作的功能名称:")
print(menu)

# 根据功能名在指定模块对象里面反射出来功能对象
class_name = getattr(module_obj, menu)

print(class_name)

# 创建对象
stu = class_name()

print(stu.name, stu.age)

# 判断对象是否有对应的成员
if hasattr(stu, "sex"):
    # 获取stu对象中是否有name属性
    sex = getattr(stu, "sex")
    print(sex)
else:
    # 给对象设置sex属性
    setattr(stu, "sex", "男")
    sex = getattr(stu, "sex")
    print(sex)

    print("对不起，对象中没有指定的成员")

# 删除对象的属性
delattr(stu, "name")
print(stu.name)



# __import__(字符串模块名) # 动态导入指定模块
# getattr: 根据字符串在指定对象中获取成员
# setattr: 根据字符串在指定对象中设置成员
# delattr： 根据字符串在指定对象中删除成员
# hasattr： 判断字符串是否在指定对象中有该成员





