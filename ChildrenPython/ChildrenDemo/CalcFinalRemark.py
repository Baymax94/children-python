import tkinter #导入tkinter模块
import re #导入正则模块

root  = tkinter.Tk() #创建窗体两种方法
'''
from tkinter import *
root=Tk()
'''
root.minsize(280,500)



#1.界面布局
#显示面板
'''
tk库的可变类型，与textvariable组合运用，用于控件动态值绑定，可变类型用get.set进行取值赋值用，
int IntVar
string StringVar
bool BooleanVar
double  DoubleVar
'''
result = tkinter.StringVar()
result.set(0)                           #显示面板显示结果1，用于显示默认数字0
result2 = tkinter.StringVar()           #显示面板显示结果2，用于显示计算过程
result2.set('')
#显示版
'''
15个核心控件
Button 按钮，Canvas绘图组件，Checkbutton复选框，Entry（单行），Text（多行）文本框，Frame框架，Label标签
Listbox 列表框，Menu菜单，Menubutton 菜单按钮，Message 消息框，Radiobutton 单选按钮，Scale  进度条，Scrollbar  滚动条，Toplevel  顶级，类似框架,但提供一个独立的窗口容器。
'''
label = tkinter.Label(root,font = ('微软雅黑',20),bg = '#EEE9E9',bd ='9',fg = '#828282',anchor = 'se',textvariable = result2)
#bg背景bd边框宽度fg前景色anchor对齐方式，左对齐w,右对齐e,顶对齐n,底对齐s
label.place(width = 280,height = 170)
label2 = tkinter.Label(root,font = ('微软雅黑',30),bg = '#EEE9E9',bd ='9',fg = 'black',anchor = 'se',textvariable = result)
label2.place(y = 170,width = 280,height = 60)
#放置位置y纵坐标值




#数字键按钮

btn7 = tkinter.Button(root,text = '7',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : press('7'))
#command 绑定方法，用到匿名函数lambda.无参数可用两种方式绑定command=press，有参数则 command=lambda : press()
btn7.place(x = 0,y = 285,width = 70,height = 55)
btn8 = tkinter.Button(root,text = '8',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : press('8'))
btn8.place(x = 70,y = 285,width = 70,height = 55)
btn9 = tkinter.Button(root,text = '9',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : press('9'))
btn9.place(x = 140,y = 285,width = 70,height = 55)

btn4 = tkinter.Button(root,text = '4',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : press('4'))
btn4.place(x = 0,y = 340,width = 70,height = 55)
btn5 = tkinter.Button(root,text = '5',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : press('5'))
btn5.place(x = 70,y = 340,width = 70,height = 55)
btn6 = tkinter.Button(root,text = '6',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : press('6'))
btn6.place(x = 140,y = 340,width = 70,height = 55)

btn1 = tkinter.Button(root,text = '1',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : press('1'))
btn1.place(x = 0,y = 395,width = 70,height = 55)
btn2 = tkinter.Button(root,text = '2',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : press('2'))
btn2.place(x = 70,y = 395,width = 70,height = 55)
btn3 = tkinter.Button(root,text = '3',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : press('3'))
btn3.place(x = 140,y = 395,width = 70,height = 55)
btn0 = tkinter.Button(root,text = '0',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : press('0'))
btn0.place(x = 70,y = 450,width = 70,height = 55)


#运算符号按钮
btnac = tkinter.Button(root,text = 'AC',bd = 0.5,font = ('黑体',20),fg = 'orange',command = lambda :press('AC'))
btnac.place(x = 0,y = 230,width = 70,height = 55)
btnback = tkinter.Button(root,text = '←',font = ('微软雅黑',20),fg = '#4F4F4F',bd = 0.5,command = lambda:press('b'))
btnback.place(x = 70,y = 230,width = 70,height = 55)
btndivi = tkinter.Button(root,text = '÷',font = ('微软雅黑',20),fg = '#4F4F4F',bd = 0.5,command = lambda:press('/'))
btndivi.place(x = 140,y = 230,width = 70,height = 55)
btnmul = tkinter.Button(root,text ='×',font = ('微软雅黑',20),fg = "#4F4F4F",bd = 0.5,command = lambda:press('*'))
btnmul.place(x = 210,y = 230,width = 70,height = 55)
btnsub = tkinter.Button(root,text = '-',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:press('-'))
btnsub.place(x = 210,y = 285,width = 70,height = 55)
btnadd = tkinter.Button(root,text = '+',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:press('+'))
btnadd.place(x = 210,y = 340,width = 70,height = 55)
btnequ = tkinter.Button(root,text = '=',bg = 'orange',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda :pressEqual())
btnequ.place(x = 210,y = 395,width = 70,height = 110)
btnper = tkinter.Button(root,text = '%',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:press('%'))
btnper.place(x = 0,y = 450,width = 70,height = 55)
btnpoint = tkinter.Button(root,text = '.',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:press('.'))
btnpoint.place(x = 140,y = 450,width = 70,height = 55)




#操作函数
lists = []                            #设置一个变量 保存运算数字和符号的列表
isPressSign = False                  #添加一个判断是否按下运算符号的标志,假设默认没有按下按钮
isPressNum = False

