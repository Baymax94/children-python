import pygame
pygame.init()  # 启动pygame
screen = pygame.display.set_mode([800,600])  # 创建一个宽800像素，高600像素的显示窗口
keep_going = True
# pic = pygame.image.load("D:\Users\Baymax\Desktop\child\8\CrazySmile.bmp")
pic = pygame.image.load("CrazySmile.bmp") 
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    screen.blit(pic,(100,100))
    pygame.display.update()
pygame.quit()