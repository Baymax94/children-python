# -*- coding: cp936 -*-
#第六章----分数趣题
#《c趣味编程》42-47题
#21:46 2006-11-4
def gcd(x,y):
    #最大公因子
    if x>y:x%=y
    while x:
        x,y=y%x,x
    return y
def lcm(x,y):
    #最小公倍数
    return x*y/gcd(x,y)
def jhua(x):
    t=gcd(x[0],x[1])
    return [x[0]/t,x[1]/t]
def z42():
    x,y=(120,36)
    print x,y,"的最小公倍数是",lcm(x,y)
    print x,y,"的最大公因子是",gcd(x,y)
def z43():
    #比较两个分数的大小
    def bijiao(x,y):
        x,y=jhua(x),jhua(y)
        m,n=x[0]*y[1],x[1]*y[0]
        if m>n:
            return '>'
        elif m<n:
            return '<'
        else:
            return '='
    x,y=[1235,2356],[1357,2468]
    print x,bijiao(x,y),y
def z44():
    #找出方程1/x+1/y+1/z+1/a=1的解
    def addf(x,y):
        x,y=jhua(x),jhua(y)
        return jhua([x[0]*y[1]+x[1]*y[0],y[1]*x[1]])
    ai=range(2,13)
    aii=range(2,43)
    num=1
    for i in ai:
        for j in ai:
            for m in ai:
                for k in aii:
                    if i<=j<=m<=k:
                        r=[i,j,m,k]
                        t=reduce(addf, map(lambda x:[1,x],r))
                        if t==[1,1]:
                            print num,r
                            num+=1 
def z45():
    def fena(x,y):
        #分子为1的分数叫做埃及分数把一个分数a/b分解成n个埃及分数的和
        sh,yu=divmod(x,y)
        re=[]
        if yu:
            t=sh+1
            re+=[t]
            y,x=y*t-x,x*t
            re+=fena(x,y)
        else:
            re+=[x/y]
        return re
    print fena(99,19)
def z46():
    #找出分子小于40，分母等于40的最简真分数,就是说分子和分母没有公因子的分数
    num=1
    for i in range(1,40):
        y=40
        if gcd(i,y)==1:
            print num,[i,y]
            num+=1
def z47():
    def divf(x,y):
        yu=[]
        sh=[]
        sh1,yu1=divmod(x,y)
        sh+=[str(sh1),'.']
        if yu1==0:return ''.join(sh[:-1])
        while yu1 :
            sh1,yu1=divmod(yu1*10,y)
            sh+=[str(sh1)]
            if yu1 not in yu:
                yu+=[yu1]
            else:
                t=yu.index(yu1)
                sh.insert(t+3,'(')
                sh.append(')')
                break
        return ''.join(sh)
    print divf(3737,27000)
    print divf(12,100)
    print divf(120,12)
if __name__ == '__main__':
    s=""
    for i in range(42,48):
        s+='z'+str(i)+'()\n'
    exec(s)
