# -*- coding: cp936 -*-
from math import sqrt
from datetime import date
#第二章----生活中的数学
#《c趣味编程》11-17题
#21:42 2006-11-4
def z11():
    
    #某人是1999年9月29日生日
    #问到2006年9月29日他活了多少天
    a=date(1999,9,29)
    b=date(2006,9,29)
    c=str(b-a).split(" ")
    print int(c[0])
    return int(c[0])

def z12():
    #四位数前两位相同，后两位也相同，并且是个自然数的平方,问他 是多少
    t=range(1,10)
    for i in t :
        for j in t:
           m=i*1100+j*11
           n=int(sqrt(m))
           if m==n*n and i!=j :
               print m
def z13():
    #银行月息0.63%，一 人打算今后五年每年年底取1000，正好取完，问第一年应该存多少
    tl=0
    for i in range(5):
        tl=(tl+1000.0)/(1+0.0063*12)
    print tl
def z14():
    '''整存整取存钱的利率1，2，3，5，8年的利率分别是
    0.63%,0.66%,0.69%,0.75%,0.84%存20年钱问怎样存    利最大'''
    l1=[8,5,3,2,1]
    l2=[0.0084,0.0075,0.0069,0.0066,0.0063]
    nn=20
    maxx=0
    l3=map(lambda x,y:  1+12*x*y, l1,l2)
    for i in range(nn/l1[0]+1):
        for j in range(nn/l1[1]+1):
            for a in range(nn/l1[2]+1):
                for b in range(nn/l1[3]+1):
                    t=nn-i*l1[0]-j*l1[1]-a*l1[2]-b*l1[3]
                    if t>=0 :
                        kk=[i,j,a,b,t]
                        kt=reduce(lambda x, y: x*y, map(lambda x,y:  x**y,l3,kk))
                        if kt>maxx :
                            maxx=kt
                            kkk=kk 
    print kkk,2000*maxx
def z15():
    '''五人捕鱼,a先将鱼分为5份，把多余的一条扔了，拿走自己
的一份，bcde同样这样拿，问鱼最少多少条 '''
    n=1
    nn=5
    flag=0
    while flag==0 :
        n+=5
        s=n
        for i in range(5):
            s,y=divmod(s-1,5)
            if y==0:
                s*=4
                flag=1
            else :
                flag=0
                break
    print n
def z16():
    '''卖鱼，第一次卖了1/2加1/2条
            第2次卖了1/3加1/3条
            第3次卖了1/4加1/4条
            第4次卖了1/5加1/5条
            余下11条
            问一开始是多少条'''
    n=23
    nn=5
    flag=0
    while flag==0 :
        n+=2
        ss=n
        for i in range(1,5):
            s,y=divmod(ss+1,(i+1))
            if y==0:
                ss-=s
                flag=1
            else :
                flag=0
                break
    print n
def z17():
    #21筐鱼，7筐满，7筐半，7筐空，在不倒出鱼的情况下，怎样平分为3份
    k=[]
    for i in range(1,4):
        k+=[[i,7-i*2,i]]
    #print k
    for i in k:
        for j in k:
            for m in k:
                l3=map(lambda x,y,z:x+y+z, i,j,m)
                if i<=j<=m and l3[0]==7 and l3[1]==7:
                    print [i,j,m]
                    
if __name__ == '__main__':
    s=""
    for i in range(11,18):
        s+='z'+str(i)+'()\n'
    exec(s)
    
