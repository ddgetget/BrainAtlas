# 定义人类
class Person(object):
    def __init__(self, name):
        # 人的名字
        self.name = name

    # 安装子弹到弹夹
    @staticmethod
    def install_bullet_to_cartridge(bullet, cartridge):
        # 把子弹安装到弹夹里面
        # 弹夹.保存子弹(bullet)
        cartridge.save_bullet(bullet)

    # 安装弹夹到枪里面
    @staticmethod
    def install_cartridge_to_gun(cartridge, gun):
        # 枪.保存弹夹(cartridge)
        gun.save_cartridge(cartridge)


# 定义枪类
class Gun(object):
    def __init__(self, name):
        # 枪的名字
        self.name = name
        # 保存弹夹
        self.cartridge = None

    # 枪保存弹夹
    def save_cartridge(self, cartridge):
        self.cartridge = cartridge


# 定义弹夹类
class Cartridge(object):
    def __init__(self, num):
        # 弹夹的最大容量
        self.max_num = num
        # 弹夹记录子弹列表信息
        self.bullet_list = []

    # 保存子弹
    def save_bullet(self, bullet):
        # 把子弹保存到弹夹里面
        self.bullet_list.append(bullet)


# 定义子弹类
class Bullet(object):
    def __init__(self, damage):
        # 威力
        self.damage = damage

if __name__ == '__main__':
    # 1. 创建老王对象
    lao_wang = Person("老王")

    # 2. 创建枪的对象
    ak_47 = Gun("AK47")

    # 3. 创建弹夹对象
    ak_47_cartridge = Cartridge(20)

    # 4. 创建子弹对象
    ak_47_bullet = Bullet(50)

    # 5. 老王把子弹安装到弹夹里面
    # lao_wang.安装(子弹，弹夹)
    lao_wang.install_bullet_to_cartridge(ak_47_bullet, ak_47_cartridge)

    # 6. 老王把弹夹安装到枪里面
    # lao_wang.安装(弹夹，枪)
    lao_wang.install_cartridge_to_gun(ak_47_cartridge, ak_47)

    # 7. 老王拿起枪

    # 8. 创建敌人对象

    # 9. 老王向敌人开枪