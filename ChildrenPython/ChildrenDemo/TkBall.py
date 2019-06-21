from tkinter import *
import random
import time
class Ball:
    def __init__(self,canvas,paddle,color): #用self作全局变量
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        starts=[-3,-2,-1,1,2,3]#让x开始的坐标为列表里的任意一个坐标
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-3
        self.canvas_width=canvas.winfo_width()#获取画布当前的宽度
        self.canvas_height=canvas.winfo_height()#获取画布当前的高度
        self.hit_bottom=False
    def hit_paddle(self,pos):#击打函数，pos是小球的坐标
        paddle_pos=self.canvas.coords(self.paddle.id)#获取球拍的位置
        #pos[0]小球左边pos[1]小球顶部post[2]小球右边pos[3]小球底部
        #if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:#小球右侧大于球拍左侧且小球左侧小于球拍右侧,
        if pos[0]>=paddle_pos[0] and pos[2]<=paddle_pos[2]:#小球左边比拍子大，右边比拍子小
            if pos[3]>=paddle_pos[1]and pos[3]<=paddle_pos[3]:
                return True
        return False
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)#用来传入画布上任何画好的东西的坐标（四个坐标）
        if pos[1]<=0:#判断Y1坐标（即小球的顶部）是否小于等于0，成立即不再减少
            self.y=3
        if pos[3]>=self.canvas_height:#判断Y2坐标（即小球的底部）是否大于画布高度，成立也往回走
            self.hit_bottom=True
        if self.hit_paddle(pos)==True:
            self.y=-3
        if pos[0]<=0:
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3