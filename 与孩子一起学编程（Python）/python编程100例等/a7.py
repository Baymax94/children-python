# -*- coding: cp936 -*-
#第七章----逻辑推理与判断
#《c趣味编程》48-57题
#21:47 2006-11-4
def ntom(x,size,mod):
    t=[0]*(size)
    j=0
    while x and j<size:
        x,t[j]=divmod(x,mod)
        j+=1
    return t
def permute(seq, index):
   seqc = seq[:]
   seqn = [seqc.pop()]
   divider = 2
   while seqc:
     index, new_index = divmod(index,divider)
     seqn.insert(new_index, seqc.pop())
     divider += 1
   return seqn
def z48():
    '''新郎与新娘已经知道条件矩阵,用消去法求解
    '''
    z=[[3,2,2],[2,2,2],[3,2,3]]
    t=juz(z)
    m=range(0,3)
    for i in m:
        for j in m:
            if t[i][j]==1:
                print chr(97+i),"和",chr(49+j),"结婚"
    return
def z49():
    ''' 六个人按照条件挑选去和留，条件是
a和b至少去一个人   a+b>1
a和d不能一起去   a+d!=2
a，e，f三人里要去两人  a+e+f==2
b和c都去  或者 都不去  (b+c==0 or b+c==2)
c和d两人中只去一个  c+d==1
如果d不去则e也不去    (d+e==0 or d==1)'''
    ss=["不去", "去"]
    n=6
    for i in range(0,2**n+1):
        a,b,c,d,e,f=ntom(i,n,2)
        if a+b>1 and a+d!=2 and a+e+f==2 and (b+c==0 or b+c==2)\
        and c+d==1 and (d+e==0 or d==1):
            t=[a,b,c,d,e,f]
    for i in range(0,n):
        print chr(97+i),ss[t[i]]
    return
def z50():
    '''谁在说谎
a说b在说谎(a and not b or not a and b)
b说c在说谎(b and not c or not b and c)
c说a和b都在说谎(c and a+b==0 or  not c and a+b!=0)
问他们谁在说真话谁在说谎'''
    ss=["说谎者", "诚实者"]
    n=3
    for i in range(0,2**n+1):
        a,b,c=ntom(i,n,2)
        if (a and not b or not a and b) and  (b and not c or not b and c)\
           and (c and a+b==0 or  not c and a+b!=0):
            t=[a,b,c]
    for i in range(0,n):
        print chr(97+i),ss[t[i]]
    return
def z51():
    '''四个被怀疑是小偷的人被抓了，知道他们中只有一个小偷 a+b+c+d=1
a说 b没有偷  是 d偷的b+d=1 ①
b说  b没有偷  是 c偷的b+c=1　②
c说 a 没有偷  是 b偷的a+b=1
已知 三人要么说真话要么说假话,问谁偷的'''
    #因为①-②得到d+c=0所以b=1，所以是b偷的
    print "b是小偷"
def z52():
    '''黑与蓝
五个人，帽子上贴着黑与蓝的标签。黑的说谎，蓝色的说真话，他们这样说：
a说他看见3个蓝的标签（不包括他自己）,如果他是真话那么有a=1 且b+c+d+e=3，如果他是
假话那么有!a=1且 b+c+d+e!=3，也就是 a&& b+c+d+e==3 || !a  && b+c+d+e!=3
b说有0个，c说有1个，d说有4个'''
    ss=["黑色", "蓝色"]
    n=5
    g=lambda w,ind,x:w[ind] and sum(w)-w[ind]==x or not w[ind] and\
          sum(w)-w[ind]!=x
    for i in range(0,2**n+1):
        t=ntom(i,n,2)
        if g(t,0,3) and g(t,1,0) and g(t,2,1) and g(t,3,4):
            tt=t
    for i in range(0,n):
        print chr(97+i),ss[tt[i]]
    return
