import pygame
import core_data
import game_map
import game_hero
import game_enemy

# 游戏窗口类
class GameWindow(object):
    def __init__(self):
        # 初始化pygame
        pygame.init()
        # 创建游戏窗口
        self.window = pygame.display.set_mode((core_data.SCREEN_WIDTH, core_data.SCREEN_HEIGHT))
        # 设置窗口的标题
        pygame.display.set_caption("飞机大战")
        # 加载图标对象
        app_img = pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/app.ico")
        # 设置窗口的图标
        pygame.display.set_icon(app_img)

        # 创建一个地图对象
        self.game_map = game_map.GameMap()
        # 创建英雄飞机对象
        self.hero = game_hero.HeroPlane()
        # 敌机列表
        self.enemy_list = [game_enemy.EnemyPlane() for _ in range(5)]
        # 播放背景音乐
        self.play_bg_music()

        # 创建爆炸音效对象
        self.bz_sound = pygame.mixer.Sound("/mnt/hgfs/WorkSpace/data/planeBattle/res/baozha.ogg")
        # 创建游戏结束的音效
        self.over_sound = pygame.mixer.Sound("/mnt/hgfs/WorkSpace/data/planeBattle/res/gameover.wav")

        # 得分的属性
        self.score = 0


    # 播放背景音乐
    def play_bg_music(self):
        # 播放背景音乐
        pygame.mixer.music.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/bg2.ogg")
        pygame.mixer.music.play(-1)

    # 释放背景音乐
    def stop_bg_music(self):
        pygame.mixer.music.stop()


    # 处理窗口事件
    def handle_event(self):
        # 获取窗口事件
        event_list = pygame.event.get()
        for event in event_list:
            # 判断事件的类型
            if event.type == pygame.QUIT:
                # 代码执行到此说明用户点击的关闭按钮
                # 释放背景音乐和音效
                self.stop_bg_music()
                self.bz_sound.stop()
                exit()
            elif event.type == pygame.KEYDOWN:
                # 判断按键操作
                if event.key == pygame.K_ESCAPE:
                    # 按下的是esc键
                    # 释放背景音乐和音效
                    self.stop_bg_music()
                    self.bz_sound.stop()
                    exit()
                elif event.key == pygame.K_SPACE:
                    # 发射子弹
                    self.hero.shot()

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


    # 移动和绘制图片
    def move_draw(self):
        # 让地图先滚动
        self.game_map.scoll_map()
        # 绘制地图图片对象
        self.window.blit(self.game_map.bg_img1, (self.game_map.bg_img1_rect[0], self.game_map.bg_img1_rect[1]))
        # 绘制地图图片对象
        self.window.blit(self.game_map.bg_img2, (self.game_map.bg_img2_rect[0], self.game_map.bg_img2_rect[1]))

        # 绘制英雄飞机图片到窗口
        self.window.blit(self.hero.hero_img, (self.hero.hero_img_rect[0], self.hero.hero_img_rect[1]))

        # 遍历每一个敌机，然后让敌机往下移动，然后绘制敌机移动后的位置在窗口上显示
        for enemy in self.enemy_list:
            # 让敌机移动
            enemy.move_down()
            self.window.blit(enemy.enemy_img, (enemy.enemy_img_rect[0], enemy.enemy_img_rect[1]))

        # 遍历子弹列表，找到发射的子弹，让子弹向上移动，然后在绘制移动后的子弹
        for bullet in self.hero.bullet_list:
            # 判断子弹的发射状态
            if bullet.is_shot:
                # 让子弹向上移动
                bullet.move_up()
                # 绘制子弹移动的位置
                self.window.blit(bullet.bullet_img, (bullet.bullet_img_rect[0], bullet.bullet_img_rect[1]))



        # 创建字体对象
        # font = pygame.font.SysFont("simhei", 25)
        # # 通过字体对象创建文字对象
        # txt_obj = font.render("得分:%d" % self.score, True, (255, 255, 255))
        # # 把文字绘制到游戏窗口上
        # self.window.blit(txt_obj, (10, 10))
        # 绘制得分信息
        self.draw_text(25, "得分:%d" % self.score, 10, 10)


    # 刷新游戏窗口的操作
    def window_update(self):
        # 刷新窗口，显示图片对象
        pygame.display.update()


    # 检测子弹和敌机碰撞的操作
    def bullet_hit_enemy(self):
        # 遍历子弹列表获取发射状态的子弹
        for bullet in self.hero.bullet_list:
            # 判断是否是发射状态的子弹
            if bullet.is_shot:
                # 遍历敌机列表，让发射状态的子弹和每一个敌机检测是否发生了碰撞
                for enemy in self.enemy_list:
                    # 检测子弹和敌机的矩形对象是否有重叠，有重叠表示碰撞
                    if pygame.Rect.colliderect(bullet.bullet_img_rect, enemy.enemy_img_rect):
                        # 碰撞啦
                        # 播放爆炸的音效
                        self.bz_sound.play()
                        # 击毁一架敌机加1分
                        self.score += 1
                        # 1. 子弹的状态改成未发射状态
                        bullet.is_shot = False
                        # 2. 敌机的位置重置
                        enemy.reset()
                        # 提示如果子弹和某一个敌机碰撞了，那么跳出循环，不要再循环比较下一个敌机的矩形对象了
                        break


    # 检测英雄飞机和敌机是否碰撞
    def hero_hit_enemy(self):
        # 遍历敌机列表
        for enemy in self.enemy_list:
            if pygame.Rect.colliderect(self.hero.hero_img_rect, enemy.enemy_img_rect):
                # 有碰撞
                return True
        else:
            # 每个敌机和我的英雄飞机都没有碰撞，那么返回False
            return False

    # 显示文字信息
    def draw_text(self, font_size, text, x, y):
        # 创建字体对象
        font = pygame.font.SysFont("simhei", font_size)
        # 通过字体对象创建文字对象
        txt_obj = font.render(text, True, (255, 255, 255))
        # 把文字绘制到游戏窗口上
        self.window.blit(txt_obj, (x, y))

    # 程序运行的方法
    def run(self):
        # 游戏运行起来就是一个大循环，需要循环获取窗口的事件
        while True:
            # 窗口事件处理
            self.handle_event()
            # 移动和绘制处理
            self.move_draw()
            # 刷新窗口
            self.window_update()
            # 检测子弹和敌机的碰撞操作
            self.bullet_hit_enemy()
            # 检测敌机和英雄飞机是否碰撞
            result = self.hero_hit_enemy()
            if result:
                # 代码执行到此说明有碰撞，游戏结束
                break

        # 游戏结束
        self.game_over()

    def game_over(self):
        # 停止背景音乐的播放
        self.stop_bg_music()
        # 播放游戏结束的音效
        self.over_sound.play()
        #
        # font = pygame.font.SysFont("simhei", 30)
        # # 通过字体对象创建文字对象
        # txt_obj = font.render("游戏结束(ESC 退出), 得分:%d" % self.score, True, (255, 255, 255))
        # # 把文字绘制到游戏窗口上
        # self.window.blit(txt_obj, (80, 350))
        # 游戏结束显示最终的得分
        self.draw_text(30, "游戏结束(ESC 退出), 得分:%d" % self.score, 80, 350)
        # 刷新窗口显示结束的文字
        self.window_update()

        # 循环获取窗口的操作事件
        while True:
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    # 键盘按下的事件
                    if event.key == pygame.K_ESCAPE:
                        exit()