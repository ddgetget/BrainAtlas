import random
import core_data
import pygame

# 敌机类
class EnemyPlane(object):
    def __init__(self):
        # 生成一个1-7的随机数字
        random_num = random.randint(1, 7)
        # 加载敌机图片
        self.enemy_img = pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/img-plane_%d.png" % random_num)
        # 获取图片的矩形对象
        self.enemy_img_rect = self.enemy_img.get_rect()
        # 随机产生一个x坐标
        random_x = random.randint(0, core_data.SCREEN_WIDTH - self.enemy_img_rect[2])
        # 设置矩形对象的位置
        self.enemy_img_rect[0] = random_x
        self.enemy_img_rect[1] = -self.enemy_img_rect[3]

        # 移动速度
        self.speed = random.randint(4, 6)

    # 重置敌机位置
    def reset(self):
        # 随机产生一个x坐标
        random_x = random.randint(0, core_data.SCREEN_WIDTH - self.enemy_img_rect[2])
        # 设置矩形对象的位置
        self.enemy_img_rect[0] = random_x
        self.enemy_img_rect[1] = -self.enemy_img_rect[3]

        # 移动速度
        self.speed = random.randint(4, 6)


    # 敌机往下移动的方法
    def move_down(self):
        self.enemy_img_rect.move_ip(0, self.speed)

        # 判断敌机的矩形对象的y坐标是否大于屏幕的高度，如果大于说明飞机已经超出屏幕需要重新设置位置到顶部外
        if self.enemy_img_rect[1] > core_data.SCREEN_HEIGHT:
            # 重置敌机的位置
            self.reset()