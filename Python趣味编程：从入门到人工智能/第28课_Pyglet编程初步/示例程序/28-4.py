'''
程序：显示GIF动画图像
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
import pyglet

game_win = pyglet.window.Window()

fish_gif = pyglet.image.load_animation('clown-fish.gif')
fish = pyglet.sprite.Sprite(fish_gif, x=200, y=200)

@game_win.event
def on_draw():
    game_win.clear()
    fish.draw()
    
pyglet.app.run()
