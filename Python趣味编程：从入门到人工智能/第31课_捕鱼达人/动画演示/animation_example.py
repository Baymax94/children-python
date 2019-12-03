'''
程序：动画演示
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
import pyglet
from pyglet.image import ImageGrid
from pyglet.image import Animation

game_win = pyglet.window.Window(width=1024, height=768)
image = pyglet.resource.image('fish2.png')

img_seq = ImageGrid(image, 8, 1)
print(len(img_seq))
animation = Animation.from_image_sequence(img_seq[:3:-1], 0.2)
fish = pyglet.sprite.Sprite(animation, 500, 300)

@game_win.event
def on_draw():
    game_win.clear()
    img_seq[0].blit(0,0)
    fish.draw()
    
if __name__ == '__main__':
    pyglet.app.run()
