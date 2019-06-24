# -*- coding: cp936 -*-
#第十二章----其他趣味程序
#:《c趣味编程》94-100题
#21:51 2006-11-4
def z94():
    #斐波那契数列
    def filie(x):
        a,b,t=1,1,0
        if x==1 or x==2:return 1
        while t!=x-2:
            a,b,t=b,a+b,t+1
        return b
    for i in range(1,30):
        print filie(i)
def z95():
    #把三位数字转化成罗马数字
    def lm(x):
        fy=[["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
            ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XCC"],
            ["","I","II","III","IV","V","VI","VII","VIII","IX"]]
        e=reduce(lambda x,y:x+y,
                 map(lambda x,y:x[y],fy,map(lambda x:int(x),list(str(x)))))
        print e
    lm(863)
def z96():
    #7个选手的得分分别是{5,3,4,7,3,5,6}序号是1~7，规则是得分越高，名次越低
    #而相同的得分名次一样,输出名次是{3,1,2,5,1,3,4}
    z=[5, 3, 4, 7, 3, 5, 6]
    k=[0]*7
    max1=0
    minc=0
    b=map(lambda x:list(x),zip(range(1,8),z,k))
    b=sorted(b,cmp=lambda x,y: cmp(x[1], y[1]))
    for i in b:
        if i[1]>max1:
            max1=i[1]
            minc+=1
        i[2]=minc
    b=sorted(b)
    t=map(lambda x:x[2],b)
    print t
def z97():
    #满足一定条件的序列：如3，2，2，1四数,他们的和是8,并且3>=2>=2>=1;找出所有这样的序列
    n=18
    r=[1]*4
    num=1
    for r[1] in range(r[0],n-sum(r[:0])):
        for r[2] in range(r[1],n-sum(r[:1])):
            for r[3] in range(r[2],n-sum(r[:2])):
                t=n-sum(r)
                if t>=r[3]:
                    tt=r[1:]+[t]
                    print num,tt
                    num+=1
    return
def z97_b():
    exec(zz97(23,6))
    z97_a()
def zz97(n,k):
    s='def z97_a():\n'
    tb='  '
    s+=tb+'n='+str(n+1)+'\n'
    s+=tb+'r=[1]*'+str(k)+'\n'
    g=lambda x:tb*(x)+'for r['+str(x)+'] in range(r['+str(x-1)+\
       '],n-sum(r[:'+str(x-1)+'])):\n'
    for i in range(1,k):
        s+=g(i)
    e=tb*(k+1)
    s+=e+'t=n-sum(r)\n'+e+'if t>=r['+str(k-1)+']:\n'
    e+=tb
    s+=e+'tt=r[1:]+[t]\n'+e+'print tt'
    print s
    return s
def remo(x1,y):
    mt=[]
    for now in range(1,y+1):
        t=True
        for x in range(len(x1)):
            m=x-len(x1)
            if  now==x1[x] or now==x1[x]+m or now==x1[x]-m:
                t=False
        if t:
            mt+=[now]
    return mt
def z98_4():
    # 四皇后问题 ,就是把四个国际象棋里的皇后放到棋盘里问怎么放不互相吃
    n=4
    k=[1]*n
    num=1
    for k[0] in remo(k[:0],n):
        for k[1] in remo(k[:1],n):
            for k[2] in remo(k[:2],n):
                for k[3] in remo(k[:3],n):
                    print num,k
                    num+=1
def zz98(n):
    s='def z98_a():\n'
    tb='  '
    s+=tb+'n='+str(n)+'\n'
    s+=tb+'k=[1]*n\n'
    s+=tb+'num=1\n'
    g=lambda x:tb*(x+1)+'for k['+str(x)+'] in remo(k[:'+str(x)+'],n):\n'
    for i in range(0,n):
        s+=g(i)
    e=tb*(n+1)
    s+=e+'print num,k\n'
    s+=e+'num+=1\n'
    print s
    return s
def z98():
    # 八皇后问题 ,就是把八个国际象棋里的皇后放到棋盘里问怎么放不互相吃
    exec(zz98(8))
    z98_a()
def z99():
    #超长正整数的加法
    a=122414354367l
    b=23157465721578l
    print a,"+",b,"=",a+b
class qi:
    num0=1
    st='1'
    def __init__(self, str1=None):
        self.st=str1
        self.num0=str1.find('0')
        return
    def show(self):
        st=list(self.st)
        e=st[:]
        e[7],e[8],e[5],e[4],e[3]=st[5],st[4],st[3],st[8],st[7]
        m=0
        for i in e:
            m+=1
            print i,
            if m%3==0:print
        return
    def move(self,x):
        st=list(self.st)
        if st[x]!='1':
            st[x],st[self.num0]=st[self.num0],st[x]
        return ''.join(st)
    
def z100():
    '''数字移动 ::在图上的九个点上，空出中间的点，其余的
    点上任意填上1~8   8个数字，然后移动除了一之外其余的
    数字，使1到8顺时针从小到大排列，规则是，只能将数字
    沿线移动到空白的位置。'''
    def nexts(d,e):
        tt=[]
        def add (a,b,t=tt,ee=e):
            if a not in ee:
                ee[a]=b
                t+=[a]
            return
        for i in d:
            x=qi(i)
            if (x.num0==8):
                for j in range(0,8):
                    add(x.move(j),i)
            else:
                t=x.num0
                add(x.move((t+1)%8),i)
                add(x.move((t+7)%8),i)
                add(x.move(8),i)
        return tt
    s1 = "856321740"
    s3 = "12345678"
    i = len(s3)-s1.find("1")
    s3=s3[i:]+s3[:i]+'0'
    a=qi(s1)
    dd=[s1]
    ee={s1:'0'}
    while s3 not in ee:
        dd=nexts (dd,ee)
    e=ee[s3]
    num=1
    qi(s3).show()
    num=1
    print num
    num+=1
    while e!='0':
        qi(e).show()
        print num
        num+=1
        e=ee[e]
    return
if __name__ == '__main__':
    s=""
    for i in range(94,101):
        s+='z'+str(i)+'()\n'
    exec(s)
