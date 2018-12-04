import pygame
import core_data
import game_bullet

# 英雄飞机类
class HeroPlane(object):
    def __init__(self):
        # 加载英雄飞机的图片对象
        self.hero_img = pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/hero2.png")
        # 获取图片的矩形对象
        self.hero_img_rect = self.hero_img.get_rect()
        # 修改矩形对象的位置
        self.hero_img_rect[0] = core_data.SCREEN_WIDTH / 2 - self.hero_img_rect[2] / 2
        self.hero_img_rect[1] = core_data.SCREEN_HEIGHT - self.hero_img_rect[3] - 20

        # 移动速度
        self.speed = 5

        # 飞机携带子弹列表, '_': 忽略不使用的参数
        self.bullet_list = [game_bullet.Bullet() for _ in range(5)]


    # 飞机发射子弹
    def shot(self):
        for bullet in self.bullet_list:
            # 遍历每一颗子弹，判断子弹的状态
            # if bullet.is_shot == False:
            if not bullet.is_shot:
                # 1. 把子弹改成发射状态
                bullet.is_shot = True
                # 2. 飞机发射子弹的时候，因为飞机的位置已经确定下来的，那么这个时候需要设置子弹的位置
                bullet.bullet_img_rect[0] = self.hero_img_rect[0] + self.hero_img_rect[2] / 2 - bullet.bullet_img_rect[2] / 2
                bullet.bullet_img_rect[1] = self.hero_img_rect[1] - bullet.bullet_img_rect[3]
                # 按下空格发射一颗子弹， 只改变一颗子弹的状态
                break

    # 上
    def move_up(self):
        if self.hero_img_rect[1] > 0:
            self.hero_img_rect.move_ip(0, -self.speed)

    # 下
    def move_down(self):
        if self.hero_img_rect[1] < core_data.SCREEN_HEIGHT - self.hero_img_rect[3]:
            self.hero_img_rect.move_ip(0, self.speed)

    # 左
    def move_left(self):
        if self.hero_img_rect[0] > 0:
            self.hero_img_rect.move_ip(-self.speed, 0)

    # 右边
    def move_right(self):
        if self.hero_img_rect[0] < core_data.SCREEN_WIDTH - self.hero_img_rect[2]:
            self.hero_img_rect.move_ip(self.speed, 0)

