'''
程序：疯狂摩托v1
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
import pyglet
from pyglet.window import key
from pyglet import clock
from random import randint
from math import sqrt
#------------------------------------------------------------------------
#加载资源
pyglet.resource.path = ['./res']
bg_img = pyglet.resource.image('沙漠.png')
motor_animation = pyglet.resource.animation('motor-red.gif')
box_img = pyglet.resource.image('box.png')
motor_sound = pyglet.resource.media('motor.wav', streaming=False)
alert_sound = pyglet.resource.media('alter.mp3', streaming=False)

#------------------------------------------------------------------------
#全局变量
motor_x = 0
motor_y = 40
motor_speed = 0
mileages = 0

#创建窗口
game_win = pyglet.window.Window(width=600, height=295, caption='疯狂摩托')
#创建角色
motor = pyglet.sprite.Sprite(img=motor_animation, x=50, y=40)
box = pyglet.sprite.Sprite(img=box_img, x=500, y=10)
#文本标签
speed_label = pyglet.text.Label('Speed: 0', x=10, y=280)
mileages_label = pyglet.text.Label('Mileages: 0', x=10, y=260)
#音乐播放器
motor_player = pyglet.media.Player()
alert_player = pyglet.media.Player()

@game_win.event
def on_draw():
    '''绘制游戏画面'''
    global motor_x
    bg_img.blit(0 - int(motor_x) % 600, 0)
    bg_img.blit(600 - int(motor_x) % 600, 0)
    
    if motor.y > box.y:
        motor.draw()
        box.draw()
    else:
        box.draw()
        motor.draw()

    speed_label.draw()
    mileages_label.draw()
    
if __name__ == '__main__':
    '''程序入口'''
    pyglet.app.run()
