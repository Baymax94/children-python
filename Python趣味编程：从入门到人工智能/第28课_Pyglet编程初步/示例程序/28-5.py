'''
程序：播放音乐
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
提示：程序会在后台运行，播放完毕会自动结束
'''
import pyglet

mp3 = pyglet.resource.media('music.mp3')
mp3.play()

#mp3 = pyglet.resource.media('music.mp3', streaming=False)
#mp3.play()

#wav = pyglet.media.load('ball.wav', streaming=False)
#wav.play()
