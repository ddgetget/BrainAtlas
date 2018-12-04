import pygame
import random

# 屏幕的宽度
SCREEN_WIDTH = 512
# 屏幕的高度
SCREEN_HEIGHT = 768

# 英雄飞机类
class HeroPlane(object):
    def __init__(self):
        # 加载英雄飞机的图片对象
        self.hero_img = pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/hero2.png")
        # 获取图片的矩形对象
        self.hero_img_rect = self.hero_img.get_rect()
        # 修改矩形对象的位置
        self.hero_img_rect[0] = SCREEN_WIDTH / 2 - self.hero_img_rect[2] / 2
        self.hero_img_rect[1] = SCREEN_HEIGHT - self.hero_img_rect[3] - 20

        # 移动速度
        self.speed = 5

    # 上
    def move_up(self):
        if self.hero_img_rect[1] > 0:
            self.hero_img_rect.move_ip(0, -self.speed)

    # 下
    def move_down(self):
        if self.hero_img_rect[1] < SCREEN_HEIGHT - self.hero_img_rect[3]:
            self.hero_img_rect.move_ip(0, self.speed)

    # 左
    def move_left(self):
        if self.hero_img_rect[0] > 0:
            self.hero_img_rect.move_ip(-self.speed, 0)

    # 右边
    def move_right(self):
        if self.hero_img_rect[0] < SCREEN_WIDTH - self.hero_img_rect[2]:
            self.hero_img_rect.move_ip(self.speed, 0)



# 游戏地图类
class GameMap(object):
    def __init__(self):
        # 获取背景图片的随机数字
        random_num = random.randint(1, 5)
        # 加载背景图片1
        self.bg_img1 =  pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/img_bg_level_%d.jpg" % random_num)
        # 加载背景图片2
        self.bg_img2 = pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/img_bg_level_%d.jpg" % random_num)


        # 获取背景2图片的矩形对象
        self.bg_img2_rect = self.bg_img2.get_rect()
        # 修改背景图片的矩形对象的位置
        self.bg_img2_rect[1] = -SCREEN_HEIGHT
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
        if self.bg_img1_rect[1] >= SCREEN_HEIGHT:
            print("第一张背景图片超出了屏幕")
            print("第一张:", self.bg_img1_rect[1])
            self.bg_img1_rect[1] = 0-SCREEN_HEIGHT

        if self.bg_img2_rect[1] >= SCREEN_HEIGHT:
            print("第二张背景图片超出了屏幕")
            print("第二张:", self.bg_img2_rect[1])
            self.bg_img2_rect[1] = -SCREEN_HEIGHT






# 游戏窗口类
class GameWindow(object):
    def __init__(self):
        # 初始化pygame
        pygame.init()
        # 创建游戏窗口
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # 设置窗口的标题
        pygame.display.set_caption("飞机大战")
        # 加载图标对象
        app_img = pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/app.ico")
        # 设置窗口的图标
        pygame.display.set_icon(app_img)

        # 创建一个地图对象
        self.game_map = GameMap()
        # 创建英雄飞机对象
        self.hero = HeroPlane()

    # 程序运行的方法
    def run(self):
        # 游戏运行起来就是一个大循环，需要循环获取窗口的事件
        while True:
            # 获取窗口事件
            event_list = pygame.event.get()
            for event in event_list:
                # 判断事件的类型
                if event.type == pygame.QUIT:
                    # 代码执行到此说明用户点击的关闭按钮
                    exit()
                elif event.type == pygame.KEYDOWN:
                    # 判断按键操作
                    if event.key == pygame.K_ESCAPE:
                        # 按下的是esc键
                        exit()
                    elif event.key == pygame.K_SPACE:
                        print("biubiu~")

            # 获取长按键的列表，判断关心的长按的键对应的value值是否为1
            key_list = pygame.key.get_pressed()
            if key_list[pygame.K_UP] or key_list[pygame.K_w]:
                self.hero.move_up()
            elif key_list[pygame.K_DOWN]:
                self.hero.move_down()
            elif key_list[pygame.K_LEFT]:
                self.hero.move_left()
            elif key_list[pygame.K_RIGHT]:
                self.hero.move_right()

            # 让地图先滚动
            self.game_map.scoll_map()
            # 绘制地图图片对象
            self.window.blit(self.game_map.bg_img1, (self.game_map.bg_img1_rect[0], self.game_map.bg_img1_rect[1]))
            # 绘制地图图片对象
            self.window.blit(self.game_map.bg_img2, (self.game_map.bg_img2_rect[0], self.game_map.bg_img2_rect[1]))

            # 绘制英雄飞机图片到窗口
            self.window.blit(self.hero.hero_img, (self.hero.hero_img_rect[0], self.hero.hero_img_rect[1]))
            # 刷新窗口，显示图片对象
            pygame.display.update()

if __name__ == '__main__':
    # 测试代码
    game_window = GameWindow()
    # 运行游戏
    game_window.run()