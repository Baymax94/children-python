import pygame
pygame.init()  # 启动pygame
screen = pygame.display.set_mode([600,600])  # 创建一个宽800像素，高600像素的显示窗口
keep_going = True
# pic = pygame.image.load("D:\Users\Baymax\Desktop\child\8\CrazySmile.bmp")
pic = pygame.image.load("CrazySmile.bmp") 
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    picx += 1
    picy += 1
    screen.blit(pic,(picx,picy))
    pygame.display.update()
pygame.quit()