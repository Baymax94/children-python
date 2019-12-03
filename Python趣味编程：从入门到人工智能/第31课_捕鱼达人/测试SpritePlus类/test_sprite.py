'''
程序：测试Sprite增强类
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
提示：在窗口点击鼠标，小鱼会朝向鼠标移动
'''
import pyglet
from sprite_plus import SpritePlus
    
game_win = pyglet.window.Window(width=1024, height=768)
fish_img = pyglet.resource.animation('小丑鱼.gif')
fish = SpritePlus(img=fish_img, x=300, y=300)
fish.set_sprite_center()
fish.rotation = 0

@game_win.event
def on_draw():
    '''绘制游戏画面'''
    game_win.clear()
    fish.draw()
     
@game_win.event                                  
def on_mouse_press(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        #面向鼠标指针移动10个像素
        fish.point(x, y)
        fish.move(10)
        
if __name__ == '__main__':
    '''程序入口'''
    pyglet.app.run()
