'''
程序：hello, world
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
import pyglet

game_win = pyglet.window.Window()
label = pyglet.text.Label('hello, world', x=0, y=0)

@game_win.event
def on_draw():
    game_win.clear()
    label.draw()

pyglet.app.run()
