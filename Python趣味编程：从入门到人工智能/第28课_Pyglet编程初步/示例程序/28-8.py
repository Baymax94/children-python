'''
程序：键盘事件
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
import pyglet
from pyglet.window import key

game_win = pyglet.window.Window()

@game_win.event
def on_key_press(symbol, modifiers):
    if symbol == key.ENTER:
        print('回车键被按下')
    elif symbol == key.LEFT:
        print('左方向键被按下')
    elif symbol == key.A:
        print('字母键A被按下')
    elif symbol == key._1:
        print('数字键1被按下')
    elif modifiers & key.MOD_CTRL:
        print('CTRL键被按下')
        print(modifiers & key.MOD_CTRL, modifiers, key.MOD_CTRL)

@game_win.event
def on_draw():
    game_win.clear()

pyglet.app.run()
