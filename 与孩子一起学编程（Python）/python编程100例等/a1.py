# -*- coding: cp936 -*-
from math import acos,sqrt
#第一章----最简单的问题
#《c趣味编程》1-10题
#21:39 2006-11-4
def genfunc(n,k):
   head = """
def permute(seq0):
   result = [] """
   boiler = """
 for counter%i in seq%i:
   seq%i = seq%i[:]
   seq%i.remove(counter%i)"""
   for i in range(1,k+1):
     space = '  '*i
     head = head + boiler.replace('\n','\n'+space)%(i,i-1,i,i-1,i,i)
   temp = ','.join([ 'counter%i'%(x) for x in range(1,k+1) ] )
   head = head + '\n' + space + "   result.append(''.join([%s]))"%(temp)
   return head + '\n   return result\n'
def zz1(e,f):
    ss=[]
    for m in e:
        s1=" "*62
        k=f(m)
        s2=s1[:k]+"*"+s1[k+1:]
        k=62-k
        s3=s2[:k]+"*"+s2[k+1:]
        ss+=[s3]
    return ss

def z1():
    #绘制余弦曲线
    k=zz1(range(10,-11,-1),lambda m: int(acos(m/10.0)*10))
    for n in k:
        print n

def z2():
    #绘制余弦曲线和一条直线
    k=zz1(range(10,-11,-1),lambda m: int(acos(m/10.0)*10))
    def g(e,gg,f):
        ss=[]
        for m in e:
            s1=gg[m]
            k=f(m)
            if 0<k<len(s1):
                s2=s1[:k]+"#"+s1[k+1:]
            else :
                s2=s1
            ss+=[s2]
        return ss
    k=g(range(20),k,lambda m: int(4.5*(m-1)+3.1))
    for n in k:
        print n
        
def z3():
    #绘制圆
    k=zz1(range(10,-11,-1),lambda m: int(30-2.5*int(sqrt(100-m*m))))
    for n in k:
        print n
def z4():
    '''唱歌大奖比赛,去掉最高分和最低分得到平均分
    '''
    def g(n):
        x=max(n)
        nn=min(n)
        print "最高分",x
        print "最低分",nn
        print "平均分",(sum(n)-x-nn)/(len(n)-2)
        return
    m=[1,2,3,4,5,6,7]
    g (m)

def z5():
    #555555的最大的三位数约数是多少
    print max(filter(lambda x: 555555%x==0,range(100,999)))
def z6():
    #13的20次方的最后三位数是多少
    def zz6(x,y,z):
        xx=[x]*y
        return reduce(lambda x,y:x*y%z, xx)
    print zz6(13,20,1000)

def z7():
    #100 !的末尾有多少个0
    def g(n):
        k=0
        for m in range(1,n+1):
            if m%25==0 :
                k+=2
            elif m%5==0 :
                k+=1 
        return k
    print g(100)
def z8():
    #5个取3个的排列的总数以及方法
    functext = genfunc(9,3)
    print functext
    exec(functext)
    s=permute(list("12345"))
    print s,len(s)
def z9():
    #计算杨辉三角形
    g = lambda x,y: (y==1 or y==x+1) and 1 or g(x-1,y-1)+g(x-1,y)
    for m in range(1,13):
        print ' '*2*(13-m),
        for n in range(1,m+2):
            print  str(g(m,n)).center(4),
        print
def z10():
    #把10进制度变成2进制
    def g(n,k):
        d=n
        s=""
        while d!=0:
            d,f=divmod(d,k)
            s=str(f)+s
        return s
    print g(234,2)
if __name__ == '__main__':
    s=""
    for i in range(1,11):
        s+='z'+str(i)+'()\n'
    exec(s)
   
