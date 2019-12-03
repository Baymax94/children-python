'''
程序：公主迎圣诞的资源
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
import pyglet

def center_image(image):
    '''设置图片的锚点为中心'''
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

#修改资源路径
pyglet.resource.path = ['./res/images', './res/sounds']

#加载图像资源
welcome_img = pyglet.resource.image('game_welcome.png')
end_img = pyglet.resource.image('game_end.png')
bg_img = pyglet.resource.image('game_play.png')
heart1_img = pyglet.resource.image('heart1.png')
heart2_img = pyglet.resource.image('heart2.png')
heart3_img = pyglet.resource.image('heart3.png')
clipper_img = pyglet.resource.image('剪刀.png')
snowflake_img = pyglet.resource.image('雪花.png')
gift_img = pyglet.resource.image('礼物.png')
princess_img = pyglet.resource.image('公主.png')

#修改图像锚点
center_image(clipper_img)
center_image(snowflake_img)
center_image(gift_img)
center_image(princess_img)

#加载声音资源
music = pyglet.resource.media('铃儿响叮当.m4a', streaming=False)
pop_sound = pyglet.resource.media('pop.wav', streaming=False)
