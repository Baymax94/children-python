#四色螺旋线
import turtle
t = turtle.Pen()
#修改背景颜色
turtle.bgcolor("yellow")
colors = ["red","black","blue","green"]
#t.pencolor("green")
for x in range(100):
    t.pencolor(colors[x%4])
    #t.forward(x*5)
    t.circle(x)
    t.left(91)