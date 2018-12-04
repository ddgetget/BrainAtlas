import pygame

# 初始化pygame
pygame.init()

# 创建游戏窗口 512, 768px
window = pygame.display.set_mode((512, 768))
# 设置标题
pygame.display.set_caption("飞机大战")
# 加载app.ico的图片对象
app_img = pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/app.ico")
# 设置窗口的图标
pygame.display.set_icon(app_img)

# 加载背景图片对象
bg_img = pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/img_bg_level_2.jpg")
# 把背景图片绘制到游戏窗口上
window.blit(bg_img, (0, 0))
# 提示： 绘制完成以后需要刷新一下窗口
pygame.display.update()


input("")