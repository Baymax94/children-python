'''
程序：捕鱼达人v1
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
import pyglet
from sprite_plus import SpritePlus
from game_res import *

#全局变量
fishes, bullets, nets, coins = [], [], [], []
score, game_time, auto_play = 0, 0, False

#创建游戏窗口、面板、大炮、标签等
game_win = pyglet.window.Window(width=1024, height=768, caption='捕鱼达人')
panel = pyglet.sprite.Sprite(img=panel_img, x=130, y=0)
cannon = SpritePlus(img=cannon_img, x=554, y=20)
cannon.set_sprite_center()
score_label = pyglet.text.Label('000000', x=165, y=6)
score_label.font_name = 'Arial Black'
score_label.font_size = 18

@game_win.event
def on_mouse_motion(x, y, dx, dy):
    '''大炮面向鼠标转动'''
    cannon.point(x, y)
        
@game_win.event
def on_draw():
    '''绘制游戏画面'''
    bg_img.blit(0, 0)
    panel.draw()
    score_label.draw()
    cannon.draw()
            
if __name__ == '__main__':
    '''程序入口'''
    pyglet.app.run()
