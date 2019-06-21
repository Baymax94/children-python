import turtle 
import time
class Paint:
    def sunFlower(self):
        t=turtle.Pen()
        t.color("red","yellow")
        t.speed(10)
        t.begin_fill()
        forwardLen=200
        leftLen=170
        for _ in range(50):
            t.forward(forwardLen)
            t.left(leftLen)
        t.end_fill()
            
    def drawSnake(self):
        turtle.setup(1500, 1400, 0, 0)
        t=turtle.Pen()
        t.pensize(30)
        t.pencolor("green")
        t.speed(1)
        t.seth(270) # 前进的方向0east,90north
        rad=70
        angle=80
        len=2
        neckrad=15
        for _ in range(len):
            t.circle(rad, angle)
            t.circle(-rad, angle)
        t.circle(rad, angle/2)
        t.forward(rad/2)  # 直线前进
        t.circle(neckrad, 180)
        t.forward(rad/4)

    def fiveAngle(self):
        turtle.pensize(5)
        turtle.color("yellow","red")
        turtle.begin_fill()

        for _ in range(5):
            turtle.forward(200)
            turtle.right(144)
        turtle.end_fill()
       # time.sleep(2)

        turtle.penup()
        turtle.goto(-150,-120)
        turtle.color("violet")
        turtle.write("Done", font=('Arial', 40, 'normal'))
        time.sleep(1)
    
    def curvemove(self):
        for _ in range(200):
            turtle.right(1)
            turtle.forward(1)

    def heart(self):
        turtle.color('red','pink')
        turtle.begin_fill()
        turtle.left(140)
        turtle.forward(111)
        self.curvemove()
        turtle.left(120)
        self.curvemove()
        turtle.forward(111)
        turtle.end_fill()
        turtle.done()
    def bus(self):
        t=turtle.Pen()
        t.color("yellow","red")
        t.begin_fill()
        t.forward(100)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.forward(60)
        t.left(90)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.end_fill()
        t.color("black","black")
        t.up()
        t.forward(10) #并不进行画线
        t.down()
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        t.setheading(0) #方向
        t.up()
        t.forward(70)
        t.right(90)#调整偏移度
        t.down()
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        time.sleep(10)