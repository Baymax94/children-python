'''
程序：用鼠标控制角色移动
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
import pyglet

game_win = pyglet.window.Window()
plan_img = pyglet.resource.image('plan.png')
plan = pyglet.sprite.Sprite(plan_img)

@game_win.event
def on_mouse_motion(x, y, dx, dy):
    print(dx, dy)
    plan.x, plan.y = x, y

@game_win.event
def on_draw():
    game_win.clear()
    plan.draw()

pyglet.app.run()
