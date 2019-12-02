'''
程序：模拟J-15战机，继承J-11战机
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
from j11fighter import J11Fighter
       
class J15Fighter(J11Fighter):
    '''模拟J-15战机，继承J-11战机'''
    def __init__(self, number, pilot):
        '''初始化时描述战机属性'''
        super().__init__(number, pilot)
        self.model = 'J-15'          #战机型号

    def take_off(self):
        '''让战机起飞，并输出战机相关信息'''
        self.cur_altitude = 10000
        print('%s驾驶一架编号为%s的%s战机从某航母起飞，并迅速爬升到%s米高空' %
              (self.pilot, self.number, self.model, self.cur_altitude))

if __name__ == '__main__':
    '''测试J-15战机类'''
    j15 = J15Fighter(2048, '李大宝')
    j15.take_off()
