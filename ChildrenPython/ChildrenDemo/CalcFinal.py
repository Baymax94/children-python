import tkinter #导入tkinter模块
import re

root  = tkinter.Tk()
root.minsize(280,500)


#1.界面布局
#显示面板
result = tkinter.StringVar()
result.set(0)                           #显示面板显示结果1，用于显示默认数字0
result2 = tkinter.StringVar()           #显示面板显示结果2，用于显示计算过程
result2.set('')
#显示版
label = tkinter.Label(root,font = ('微软雅黑',20),bg = '#EEE9E9',bd ='9',fg = '#828282',anchor = 'se',textvariable = result2)
label.place(width = 280,height = 170)
label2 = tkinter.Label(root,font = ('微软雅黑',30),bg = '#EEE9E9',bd ='9',fg = 'black',anchor = 'se',textvariable = result)
label2.place(y = 170,width = 280,height = 60)




#数字键按钮

btn7 = tkinter.Button(root,text = '7',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : press('7'))
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
    global lists   
    a=''                  #全局化lists和按钮状态isPressSign
    oldnum = result.get()            
    if oldnum =='0':                 
        result.set(num)
    else:                            
        newnum = oldnum + num
        result.set(newnum)    
    if num =='AC':                #如果按下的是'AC'按键，则清空列表内容，讲屏幕上的数字键设置为默认数字0
        lists.clear()
        result.set(0)
    if num =='b':                 #如果按下的是退格‘’，则选取当前数字第一位到倒数第二位
        a = oldnum[0:-1]
        if(a==''):                #退到空值是为0
            a='0'
        result.set(a)
    if num=='%':
        if len(oldnum)==1:
            a=round(float(oldnum)*0.01,2)
        else:
            orgNume=oldnum[::-1]
            isfind=False
            for i in range(len(orgNume)):
                if isfind==True:
                    break
                else:
                    a=orgNume[i]
                    if is_operate(a):
                        a=orgNume[0:i]
                        c=a[::-1]
                        b=float(c)*0.01
                        index=len(oldnum)-i
                        a=oldnum[0:index]+str(b)
                        isfind=True  
            if isfind==False:
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
    formula_list=formula_formate(computrStr)
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
            result=0.0
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
    formula_list=[i for i in re.split('(\-\d+\.?\d*)',formula) if i]
    final_formula=[]
    for item in formula_list:
        if len(final_formula)==0 and re.search('^\-\d+\.?\d*$',item):
            final_formula.append(item)
            continue
        
        if len(final_formula)>0:
            if re.search('[\+\-\*\/\(]$',final_formula[-1]):
                final_formula.append(item)
                continue
        item_split=[i for i in re.split('([\+\-\*\/\(\)])',item) if i]
        final_formula+=item_split
    return final_formula

def desicion(tail_op,now_op):
    rate1=['+','-']
    rate2=['*','/']
    rate3=['(']
    rate4=[')']
    if tail_op in rate1:
        if now_op in rate2 or now_op in rate3:
            return -1
        else:
            return 1
    elif tail_op in rate2: 
        if now_op in rate3:
            return -1
        else:
            return 1
    elif tail_op in rate3:
        if now_op in rate4:
            return 0
        else :
            return -1
    else:
        return -1

def final_calc(formula_list):
    num_stack=[]
    op_stack=[]
    for e in formula_list:
        operator=is_operate(e)
        if not operator:
            num_stack.append(float(e))
        else:
            while True:
                if len(op_stack)==0:
                    op_stack.append(e)
                    break
                tag=desicion(op_stack[-1],e)
                if tag==-1:
                    op_stack.append(e)
                    break
                elif tag==0:
                    op_stack.pop()
                    break
                elif tag==1:
                    op=op_stack.pop()
                    num2=num_stack.pop()
                    num1=num_stack.pop()
                    num_stack.append(calculate(num1,num2,op))

    while len(op_stack)!=0:
        op=op_stack.pop()
        num2=num_stack.pop()
        num1=num_stack.pop()
        num_stack.append(calculate(num1,num2,op))   
    return num_stack,op_stack    
        
        




root.mainloop()