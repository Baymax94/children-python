# -*- coding: cp936 -*-
from math import sqrt
import random
#第十章----定理与猜想
#《c趣味编程》78-85题
#21:50 2006-11-4
def daoxu(n):
   d=n
   s=0
   while d!=0:
      d,f=divmod(d,10)
      s=f+s*10
   return s
def z85():
    #任意取一个十进制数如123，然后他和他的回文数321相加，得到新整数后重复以上步骤，最后
    #可以得到一个回文数444
    s1=179233126
    s2=0
    while s2!=s1:
        s1=s1+s2
        s2=daoxu(s1)
        print s2
    return
def z81():
    '''角谷猜想是任何一个数如果是偶数就除以2如果是奇数就乘以3再加1，最后会导致1，4，2，循环'''
    x=123347
    while x!=1:
        x= x%2==0 and x/2 or (x*3+1)/2
        print x
def fangf(x):
    t=int(sqrt(x))
    if t*t==x: return [t]
    t=int(sqrt(x-1))+1
    m=range(t)
    for i in m:
        for j in m:
            for k in range(j,t):
                for p in range(k,t):
                    if i *i + j * j + k * k + p * p == x:
                        if i==0 and j==0:return[k,p]
                        if i==0 and j!=0:return[j,k,p]
                        return [i,j,k,p]
def z82():
    #所有自然数最多可以用四个自然数的平方表示，验证这个定理
    for i in range(2,100):
        print i,fangf(i)
def z83():
    # 任意一个四位数，如1324，可以得到数1234和4321，然后4321-1234得到新数，重复以上步骤，
    #最后得到6174。而7641-1467=6174
    def six(x):
        t=1
        e=list(str(x))
        e.sort()
        e=''.join(e)
        n=int(e)
        if n<1000:t=10
        return daoxu(n)*t-n
    i=1999
    print i
    while i!=6174:
        i=six(i)
        print i
def z84():
    '''证明任何一个数a的立方等于一串连续奇数的和，其中首项为(a*(a-1)+1),公差为2，共a项
    他们的和是((a*(a-1)+1)*a+(2*a-2)*a/2=(a^3-a^2+a)+(a^2-a)=a^3
'''
    print "任何一个数a的立方等于一串连续奇数的和"
    return
def z80():
    '''很容易证明的定理大于1000的奇数x有x*x-1是8的倍数
    [1,3,5,7]=[1,1,1,1]
'''
    t=[i*i%8 for i in range(1,8,2)]
    print t
    print "大于1000的奇数x有x*x-1是8的倍数"
    return
def z78():
    #用正多边形逼近的方法计算pi
    x1=100000
    b,i=0.5,6
    while i<x1:
        b=sqrt(2-2*sqrt(1-b*b))/2
        i*=2
    print b*i
def z79():
    '''随机法计算pi：
本程序并不使用计算pi值的算法，它只是一个概
率模拟，即在边长为100的正方形内随机产生多
个点，将点以圆弧为界分开统计，由于点的个数
很多，直至几乎布满整个区域。此时，点的个数
就可以看作就是它所在区域的面积。可以得到如
下推导:

(1)蓝色区内点个数:总个数≈蓝色面积:总面积

(2)蓝色区内点个数:总个数≈圆面积/4:总面积

(3)蓝色区内点个数:总个数≈π×200×200/4:200×200

(4)π≈ 4×蓝色区内点个数/总个数

　　当然，点的位置会重复，所以结果与π值是
有差别的，不过，当点足够多时，可以看到一个
非常接近的结果。'''
    x,y,z=0,100000,0
    g=random.random
    while x<y:
        a=g()
        b=g()
        if a*a+b*b<1:
            z+=1
        x+=1
    print 4.0*z/y
if __name__ == '__main__':
    s=""
    for i in range(78,86):
        s+='z'+str(i)+'()\n'
    exec(s)
   
