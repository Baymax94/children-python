'''
程序：捕鱼达人的资源
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
import pyglet

#加载资源
pyglet.resource.path = ['../res/images', '../res/sounds']
music = pyglet.resource.media('音乐珊瑚.mp3', streaming=False)
bg_img = pyglet.resource.image('珊瑚海岸.jpg')
panel_img = pyglet.resource.image('panel.png')
cannon_img = pyglet.resource.image('cannon.png')
bullet_img = pyglet.resource.image('bullet.png')
fishing_net_img = pyglet.resource.image('fishing_net.png')
gold_coin_img = pyglet.resource.image('gold_coin.png')
silver_coin_img = pyglet.resource.image('silver_coin.png')

#鱼群配置表：鱼总数、活跃数、文件名、动画行数、是否转向、生命值、得分、鱼速度
fishes_config = {
    '小黄鱼':{'max':50, 'alive':0, 'turn':1, 'life':1, 'score':1, 'speed':40, 'file':'fish1.png', 'rows':8},
    '小丑鱼':{'max':35, 'alive':0, 'turn':1, 'life':2, 'score':3, 'speed':40, 'file':'fish2.png', 'rows':8},
    '红鱼':{'max':25, 'alive':0, 'turn':1, 'life':3, 'score':5, 'speed':40, 'file':'fish3.png', 'rows':8},
    '蓝鱼':{'max':20, 'alive':0, 'turn':1, 'life':3, 'score':8, 'speed':40, 'file':'fish4.png', 'rows':8},
    '河豚':{'max':9, 'alive':0, 'turn':1, 'life':5, 'score':10, 'speed':30, 'file':'fish5.png', 'rows':8},
    '鹦鹉螺':{'max':8, 'alive':0, 'turn':1, 'life':3, 'score':20, 'speed':30, 'file':'fish6.png', 'rows':12},
    '水母':{'max':8, 'alive':0, 'turn':1, 'life':4, 'score':30, 'speed':25, 'file':'fish7.png', 'rows':10},
    '灯笼鱼':{'max':9, 'alive':0, 'turn':1, 'life':5, 'score':40, 'speed':25, 'file':'fish8.png', 'rows':12},
    '魔鬼鱼':{'max':7, 'alive':0, 'turn':1, 'life':6, 'score':50, 'speed':30, 'file':'fish9.png', 'rows':12},
    '海龟':{'max':5, 'alive':0, 'turn':1, 'life':8, 'score':60, 'speed':30, 'file':'fish10.png', 'rows':10},
    '蓝鲨':{'max':1, 'alive':0, 'turn':0, 'life':10, 'score':100, 'speed':25, 'file':'shark1.png', 'rows':12},
    '金鲨':{'max':1, 'alive':0, 'turn':0, 'life':12, 'score':200, 'speed':25, 'file':'shark2.png', 'rows':12},
    }
