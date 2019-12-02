'''
程序：用计划任务实现简单的字幕移动效果
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
import pyglet
from pyglet import clock

window = pyglet.window.Window()
label = pyglet.text.Label('hello, world')

@window.event
def on_draw():
    window.clear()
    label.draw()

def move(dt):
    label.x += int(100 * dt)
    if label.x > 300:
        clock.unschedule(move)

if __name__ == '__main__':
    clock.schedule_interval(move, 1/60)
    pyglet.app.run()
