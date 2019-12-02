'''
程序：鼠标的按下、释放、拖动事件
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
提示：程序运行后，在窗口上对鼠标进行按下、拖动等操作
'''
import pyglet
from pyglet.window import mouse
from pyglet.window import key

game_win = pyglet.window.Window()

@game_win.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('在窗口(%d,%d)处按下鼠标左键' % (x, y))

@game_win.event
def on_mouse_release(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('在窗口(%d,%d)处松开鼠标左键' % (x, y))

@game_win.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if buttons & mouse.LEFT:
        print('拖动时按下的是鼠标左键')
    if modifiers & key.MOD_CTRL:
        print('在窗口(%d,%d)处拖动鼠标，并按下键盘CTRL键' % (x, y))

#game_win.push_handlers(pyglet.window.event.WindowEventLogger())
pyglet.app.run()