def z53():
    #三人要么说谎要么说真话,a说有2个是说真话的,b和c都说 有1个说真话的
    ss=["说谎者", "诚实者"]
    n=3
    g=lambda w,ind,x:w[ind] and sum(w)==x or not w[ind] and sum(w)!=x
    for i in range(0,2**n+1):
        t=ntom(i,n,2)
        if g(t,0,2) and g(t,1,1) and g(t,2,1) :
            tt=t
    for i in range(0,n):
        print chr(97+i),ss[tt[i]]
    return
def z54():
    '''三个人，一个说谎0，一个说真话2，一个不确定1 ,a说  b是2，
    (a==2==b or a!=2!=b)b说 b是1，b!=2（因为如果b是2那么b会说b=2）c说b是0 ，
    (c==0!=b or c==2 and b==0 or c==1)'''
    ss=["说谎者", "两面派", "诚实者"]
    k=range(0,3)
    g=lambda m: reduce(lambda x,y:x*y, range(1, m+1))
    for i in range(1,g(3)):
        t=permute(k,i)
        a,b,c=t
        if (a==2==b or a!=2!=b) and b!=2 and (c==0!=b or c==2 and b==0 or c==1):
            tt=t
    for i in range(0,3):
        print chr(97+i),ss[tt[i]]
    return

def z55():
    #值班问题a=c+1;d=e+2;g=b+3;f=4;并且a~f和1~7是一对一的关系
    s11=["", "一", "二", "三", "四", "五", "六", "日"]
    k=range(1,8)
    k.remove(4)
    g=lambda m: reduce(lambda x,y:x*y, range(1, m+1))
    for i in range(1,g(6)):
        t=permute(k,i)
        a,b,c,d,e,g=t
        f=4
        if (a == c + 1) and (d == e+2) and (g == b + 3) and(c<f<b or  c>f>b):
            tt=[a,b,c,d,e,f,g]
    for i in range(0,7):
        print chr(97+i),s11[tt[i]]
    return
def z56():
    #区分国籍,已经知道条件矩阵,用消去法求解
    z=[[3,2,3,3,2,3],
[3,2,3,3,2,2],
[3,2,3,3,3,3],
[2,2,2,2,2,2],
[3,2,2,3,2,3],
[2,2,2,3,2,2]]
    ss=["美", "英", "法", "德", "意", "俄"]
    t=juz(z)
    m=range(0,6)
    for i in m:
        for j in m:
            if t[j][i]==1:
                print chr(97+i),"来自",ss[j]
def juz(z):
    n4=0
    while n4!=len(z):
        t=[]
        n4=0
        for ii in z:
            i=list(ii)
            n3=len(filter(lambda x:x==3,i))
            n1=len(filter(lambda x:x==1,i))
            if n3==len(z)-1:
                i=map(lambda x:x!=3 and 1 or x,i)
            if n1==1:
                n4+=1
                i=map(lambda x:x!=1 and 3 or x,i)
            t+=[i]
        z=t
        s1="zip("
        for j in range(0,len(z)):
            s1+="z["+str(j)+'],'
        s1=s1[:-1]+')'
        z=eval(s1)
        #print t,z
        # raw_input('ssss')
    return t
def z57():
    '''三家九个孩子比赛，第一名得9分，第k名得10-k分,总分为1+2+3+...+9=45,
    一家为15分，并且每一家没有两个或者三个孩子得到相连的名次，第一名是李 家的孩子9，
    第二名是王家的孩子 8问最后一名是谁家的孩子。
因为不相连，所以第三名是赵家的孩子7分。第四名6分只能是 "李","王"家的。
同时因为15-1-7=7所以最后一名不是赵家的孩子。
最后因为15-6-9=0所以 最后一名不是李家的孩子。'''
    print "最后一名是王家的孩子"
    return
if __name__ == '__main__':
    s=""
    for i in range(48,58):
        s+='z'+str(i)+'()\n'
    exec(s)
   
