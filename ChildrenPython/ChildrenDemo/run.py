
import TurtlePaint
import time
import TkPaint
import TkBall
import TkPanddle
from tkinter import*


if __name__=="__main__":
    #wash=TurtlePaint.Paint()
    #wash.sunFlower()
    #wash.drawSnake()
    #wash.fiveAngle()
    #wash.heart()
    #wash.bus()
    #tkp=TkPaint.Paint()
    #tkp.input("mary")
    #tkp.createLine()
    #tkp.createBox()
    #tkp.createModernPaint("grey")
    #tkp.arc(359) #359为整圆，360==0
    #tkp.shape()
    #tkp.animation()
    #tkp.bindEvent()
    #弹球
    tk=Tk()
    tk.title("Game")
    tk.resizable(0,0)#窗口在垂直和水平方向都不能改变
    tk.wm_attributes("-topmost",1)#画布窗口放在所有窗口之前
    canvas=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)#确保画布之外没有边框
    canvas.pack()
    tk.update()
    paddle=TkPanddle.Paddle(canvas,'green')
    ball=TkBall.Ball(canvas,paddle,'red')
    while 1:
        if ball.hit_bottom==False:
            ball.draw()
            paddle.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
    tk.mainloop()
    
    
   
    
    
    
