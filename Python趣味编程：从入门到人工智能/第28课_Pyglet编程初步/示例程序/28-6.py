'''
程序：用媒体播放器播放音乐
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
提示：程序会在后台运行，播放完毕会自动结束
'''
import pyglet

sound1 = pyglet.resource.media('音乐珊瑚.mp3', streaming=False)
sound2 = pyglet.resource.media('music.mp3', streaming=False)

player = pyglet.media.Player()
player.queue(sound1)
player.queue(sound2)
player.queue(sound1)
player.queue(sound2)
player.play()
