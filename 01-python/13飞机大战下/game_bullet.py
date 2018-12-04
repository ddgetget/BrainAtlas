import random
import pygame

# 子弹类
class Bullet(object):
    def __init__(self):
        # 产生一个9-14的随机数
        random_num = random.randint(9, 14)
        # 加载子弹的图片对象
        self.bullet_img = pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/bullet_%d.png" % random_num)

        # 获取子弹图片的矩形对象，因为图片的移动都是通过矩形对象来控制的
        self.bullet_img_rect = self.bullet_img.get_rect()
        # 子弹的速度
        self.speed = 5
        # 子弹的状态
        self.is_shot = False

    # 子弹向上移动的方法
    def move_up(self):
        self.bullet_img_rect.move_ip(0, -self.speed)
        # 判断子弹是否超出屏幕外
        if self.bullet_img_rect[1] < -self.bullet_img_rect[3]:
            # 把子弹的状态改成未发射的状态
            self.is_shot = False