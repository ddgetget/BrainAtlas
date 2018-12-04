# 定义人类
class Person(object):
    def __init__(self, name):
        # 人的名字
        self.name = name
        # 枪的属性
        self.gun = None
        # 血量
        self.hp = 100

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

    # 拿枪
    def get_gun(self, gun):
        self.gun = gun

    # 掉血
    def hurt(self, damage):
        self.hp -= damage

    # 开枪
    def fire(self, enemy):
        # 老王.枪.shot(enemy)
        self.gun.shot(enemy)


    # 显示人类的描述信息
    def __str__(self):
        if self.gun:
            return "%s的血量:%d %s" % (self.name, self.hp, self.gun)
        else:
            if self.hp <= 0:
                return "%s已挂!!!" % self.name
            else:
                return "%s的血量:%d 他没有枪" % (self.name, self.hp)



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

    # 射击
    def shot(self, enemy):
        # 1. 从弹夹中获取一颗子弹
        # 弹夹.弹出一颗子弹()
        bullet = self.cartridge.pop_bullet()
        if bullet:
            # 2. 子弹去击中敌人
            bullet.hit(enemy)
        else:
            print("对不起，没有子弹了")

    def __str__(self):
        if self.cartridge:
            return "枪的信息: %s %s" % (self.name, self.cartridge)
        else:
            return "枪的信息: %s" % self.name


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

    # 弹出一颗子弹
    def pop_bullet(self):
        if self.bullet_list:
            # 获取最后一颗子弹,并且从子弹列表中移除
            bullet = self.bullet_list.pop()
            return bullet
        else:
            return None


    def __str__(self):
        return "弹夹的信息: %d/%d" % (len(self.bullet_list), self.max_num)


# 定义子弹类
class Bullet(object):
    def __init__(self, damage):
        # 威力
        self.damage = damage

    # 让子弹击中敌人
    def hit(self, enemy):
        # 敌人掉血
        enemy.hurt(self.damage)

if __name__ == '__main__':
    # 1. 创建老王对象
    lao_wang = Person("老王")

    # 2. 创建枪的对象
    ak_47 = Gun("AK47")

    # 3. 创建弹夹对象
    ak_47_cartridge = Cartridge(20)

    for i in range(10):
        # 4. 创建子弹对象
        ak_47_bullet = Bullet(50)

        # 5. 老王把子弹安装到弹夹里面
        # lao_wang.安装(子弹，弹夹)
        lao_wang.install_bullet_to_cartridge(ak_47_bullet, ak_47_cartridge)

    # 6. 老王把弹夹安装到枪里面
    # lao_wang.安装(弹夹，枪)
    lao_wang.install_cartridge_to_gun(ak_47_cartridge, ak_47)

    # 测试： 显示枪的信息和弹夹的信息
    print(ak_47)
    print(ak_47_cartridge)

    # 7. 老王拿起枪
    # lao_wang.拿枪(ak_47)
    lao_wang.get_gun(ak_47)
    print(lao_wang)

    # 8. 创建敌人对象
    lao_song = Person("老宋")
    print(lao_song)

    # 9. 老王向敌人开枪
    # lao_wang.开枪(敌人)
    lao_wang.fire(lao_song)
    print(lao_wang)
    print(lao_song)

    # lao_wang.开枪(敌人)
    lao_wang.fire(lao_song)
    print(lao_wang)
    print(lao_song)

    # lao_wang.开枪(敌人)
    lao_wang.fire(lao_song)
    print(lao_wang)
    print(lao_song)