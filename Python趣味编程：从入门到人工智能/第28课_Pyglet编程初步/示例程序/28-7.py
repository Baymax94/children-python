'''
程序：用媒体播放器播放视频
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
import pyglet

mov = pyglet.resource.media('美丽勾股树.mov')
game_win = pyglet.window.Window(width=mov.video_format.width,
                                height=mov.video_format.height)
player = pyglet.media.Player()
player.queue(mov)
player.play()

@game_win.event
def on_draw():
    game_win.clear()
    player.get_texture().blit(0, 0)

@game_win.event
def on_close():
    player.pause()

pyglet.app.run()
