'''
程序：捕鱼达人
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
import pyglet
from sprite_plus import SpritePlus
from game_res import *
from game_sprites import *

#全局变量
fishes, bullets, nets, coins = [], [], [], []
score, game_time, auto_play = 0, 0, False

#创建游戏窗口、面板、大炮、标签等
game_win = pyglet.window.Window(width=1024, height=768, caption='捕鱼达人')
panel = pyglet.sprite.Sprite(img=panel_img, x=130, y=0)
cannon = SpritePlus(img=cannon_img, x=554, y=20)
cannon.set_sprite_center()
score_label = pyglet.text.Label('000000', x=165, y=6)
score_label.font_name = 'Arial Black'
score_label.font_size = 18

@game_win.event
def on_mouse_motion(x, y, dx, dy):
    '''大炮面向鼠标转动'''
    cannon.point(x, y)
        
@game_win.event
def on_draw():
    '''绘制游戏画面'''
    bg_img.blit(0, 0)
    draw_sprites(fishes)
    draw_sprites(nets)
    draw_sprites(coins)
    panel.draw()
    score_label.draw()
    draw_sprites(bullets)
    cannon.draw()

def draw_sprites(sprites):
    '''绘制精灵'''
    for sprite in sprites:
        if sprite.visible:
            sprite.draw()
            
def fishes_control(dt):
    '''鱼群数量控制'''
    global game_time
    game_time += 1 * dt
    
    for fish_name, item in fishes_config.items():
        if item['alive'] == 0:
            num = item['max'] // 2
        elif item['alive'] < item['max'] // 3:
            num = item['max'] - item['alive']
        else:
            num = 0
           
        if fish_name == '蓝鲨' and int(game_time + 1) % 300 == 0:
            num = item['max'] - item['alive']
            
        if fish_name == '金鲨' and int(game_time + 1) % 480 == 0:
            num = item['max'] - item['alive']
        
        for i in range(num):
            fish = FishSprite(name=fish_name, item=item)
            item['alive'] += 1
            fishes.append(fish)
            
    #鱼群
    for fish in fishes:
        if fish.life > 0:
            fish.swim(dt)
        else:
            if not fish.is_capture:
                fish.is_capture = True
                #换成鱼扭动的造型
                fish.twist()
                #释放金币
                release_coin(fish.position, fish.score)
            else:
                #挣扎1秒后消失
                fish.check_dead(dt)
                
        if not fish.visible:
            #减少鱼的存活数
            fishes_config[fish.name]['alive'] -= 1
            fishes.remove(fish)
            fish.delete()

def fire_control(dt):
    '''捕鱼控制'''
    #炮弹
    for bullet in bullets:
        if bullet.visible:
            #移动炮弹
            bullet.fire_move(dt)
            if bullet.y < 150: continue
            #对每条有生命的鱼进行碰撞检测
            for fish in fishes:
                if fish.life <= 0: continue
                if bullet.touching(fish.position, fish.height // 2):
                    #命中鱼减去生命值
                    fish.life -= 1
                    #让炮弹消失
                    bullet.visible = False
                    #抛撒渔网在炮弹处
                    throw_fishing_net(fish.position)                  
        else:
            bullets.remove(bullet)
            bullet.delete()
            
    #渔网
    for net in nets:
        if net.visible:
            net.open(dt)
        else:
            nets.remove(net)
            net.delete()
                       
    #硬币
    for coin in coins:
        if coin.visible:
            coin.move_down(dt)
        else:
            #加分
            global score
            score += coin.score
            score_label.text = '%06d' % score
            coins.remove(coin)
            coin.delete()

def fire_bullet():
    '''发射炮弹'''
    bullet = BulletSprite(x=cannon.x, y=cannon.y)
    bullet.rotation = cannon.rotation
    bullets.append(bullet)

def throw_fishing_net(pos):
    '''抛撒渔网'''
    net = NetSprite(x=pos[0], y=pos[1])
    nets.append(net)

def release_coin(pos, score):
    '''释放金币'''
    coin = CoinSprite(x=pos[0], y=pos[1], score=score)
    coins.append(coin)

@game_win.event                                  
def on_mouse_press(x, y, button, modifiers):
    '''大炮射击'''
    if button == pyglet.window.mouse.LEFT:
        fire_bullet()

@game_win.event
def on_close():
    '''游戏窗口关闭'''
    player.next_source()
    
def music_control(dt):
    if not player.playing:
        player.queue(music)
        player.play()

if __name__ == '__main__':
    '''程序入口'''
    pyglet.clock.schedule_interval(fire_control, 1/60)
    pyglet.clock.schedule_interval(fishes_control, 1/60)
    player = pyglet.media.Player()
    pyglet.clock.schedule_interval(music_control, 1)
    pyglet.app.run()
