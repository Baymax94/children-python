# -*- coding: cp936 -*-
from math import sqrt
#第四章----素数的家族
#《c趣味编程》30-35题
#21:44 2007-1-11
def z30():
    #10000以内的素数是：
    print "10000以内的素数是："
    m= filter(isP,range(2,1000))
    print m,len(m)
def isP(x):
    if x==2 :return True
    if x%2==0 :return False
    for n in range(3,int(sqrt(x)+2),2):
        if x%n==0 :return False
    return True
def z31():
    #验证哥德巴赫猜想
    print "验证哥德巴赫猜想:"
    ss=[]
    t=filter(isP,range(2,1000))
    for i in range(6,1000,2):
        for j in t:
            if isP(i-j):
                s=str(i)+"="+str(j)+"+"+str(i-j)
                ss+=[s]
                break
    print ss
def hueiwen(x):
    t=""
    for i in reversed(str(x)):
        t+=i
    return int(t)
def z32():
    print "计算可逆素数"
    t=filter(lambda m: isP(m) and isP(hueiwen(m)),range(2,1000))
    print t
def z33():
    print "计算回文素数"
    t=filter(lambda m: isP(m) and hueiwen(m)==m,range(2,1000))
    print t
def z34():
    print "计算两素数差为1898"
    t=filter(lambda m: isP(m) and isP(m+1898),range(2,100))
    tt=[(m,m+1898)for m in t]
    print tt

def z35():
    '''问题：计算回文素数幻方.
回文素数幻方是一个4*4的数组，其中横线竖线和斜线10条线全部是 回文素数
这个程序首先得到第一，二，四行的数，然后通过 第一，二，四行的数
得到 第三行的数，然后判断 第三行的数和斜线三数是不是 回文素数，
所以程序非常快。
说明：如结果
1933
9133
1789
3391
横线四数1933，9133，1789，3391和
竖线四数1913，9773，3389，3391和
斜线二数1181，3373均是 回文素数
    '''
    def is1379(x):
        while(x):
            x,t=divmod(x,10)
            if t%2==0 or t==5:
                return False
        return True
    num=1
    t=filter(lambda m: isP(m) and isP(hueiwen(m)),range(1001,9999))
    g=lambda a,b,c,d:int(a/1000)*1000+int(b/100)%10*100+int(c/10)%10*10+d%10
    ns=lambda a,b,c,d:str(a)+str(b)+str(c)+str(d)
    sts=lambda s2:s2[12] + s2[8] + s2[4] + s2[0] + s2[13] + s2[9] + s2[5] +\
                s2[1] + s2[14] + s2[10] + s2[6] + s2[2] + s2[15] + s2[11] +\
                s2[7] + s2[3]
    sts1=lambda s2:s2[3] + s2[2] + s2[1] + s2[0] + s2[7] + s2[6] + s2[5] +\
                s2[4] + s2[11] + s2[10] + s2[9] + s2[8] + s2[15] + s2[14] +\
                s2[13] + s2[12]
    k=filter(is1379,t)
    rr={}
    for i in t:
        t3,t4=divmod(i,100)
        t1=t3*10+i%10
        t2=int(t4/10)
        if t1 in rr:
            rr[t1]+=[t2]
        else:
            rr[t1]=[t2]
    #print rr
    #print t
    se1=[]
    for i in k:
        for j in t:
            for m in k:
               m3=map(lambda x:  int(''.join(x)),zip(str(i),str(j),str(m)))
               #print m3
               if len(filter(lambda m: m in rr,m3))==4:
                   for m2 in rr[m3[0]]:
                       for i2 in rr[m3[1]]:
                           for j2 in rr[m3[2]]:
                               for k2 in rr[m3[3]]:
                                   hh=m2*1000+i2*100+j2*10+k2
                                   if hh in t and g(i,j,hh,m) in t and g(m,hh,j,i) in t:
                                       s2=ns(i,j,hh,m)
                                       if s2 not in se1:
                                           print num,s2
                                           # raw_input("按回车继续")
                                           num+=1
                                           s3 = sts(s2)
                                           s4 = sts1(s3)
                                           se1+=[s4,s3]
                                           s3 = sts(s3)
                                           s4 = sts1(s3)
                                           se1+=[s4,s3]
                                           s3 = sts(s3)
                                           s4 = sts1(s3)
                                           se1+=[s4,s3]
                                           s3 = sts(s3)
                                           s4 = sts1(s3)
                                           se1+=[s4,s3]
if __name__ == '__main__':
    s=""
    for i in range(30,36):
        s+='z'+str(i)+'()\n'
    exec(s)
  
