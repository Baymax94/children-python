'''
程序：模拟J-15战机，继承J-11战机，模拟战机雷达系统
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
from j11fighter import J11Fighter
import random

class Radar():
    '''模拟战机雷达系统'''
    def is_locked(self):
        '''判断目标是否被雷达锁定'''
        if random.randint(1, 10) < 6:
            return True
        else:
            return False
        
class J15Fighter(J11Fighter):
    '''模拟J-15战机，继承J-11战机'''
    def __init__(self, number, pilot):
        '''初始化时描述战机属性'''
        super().__init__(number, pilot)
        self.model = 'J-15'          #战机型号
        self.radar = Radar()         #将雷达类的实例作为属性

    def take_off(self):
        '''让战机起飞，并输出战机相关信息'''
        self.cur_altitude = 10000
        print('%s驾驶一架编号为%s的%s战机从某航母起飞，并迅速爬升到%s米高空' %
              (self.pilot, self.number, self.model, self.cur_altitude))

    def launch_missile(self, target):
        '''向目标发射导弹'''
        print('%s战机在%s米高空遭遇%s敌机，' %
              (self.model, self.cur_altitude, target), end='')
        if self.radar.is_locked():
            print('雷达锁定目标，并发射一枚导弹')
        else:
            print('雷达无法锁定目标，不能发射导弹')
            
if __name__ == '__main__':
    '''测试战机雷达'''
    j15 = J15Fighter(2048, '李大宝')
    j15.take_off()
    j15.climb_to(15000)
    j15.launch_missile('F-15')
