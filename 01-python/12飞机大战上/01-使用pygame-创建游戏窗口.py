import pygame  #导入pygame的包

# 初始化pygame，让硬件做好准备
pygame.init()

# 创建游戏窗口
window = pygame.display.set_mode((500, 500))

# 设置窗口的标题
pygame.display.set_caption("飞机大战")
# 加载窗口图标
app_img = pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/app.ico")
# 设置窗口的图标
pygame.display.set_icon(app_img)

input("")

