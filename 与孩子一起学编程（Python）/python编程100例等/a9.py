# -*- coding: cp936 -*-
from collections import deque
#第九章----数的变换
#《c趣味编程》69-77题
#21:49 2006-11-4
def z69():
    '''猜牌术（1）
魔术师,最上面一张是黑a，第2次从上到下数2张放在最
底下，然后翻开是黑k，然后再从上到下数3张放
在最底下，是黑q，第k次数k张，依次翻开，得
到黑a~1；问原始的牌序'''
    ss=13
    d = deque(range(1,ss+1))
    f=[1]*ss
    for i in range(ss):
        d.rotate(-(i%len(d)))
        f[d[0]-1]=i+1
        d.popleft()
    print f
def z70():
    '''猜牌术（2） 魔术师
最上面一张是黑a，然后从上到下数2张放在最底
下，然后翻开是黑k，然后再从上到下数2张放在
最底下，是黑q，依次翻开，得到黑a~1，红a~1
；问原始的牌序 '''
    def pai(x):
        if x>13:
            ch='r'
            x-=13
        else:
            ch='b'
        return ch+str(x)
    ss=26
    d = deque(range(1,ss+1))
    f=[1]*ss
    f[0]=pai(1)
    d.popleft()
    for i in range(2,ss+1):
        d.rotate(-(2%len(d)))
        f[d[0]-1]=pai(i)
        d.popleft()
    print f
def z71():
#11个人组成一个环，报数，每数到7，那个人就出来，问7次后剩下哪4个人
    ss=11
    nn=4
    kk=7
    d = deque(range(1,ss+1))
    for i in range(kk):
        d.rotate(-((nn-1)%len(d)))
        print d.popleft()
    print d
def z72():
#4个3和3个5可以组成几个不同的数分别是多少 
    e=[]
    for i in range(5):
        for j in range(4):
            e+=[i*3+j*5]
    print set(e)
def ntom(x,size,mod):
    t=[0]*(size)
    j=0
    while x and j<size:
        x,t[j]=divmod(x,mod)
        j+=1
    return t
def z73():
    #五个互相不相同的数和为23，其中若干个加起来可以表示1~23内的全部自然数，问他们是多少
    def h73(xx):
        t=[]
        n=5
        for nn in range(1,2**n):
            y=sum(map(lambda x,y:x*y,xx,ntom(nn,n,2)))
            t.append(y)
        return len(set(t))
    ss=23
    for i in range(ss):
        for j in range(i+1,ss):
            for m in range(j+1,ss):
                for n in range(m+1,ss):
                    kk=ss-i-j-m-n
                    if kk>n:
                        kt=[i,j,m,n,kk]
                        if h73(kt)==ss:
                            print kt
def z74():
    #重量四十的砝码被摔成四块，每块都是整数，并且用这四块可以测量1~40任意一个重量,问他们重多少
    def h74(xx):
        t=[]
        n=4
        for nn in range(1,3**n):
            y=sum(map(lambda x,y:x*y,xx,ntom(nn,n,3)))
            t.append(y)
        return len(set(t))
    ss=40
    for i in range(ss):
        for j in range(i+1,ss):
            for m in range(j+1,ss):
		kk=ss-i-j-m
                if kk>m:
		    kt=[i,j,m,kk]
		    if h74(kt)==ss:
			print kt
def z75():
    '''10个人围成一个环，分东西。他们一开始有{10,2,8,22,16,4,10,6,14,20}
个东西,所有的人如果是奇数个就再要一个，然后所有的人同时将自己的一半给他右边的人，
问几次后大家的东西的个数一样 '''
    d=deque([ 10, 2, 8, 22, 16, 4, 10, 6, 14, 20])
    print d
    while [d[0]]*10!=d:
        d=map(lambda x:x%2 and (x+1)/2 or x/2,d)
        d2=deque(d)
        d2.rotate(1)
        d=map(lambda x,y:x+y,d,d2)
        print d

def z76():
    #6个数中选择若干个数,其中他们的和最接近10,问怎么选{3.1,1.7,2.0,5.3,0.9,7.2}
    m2=[3.1,1.7,2.0,5.3,0.9,7.2]
    m2=[x*10 for x in m2]
    n=6
    t=[]
    for nn in range(1,2**n):
        tt=ntom(nn,n,2)
        y=abs(sum(map(lambda x,y:x*y,m2,tt))-100)
        t+=[[y,tt]]
    t=filter(lambda x,y=min(t)[0]:x[0]<y+0.01,t)
    for i in  t:
        m=filter(lambda x:x,map(lambda x,y:x and y or 0,i[1],m2))
        print m
def z77():
    #分水问题：某人有12升水，想平分他为2个6升，但是只有8升和5升的容器，为最少要倒几次才可以，怎么分
    def nexts(a,b,c,d):
        tt=[]
        ke1=reduce(lambda x,y:x+y,map(lambda x:str(x),a))
        for i in range(0,3):
            if a[i]!=0:
                for j in range(0,3):
                    if i!=j and a[j]<b[j]:
                        m=[]+a
                        t=b[j]-a[j]
                        if m[i]>=t:
                            m[i]-=t
                            m[j]=b[j]
                        else:
                            m[j]+=m[i]
                            m[i]=0
                        if m  not in c:
                            tt+=[m]
                            ke=reduce(lambda x,y:x+y,map(lambda x:str(x),m))
                            d[ke]=ke1
        return tt
    a=[12,0,0]
    b=[12,8,5]
    dd=[a,b]
    ee={}
    t=nexts (a,b,dd,ee)
    dd+=t
    while 1:
        m=[]
        for i in t:
            m+=nexts(i,b,dd,ee)
        dd+=t
        t=m
        if [6,6,0] in t :break
    e=ee["660"]
    print [6,6,0]
    while e!='1200':
        print map(lambda x:int(x),list(e))
        e=ee[e]
    print [12,0,0]
        # raw_input('--> ')
if __name__ == '__main__':
    s=""
    for i in range(69,78):
        s+='z'+str(i)+'()\n'
    exec(s)
