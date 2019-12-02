'''
程序：模拟J-11战机
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
class J11Fighter():
    '''模拟J-11战机'''
    def __init__(self, number, pilot):
        '''初始化时描述战机属性'''
        self.number = number         #战机编号
        self.pilot = pilot           #飞行员姓名
        self.model = 'J-11'          #战机型号
        self.max_altitude = 18500    #最大飞行高度
        self.cur_altitude = 0        #当前飞行高度
        
    def take_off(self):
        '''让战机起飞，并输出战机信息'''
        self.cur_altitude = 10000
        print('%s驾驶编号为%s的%s战机从某空军机场起飞，并迅速爬升到%s米高空' %
              (self.pilot, self.number, self.model, self.cur_altitude))

    def launch_missile(self, target):
        '''向目标发射导弹'''
        print('%s战机在%s米高空遭遇%s敌机并向目标发射1枚导弹' %
              (self.model, self.cur_altitude, target))

    def climb_to(self, altitude):
        '''战机爬升到指定的飞行高度'''
        if 0 <= altitude <= self.max_altitude:
            self.cur_altitude = altitude
            print('战机爬升到%s米' % altitude)
        else:
            print('给定的高度值%s无效' % altitude)
            
if __name__ == '__main__':
    '''测试战机'''
    j11 = J11Fighter(1024, '王小明')
    print(j11.number, j11.pilot, j11.model)
    j11.take_off()
    j11.launch_missile('F-15')
