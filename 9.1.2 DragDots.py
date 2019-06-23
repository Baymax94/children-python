import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Click to drag to draw")
keep_going = True
# RED = (255,0,0)
YELLOW = (255,255,0)
radius = 15
mousedown = False

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
    if mousedown:
        spot = pygame.mouse.get_pos()
        pygame.draw.circle(screen,YELLOW,spot,radius)
    pygame.display.update()
pygame.quit()