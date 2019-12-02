'''
程序：显示PNG图像
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
提示：PNG格式的图片支持透明，能够与窗口背景融合
'''
import pyglet

game_win = pyglet.window.Window()

plan_img = pyglet.resource.image('plan.png')
plan = pyglet.sprite.Sprite(plan_img, x=200, y=200)

@game_win.event
def on_draw():
    game_win.clear()
    plan.draw()
    
pyglet.app.run()
