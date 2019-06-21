import pygame
 
 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
 
def draw_a_boy(screen,x,y):
    pygame.draw.ellipse(screen,black,[x,y-5,10,10])
    pygame.draw.line(screen,red,[5+x,5+y],[5+x,15+y],2)
    pygame.draw.line(screen,red,[5+x,5+y],[x-5,15+y],2)
    pygame.draw.line(screen,red,[5+x,5+y],[15+x,15+y],2)
    pygame.draw.line(screen,black,[5+x,15+y],[x-5,25+y],2)
    pygame.draw.line(screen,black,[5+x,15+y],[15+x,25+y],2)
 
 
 
 
pygame.init()
size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("a boy")
 
 
done = False
clock = pygame.time.Clock()
x=15
y=15
 
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
 
    pygame.mouse.set_visible(False)
    
 
    screen.fill(white)
    draw_a_boy(screen,x,y)
 
   
    clock.tick(20)
    pygame.display.flip()
 
pygame.quit()
        
        