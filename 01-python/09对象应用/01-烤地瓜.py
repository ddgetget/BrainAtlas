

# 定义地瓜类
class SweetPotato(object):

    def __init__(self):
        # 对象属性信息
        # 烤的时间
        self.roast_time = 0
        # 烤的程度
        self.roast_state = "生的"
        # 佐料的列表属性
        self.condiment_list = []

    # 添加佐料的方法
    def add_condiment(self, condiment):
        self.condiment_list.append(condiment)

    # 烤地瓜的方法
    def roast(self, time):
        # 修改烤的时间
        self.roast_time += time

        # 根据时间判断地瓜的程度(状态)
        if self.roast_time > 8:
            self.roast_state = "烤糊了"

        elif self.roast_time > 5:
            self.roast_state = "烤熟了"

        elif self.roast_time > 3:
            self.roast_state = "半生不熟"

    def __str__(self):
        if self.condiment_list:
            # 根据指定分隔符拼接字符串数据
            result = ",".join(self.condiment_list)

            return self.roast_state + "地瓜" + "[" + result + "]"
        else:
            return self.roast_state + "地瓜"


# 创建地瓜对象
sweet_potato = SweetPotato()
print("---------------地瓜准备好了可以开始烤啦--------------------")
print(sweet_potato)
print("---------------烤3分钟--------------------")
sweet_potato.roast(3)
print(sweet_potato)
print("---------------再继续烤3分钟--------------------")
sweet_potato.roast(4)
print(sweet_potato)
print("---------------添加佐料--------------------")
# 添加佐料
sweet_potato.add_condiment("番茄酱")
sweet_potato.add_condiment("芥末")
print(sweet_potato)

