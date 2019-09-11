import turtle
turtle.Screen()
turtle.shape("turtle")
# 设置画笔属性
turtle.pensize(3)
turtle.pencolor("red")
turtle.fillcolor("yellow")

turtle.begin_fill()

# 重复5次“向前运动200像素，顺时针转动144°”
for _ in range(5):
    turtle.forward(200)
    turtle.right(144)

turtle.end_fill()

# 抬起画笔，回到原点（0,0）
turtle.penup()
turtle.goto(0, 0)
