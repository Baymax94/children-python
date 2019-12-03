'''
程序：公主迎圣诞v3
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
import pyglet
from pyglet.window import key
from pyglet import clock
from game_res import *
from falling_object import *

#游戏状态：0-等待状态，1-进行状态，2-结束状态
game_state = 0

#创建游戏窗口
game_win = pyglet.window.Window(width=800, height=600)
game_win.set_caption('公主迎圣诞')

#创建角色
princess = pyglet.sprite.Sprite(princess_img, 400, 150)
falling_obj = FallingObject()

#绘制游戏画面
@game_win.event
def on_draw():
    global game_state
    game_win.clear()
    if game_state == 0:
        welcome_img.blit(0, 0)
    elif game_state == 1:
        bg_img.blit(0, 0)
        princess.draw()
        falling_obj.draw()
    elif game_state == 2:
        end_img.blit(0, 0)
        
#响应键盘事件
@game_win.event
def on_key_press(symbol, modifiers):
    global game_state
    if symbol == key.ENTER:
        if game_state != 1:
            game_state = 1
            falling_obj.change()

    #用于测试游戏结束的情况
    if symbol == key.SPACE:
        game_state = 2

#控制公主左右移动
def princess_control(dt):
    global game_state
    if game_state != 1:
        return
    
    if keys[key.LEFT]:
        princess.x -= 400 * dt
        if princess.x < princess.width / 2:
            princess.x = princess.width / 2
    elif keys[key.RIGHT]:
        princess.x += 400 * dt
        if princess.x > 800 - princess.width / 2:
            princess.x = 800 - princess.width / 2
            
def falling_control(dt):
    '''礼物精灵的控制'''
    global game_state
    if game_state != 1:
        return
    
    #控制礼物的落下速度和旋转速度
    falling_obj.rotation += 60 * dt
    falling_obj.y -= 200 * dt
    if falling_obj.y < 0:
        falling_obj.change()
                   
#程序入口
if __name__ == '__main__':
    keys = key.KeyStateHandler()
    game_win.push_handlers(keys)
    clock.schedule_interval(princess_control, 1/60)
    clock.schedule_interval(falling_control, 1/60)
    pyglet.app.run()