def press(num):
    global lists   #设置lists为全局变量。
    a=''            #设置需要填充的结果变量     
    oldnum = result.get()     #取得当前结果       
    if oldnum =='0':                 
        result.set(num)
    else:                            
        newnum = oldnum + num   #字符串拼接
        result.set(newnum)      #没有按=时，显示为过程
    if num =='AC':                #如果按下的是'AC'按键，则清空列表内容，讲屏幕上的数字键设置为默认数字0
        lists.clear()
        result.set(0)
    if num =='b':                 #如果按下的是退格‘’，则选取当前数字第一位到倒数第二位
        a = oldnum[0:-1]          #python字符串切片
        if(a==''):                #只有单数字时，退到空值是为0，其他取开始到前一位值
            a='0'
        result.set(a)
    if num=='%':                   
        if len(oldnum)==1:                  #一位数字时，百分数后的值，并保留两位。
            a=round(float(oldnum)*0.01,2)
        else:                               #为了遍历速度快，倒序先查到第一个操作数。（定位到最后一个操作数的值），取到百分号前的值。
            orgNume=oldnum[::-1]
            isfind=False
            for i in range(len(orgNume)):
                if isfind==True:
                    break
                else:
                    a=orgNume[i]
                    if is_operate(a):   #判断是否为操作位，取操作位前的值。然后反转。取当真实的%比前的数字。
                        a=orgNume[0:i]  
                        c=a[::-1]
                        b=float(c)*0.01
                        index=len(oldnum)-i  #根据%前的值的位数。定位开始字符串到最后一个操作符之间的值。
                        a=oldnum[0:index]+str(b) #组合成应该的数值。
                        isfind=True  
            if isfind==False:       #多位数字时，则直接得到值。
                a=round(float(oldnum)*0.01,2)   
        result.set(a)

    if num=='.':    
       if oldnum=='0':
           a='0.'
           result.set(a)

#获取运算结果函数
def pressEqual():
    global lists
    curnum = result.get()           #设置当前数字变量，并获取添加到列表
    lists.append(curnum)
    computrStr = ''.join(lists)     #讲列表内容用join命令将字符串链接起来
    #computrStr="1+1*2+(1+1)"
    computrStr="-6+5+-3"
    formula_list=formula_formate(computrStr) #表达式。
    result1,_=final_calc(formula_list)
    endNum=round(result1[0],2)
    result.set(endNum)                   #讲运算结果显示到屏幕1
    result2.set(computrStr)         #将运算过程显示到屏幕2
    lists.clear()                   #清空列表内容

def calculate(n1,n2,operator):
    result=0
    if operator=="+":
        result=n1+n2
    if operator=="-":
        result=n1-n2
    if operator=="*":
        result=n1*n2
    if operator=="/":
        if n2==0.0:
            result=0.0 #除数为0，默认值为0
        else:
            result=n1/n2
    return result

#判断是否为操作符
def is_operate(e):
    opers=['+','-','*','/','(',')']
    if e in opers:
        return True
    else:
        return False 

#判断是否为负数还是操作符
def formula_formate(formula):
    #去掉空格
    formula=re.sub(' ','',formula)
    #以横杠数字为分割
    #\-表示匹配横杠开头，\d+ 表示匹配数字一次或者多次，\.?批配小数点0或才1次,\d*批配数字0次或者多次
    formula_list=[i for i in re.split('(\-\d+\.?\d*)',formula) if i]
    final_formula=[]
    for item in formula_list:
        #第一个数字是以横杠开头的数字包括小数，
        if len(final_formula)==0 and re.search('^\-\d+\.?\d*$',item):
            final_formula.append(item)
            continue
        
        if len(final_formula)>0:
            #如果final_formula最后一个元素是运算符[+-*/(],则横杠数字不是减号
            if re.search('[\+\-\*\/\(]$',final_formula[-1]):
                final_formula.append(item)
                continue
        #按照运算符分割开
        item_split=[i for i in re.split('([\+\-\*\/\(\)])',item) if i]
        final_formula+=item_split
    return final_formula

def desicion(tail_op,now_op): #栈先进后出，后进先出
    #tal_op:运算符栈的最后一个运算符
    #now_op:从算式列表取出当前运算符
    #return: 1代表弹栈运算，0代表弹运算符栈最后一个元素，-1 入栈
    rate1=['+','-']
    rate2=['*','/']
    rate3=['(']
    rate4=[')']
    if tail_op in rate1:
        if now_op in rate2 or now_op in rate3:
            #说明两个运算优先不一样，需要入栈
            return -1
        else:
            return 1
    elif tail_op in rate2: 
        if now_op in rate3:
            return -1  #有（入栈
        else:
            return 1  #运算
    elif tail_op in rate3:
        if now_op in rate4:
            return 0 #（ 遇到 ）需要弹出（ 丢掉 ）
        else :
            return -1 #只要栈顶元素为（，当前元素不是）都应入栈
    else:
        return -1

def final_calc(formula_list):
    num_stack=[] #数字栈
    op_stack=[]  #运算符栈
    for e in formula_list:
        operator=is_operate(e)
        if not operator:
            num_stack.append(float(e)) #入数字栈，字符转换浮点
        else:
            while True:  #当前同一符号多次循环直到操作符栈添加最后1个符号跳出循环
                if len(op_stack)==0:  
                    op_stack.append(e)  #运算符栈无值自动入栈
                    break
                tag=desicion(op_stack[-1],e) #判断是否入栈，运算
                if tag==-1:
                    op_stack.append(e) #入栈后等待运算
                    break
                elif tag==0:
                    op_stack.pop() #把（弹出
                    break
                elif tag==1:
                    op=op_stack.pop() #弹出计算
                    num2=num_stack.pop()
                    num1=num_stack.pop()
                    num_stack.append(calculate(num1,num2,op))

    while len(op_stack)!=0:
        op=op_stack.pop()
        num2=num_stack.pop()
        num1=num_stack.pop()
        num_stack.append(calculate(num1,num2,op))   
    return num_stack,op_stack    
        
#进入消息循环
root.mainloop()