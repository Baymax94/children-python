'''
程序：显示图像
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
import pyglet

game_win = pyglet.window.Window()

img = pyglet.image.load('kitten.jpg')

#pyglet.resource.path = ['res']
#pyglet.resource.reindex()
#img = pyglet.image.load('res/kitten.jpg')

@game_win.event
def on_draw():
    game_win.clear()
    img.blit(0, 0)

pyglet.app.run()
