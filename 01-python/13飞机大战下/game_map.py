import random
import pygame
import core_data

# 游戏地图类
class GameMap(object):
    def __init__(self):
        # 获取背景图片的随机数字
        random_num = random.randint(1, 5)
        # 加载背景图片1
        self.bg_img1 = pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/img_bg_level_%d.jpg" % random_num)
        # 加载背景图片2
        self.bg_img2 = pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/img_bg_level_%d.jpg" % random_num)


        # 获取背景2图片的矩形对象
        self.bg_img2_rect = self.bg_img2.get_rect()
        # 修改背景图片的矩形对象的位置
        self.bg_img2_rect[1] = -core_data.SCREEN_HEIGHT
        self.bg_img2_rect[0] = 0

        # 获取背景1图片的矩形对象
        self.bg_img1_rect = self.bg_img1.get_rect()
        self.bg_img1_rect[1] = 0
        self.bg_img1_rect[0] = 0

        # 地图滚动的速度
        self.speed = 3

    # 地图滚动
    def scoll_map(self):
        # 矩形对象每次移动指定的大小
        self.bg_img1_rect.move_ip(0, self.speed)
        self.bg_img2_rect.move_ip(0, self.speed)

        # 判断矩形对象的y轴是否超出屏幕
        if self.bg_img1_rect[1] >= core_data.SCREEN_HEIGHT:
            print("第一张背景图片超出了屏幕")
            print("第一张:", self.bg_img1_rect[1])
            self.bg_img1_rect[1] = 0-core_data.SCREEN_HEIGHT

        if self.bg_img2_rect[1] >= core_data.SCREEN_HEIGHT:
            print("第二张背景图片超出了屏幕")
            print("第二张:", self.bg_img2_rect[1])
            self.bg_img2_rect[1] = -core_data.SCREEN_HEIGHT

