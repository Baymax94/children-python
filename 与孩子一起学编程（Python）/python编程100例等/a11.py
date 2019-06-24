# -*- coding: cp936 -*-
#第十一章----智能游戏
#《c趣味编程》86-93题
#21:39 2007-1-23
from random import shuffle
class caigame:
    win=False
    flag=False
    life=12
    what=-1
    s1=''
    map1=[]
    thenum=0
    def start(self):
        t=range(1,10)
        shuffle(t)
        self.thenum=t[0]*1000+t[1]*100+t[2]*10+t[3]
        self.inmap()
        print self.thenum
        while self.life>0:
            self.GetResults()
        if self.win :
            print "你赢了"
        elif  self.flag:
            print "你退出了"
        else : print "你输了"
        return
    def GetResults(self):
        self.life-=1
        s1=raw_input('''输入你猜的那个数字
或者输入Q或者q退出
或者输入A或者a自动猜
''')
        if s1 in ['Q','q']:
            self.life=0
            self.flag=True
            return
        elif s1 in ['A','a']:
            s1= self.autodo()
        else:
            pass
        self.s1=s1
        w=self.getnum(s1)
        self.what=w
        print s1,":",w[0],"a",w[1],"b"
        if w[1]==4:
            self.life=0
            self.win=1
            return
        return
    def getnum(self,x,n1=-1):
        if n1==-1:n1=self.thenum
        n1=str(n1)
        a=len(filter(lambda m,n=n1:m in n,str(x)))
        b=len(filter(lambda m,n=n1,k=str(x):n.find(m)==k.find(m),str(x)))
        return [a,b]
    def inmap (self):
        r={}
        t=range(1,10)
        for i in t:
            for j in t:
                for m in t:
                    for n in t:
                        if i!=j!=m!=n!=i and j!=n and m!=i:
                            r[int(str(i)+str(j)+str(m)+str(n))]=1
        self.map1=r.keys()
        self.map1.sort()
        return
    def autodo(self):
        if self.what!=-1:
            self.map1=filter(lambda m,n=self.what,k=self.getnum ,ttt=self.s1:
                             n==k(ttt,m),self.map1)
        #if len(self.map1)<9 :print self.map1
        if self.map1[0]!=self.s1:
            return self.map1[0]
        else:
            return self.map1[-1]

def z86():
    #洗牌发牌
    t=[]
    def g(x):
        sh,yu=divmod(x,13)
        return [sh,yu]
    def g2(x,y):
        t=[]
        s1=["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        for i in x:
            if i[0]==y:
                t+=[i[1]]
        t.sort()
        t=map(lambda m,n=s1:n[m],t)
        return t
    s2=[u"黑桃", u"红桃", u"方片", u"草花"]
    s3=[u"北",u"南",u"西",u"东"]
    t=range(52)
    shuffle(t)
    t=map(g,t)
    t=t[:13],t[13:26],t[26:39],t[39:]
    m=range(4);
    for i in m:
        print s3[i]
        for j in m:
            print s2[j],g2(t[i],j)
    print
def z93():
    ''' ** 汉诺塔游戏 ** 
     这个游戏是为了移动一个塔 
     你输入一个小数,这个数只能是2~7 
     这个数代表塔的层数\n 
     在一个木板上有三根杆子\n最左边的杆子
        自上而下，由小到大串着n层的塔\n，游戏的目的是
        将最左边的杆子上的塔移动到最右\n边的杆子上，
        条件是一次只能移动一个盘，\n并且不允许大盘放在小盘上。;
     如果输入2~7以外的任何字符那么n=4\n '''
    def g(x,y):
        s4=x==1 and ' '*7 or '' 
        s3="-"* (abs(x-y)==2 and 12 or 5)
        s3= x>y and s3+">" or "<"+s3
        print s4+str(x)+s3+str(y)
        return
    def move(n,z,m,y):
        if n>0:
            move(n-1,z,y,m)
            g(z,m)
            move(n-1,y,m,z)
        return
    t=raw_input("输入那个塔的层数")
    t=int(t)
    if not 8>t>1:t=4
    move(t,0,2,1)
    return
def z91():
    '''**人机猜数游戏 ** 
 这个游戏是为了 猜数. 这个数字是四位数 
 你输入一个四位数,各位数只能是1~9 
 计算机告诉你这个四位数有几个数正确，以及有几个位置正确\n 
 比如如果那个数是1234，你猜的是2354\n那么计算机会回答3a1b 
 表示你这个四位数有3个数正确，以及有1个连位置也正确\n '''
    e=caigame()
    e.start()
def z87():
    #黑白子交换
    def nex(x):
        if '012' in x:return x.replace('012','210')
        if '120' in x:return x.replace('120','021')
        if '10' in x and '2102' not in x:return x.replace('10','01')
        if '02' in x and '1021' not in x:return x.replace('02','20')
        return
    n=4
    t,r='1'*n,'2'*n
    x=t+'0'+r
    s=r+'0'+t
    while x!=s:
        print x
        x=nex(x)
    print s
if __name__ == '__main__':
    z91()
    #z93()
