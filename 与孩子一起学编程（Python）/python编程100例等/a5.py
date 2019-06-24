# -*- coding: cp936 -*-
#第五章----不定方程的解
#《c趣味编程》36-41题
#21:45 2006-11-4
def z36():
    '''解不定方程
x+y+z=100
5*x+3*y+z/3=100
x,y,z都是整数并且大于0'''
    #方程可以化简成7*x+4*y=100
    for i in range(1,25):
        t1=(100-4*i)
        t=int(t1/7)
        if t*7==t1:
            print [t,i,100-t-i]
    return
def findx(r2,r1):
    #找到x令 x*r2%r1=1
    y=r1
    if r2%r1==1:return 1
    q2,r1=divmod(r1,r2)
    q3,r2=divmod(r2,r1)
    q3=q3*q2+1
    t=False
    while  r1!=1:
        if r2==1 :r1-=1
        q1,r3=divmod(r1,r2)
        t,q2,q3,r1,r2=not t,q3,q1*q3+q2,r2,r3
    if t:q3=y-q3
    return q3
def get23(a,b):
    m=reduce(lambda x, y: x*y, a)
    t=map(lambda x,y=m: m/x, a)
    k=sum(map(lambda x,y,z:findx(x,y)*x*z,t,a,b))
    return k%m
def z37():
    '''解同余方程
x=1(mod 2)
x=2(mod 3)
x=4(mod 5)
x=0(mod 7)'''
    a,b=[2,3,5,7],[1,2,4,0]
    print get23(a,b)
def z38():
    #解方程x*5+y*2+z=100
    num=1
    for i in range(0,100,5):
        for j in range(0,100,2):
            for m in range(0,100):
                if i+j+m==100:
                    #print num,[i/5,j/2,m]
                    num+=1
    return
def z39():
    #四数成等差数列,并且他们的和是26,积是880,输出有二十项的上面的等差数列
    for i in range(1,4):
        j=26-6*i
        j,yu=divmod(j,4)
        if yu==0 and j *(j + i)*(j + 2 * i)*(j + 3 * i) == 880:
            print "等差数列的首项和公差分别是：",i,j
            print "等差数列的前二十项是：",[j + n * i for n in range(0,20)]
    return
def z40():
    #口袋里有12个东西,其中3红，3黑，6绿,任取八个有多少不同的颜色搭配
    num=1
    i=range(0,4)
    for j in i:
        for m in i:
            n=8-j-m
            if n<=6:
                print num,[j,m,n]
                num+=1
    return
def z41():
    '''解方程
x+y+z=30
3*x+2*y+z=50'''
    #方程可以化简成2*x+y=20
    for i in range(0,11):
        t1=(20-2*i)
        print [i,t1,30-t1-i]
    return
if __name__ == '__main__':
    s=""
    for i in range(36,42):
        s+='z'+str(i)+'()\n'
    exec(s)
   
