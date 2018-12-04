# 房子里面存放家具


# 定义房子类
class Home(object):
    def __init__(self, area):
        # 可用面积
        self.area = area
        # 家具列表
        self.furniture_list = []

    # 存放家具的方法
    def add_furniture(self, furniture):
        if self.area > furniture.area:
            # 添加家具
            self.furniture_list.append(furniture)
            # 修改可用面积
            self.area -= furniture.area
        else:
            print("对不起，房子的可用面积是:%d 家具的名字:%s 面积:%d" % (self.area, furniture.name, furniture.area))

    def __str__(self):

        if self.furniture_list:

            # 家具名字的列表
            furniture_name_list = [furniture.name for furniture in self.furniture_list]
            # print(furniture_name_list)
            # 如果想要进行拼接字符串数据，容器类型中的数据必须是字符串
            result = ",".join(furniture_name_list)

            return "房子的可用面积:%d" % self.area + " 家具列表:[%s]" % result
        else:
            return "房子的可用面积:%d" % self.area


# 定义家具类
class Furniture(object):
    def __init__(self,name, area):
        # 品牌
        self.name = name
        # 家具的面积
        self.area = area

    def __str__(self):
        return "家具的名称:%s 面积:%d" % (self.name, self.area)


# 创建房子对象
home = Home(130)
print(home)
# 创建家具
tv = Furniture("TV", 90)
print(tv)
home.add_furniture(tv)

bx = Furniture("BX", 90)
print(bx)
home.add_furniture(bx)
print(home)

