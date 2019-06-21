from tkinter import*
import random
import time
class Paint:
    def __init__(self):
        self.tk=Tk()
    def hello(self,str):
            print("hello world!"+str)
    def input(self,str):
        bth=Button(self.tk,text="click me",command=lambda :self.hello(str)) #没参数情况下command=self.hello
        bth.pack()
        self.tk.mainloop()
    def createLine(self):
        canvas=Canvas(self.tk,width=500,height=500)
        canvas.pack()
        canvas.create_line(0,0,500,500)
        self.tk.mainloop()
    def createBox(self):
        canvas=Canvas(self.tk,width=400,height=400)
        canvas.pack()
        #canvas.create_rectangle(10,10,50,50)
        canvas.create_rectangle(10,10,300,50)
        self.tk.mainloop()
    def random_rectangle(self,canvas,width,height,fill_color):
        x1=random.randrange(width)
        y1=random.randrange(height)
        x2=x1+random.randrange(width)
        y2=y1+random.randrange(height)
        canvas.create_rectangle(x1,y1,x2,y2,outline=fill_color,width=1)
    def createModernPaint(self,fill_color):
        canvas=Canvas(self.tk,width=400,height=400)
        canvas.pack()
        self.random_rectangle(canvas,400,400,fill_color)
        for x in range(0,100):
            self.random_rectangle(canvas,400,400,fill_color)
        self.tk.mainloop()
    def arc(self,rad):
        canvas=Canvas(self.tk,width=400,height=400)
        canvas.pack()
        canvas.create_arc(10,10,200,100,extent=rad,style=ARC)
        self.tk.mainloop()
    def shape(self):
        canvas=Canvas(self.tk,width=400,height=400)
        canvas.pack()
        canvas.create_polygon(200,10,240,30,120,100,100,140,fill="",outline="black")
        canvas.create_text(130,120,text="who are you ",fill='red',font=('Times',20))
        canvas.create_text(200,170,text="who are you ",fill='red',font=('Helvetica',20))
        self.tk.mainloop()
    def animation(self):
        canvas=Canvas(self.tk,width=400,height=400)
        canvas.pack()
        rt1=canvas.create_polygon(10,10,10,60,50,35)
        '''
        for i in range(0,60):                 #建立一个60次的循环 ，循环区间[0,59）
            canvas.move(1,5,0)              #canvas对象中的图形调用移动函数，x轴5个像素点，y轴不变
            self.tk.update()                           #更新框架，强制显示改变
            time.sleep(0.05)                   #睡眠0.05秒，制造帧与帧间的间隔时间
        for i in range(0,60):                                                   
            canvas.move(1,0,5)
            self.tk.update()
            time.sleep(0.05)
        for i in range(0,60):
            canvas.move(1,-5,0)
            self.tk.update()
            time.sleep(0.05)
        for i in range(0,60):
            canvas.move(1,0,-5)
            self.tk.update()
            time.sleep(0.05)
         '''  
        for i in range(0,60):
            canvas.move(rt1,5,5)
            self.tk.update()
            time.sleep(0.05)  
        for i in range(0,60):
            canvas.move(rt1,0,-5)
            self.tk.update()
            time.sleep(0.05) 
        for i in range(0,60):
            canvas.move(rt1,-5,5)
            self.tk.update()
            time.sleep(0.05)  
        for i in range(0,60):
            canvas.move(rt1,5,0)
            self.tk.update()
            time.sleep(0.05)
        for i in range(0,60):
            canvas.move(rt1,-5,-5)
            self.tk.update()
            time.sleep(0.05)    
        self.tk.mainloop()
    def bindEvent(self): #根据方向键箭头进行移动
        canvas=Canvas(self.tk,width=400,height=400)
        canvas.pack()
        canvas.create_polygon(10,10,10,60,50,35)
        #return为回车事件
        canvas.bind_all('<Right>',func=self.movetringle_adaptor(self.movetringle,canvas=canvas)) #参数为字典式，和主事件参数名一致，相当于委托事件
        canvas.bind_all('<Left>',func=self.movetringle_adaptor(self.movetringle,canvas=canvas))
        canvas.bind_all('<Up>',func=self.movetringle_adaptor(self.movetringle,canvas=canvas))
        canvas.bind_all('<Down>',func=self.movetringle_adaptor(self.movetringle,canvas=canvas))
        self.tk.mainloop()
    def movetringle(self,event,canvas):
        tt=event.keysym #可以根据绑定事件名作判断调用不同方法
        if(tt.lower()=='right'):
            canvas.move(1,5,0)    #1指第一个创建的对象。也可以代入实体。如上
        elif (tt.lower()=='left'):
            canvas.move(1,-5,0)
        elif (tt.lower()=='up'):
            canvas.move(1,0,-5)
        elif(tt.lower()=='down'):
            canvas.move(1,0,5)
    def movetringle_adaptor(self, fun,  **kwds): #定义字典式给参
        return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)
    

