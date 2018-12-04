import pygame

# 初始化pygame
pygame.init()
# 创建游戏窗口
window = pygame.display.set_mode((512, 768))
# 设置标题
pygame.display.set_caption("飞机大战")
# 加载窗口的图标对象
app_img = pygame.image.load("res/app.ico")
# 设置图标
pygame.display.set_icon(app_img)

# 加载背景图片
bg_img = pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/img_bg_level_1.jpg")

# 创建背景音乐
pygame.mixer.music.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/bg2.ogg")
# 播放背景音乐，默认表示播放一次
# 循环播放使用-1
pygame.mixer.music.play(-1)

# 创建音效
sound = pygame.mixer.Sound("/mnt/hgfs/WorkSpace/data/planeBattle/res/baozha.ogg")

# 游戏其实就是一个死循环，这里需要循环获取窗口的事件，因为用户是有可能对窗口进行操作
while True:
    # 获取窗口事件
    event_list = pygame.event.get()
    # print(event_list, type(event_list))

    # 遍历事件列表判断事件的类型
    for event in event_list:
        if event.type == pygame.QUIT:
            # 停止播放背景音乐
            pygame.mixer.music.stop()
            # 停止播放音效
            sound.stop()
            # 退出程序
            exit()
        elif event.type == pygame.KEYDOWN:
            # 代码执行到此说明是键盘按下的事件类型，判断按下的键
            if event.key == pygame.K_ESCAPE:
                # 停止播放背景音乐
                pygame.mixer.music.stop()
                # 停止播放音效
                sound.stop()
                exit()
            elif event.key == pygame.K_SPACE:
                print("biubiu")
                # 播放爆炸音效
                sound.play()
            # elif event.key == pygame.K_a:
            #     print("a")

    # 获取长按键的列表
    key_list = pygame.key.get_pressed()
    # print(key_list)
    # 判断是否是关心长按的键，如果是键的对值是1， 否则是0
    if key_list[pygame.K_UP] == 1:
        print("上")
    elif key_list[pygame.K_DOWN]:
        print("下")
    elif key_list[pygame.K_LEFT]:
        print("左")
    elif key_list[pygame.K_RIGHT]:
        print("右")

    # 把背景图片进行绘制
    window.blit(bg_img, (0, 0))

    # 刷新游戏窗口
    pygame.display.update()



