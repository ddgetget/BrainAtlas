import pygame
import time

# 初始化
pygame.init()
# 创建游戏窗口
window = pygame.display.set_mode((512, 768))
# 设置标题
pygame.display.set_caption("飞机大战")
# 加载窗口的图标对象
app_img = pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/app.ico")
# 设置窗口图标
pygame.display.set_icon(app_img)

# 加载背景图片
bg_img = pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/img_bg_level_1.jpg")
# 加载敌机图片
enemy_img = pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/img-plane_1.png")

# 1. 控制敌机的y坐标，然后每次给y坐标加上一个指定的数据
# y = 0
# y += 10
# y += 10
# 2. 使用图片的矩形对象，然后移动矩形对象，然后把图片绘制到矩形对象的位置
# 获取敌机的矩形对象, 矩形对象包含: x，y,width,heigh
# <rect(0, 0, 100, 68)>: 第一个参数是x坐标，第二个参数是y坐标，第三个参数是宽度，第四个参数是高度
enemy_img_rect = enemy_img.get_rect() # 矩形对象默认坐标(0, 0)
print(enemy_img_rect)
# 修改矩形对象的坐标
enemy_img_rect[0] = 512 / 2 - enemy_img_rect[2] / 2
enemy_img_rect[1] = 0
print(enemy_img_rect)


# 循环移动矩形对象让敌机移动
for i in range(10):
    # 移动敌机的矩形对象
    enemy_img_rect.move_ip(0, 10)
    print(enemy_img_rect)

    # 把图片绘制到窗口上
    window.blit(bg_img, (0, 0))

    # 设置敌机移动后的位置
    # 把敌机图片绘制到窗口上
    # 图片的位置是依赖于矩形对象的位置
    window.blit(enemy_img, (enemy_img_rect[0], enemy_img_rect[1]))
    # 刷新窗口
    pygame.display.update()
    time.sleep(0.2)








input("")
