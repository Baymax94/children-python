import turtle
t = turtle.Pen()
colors = ["red","black","blue","green"]
for x in range(4):
    t.pencolor(colors[x%4])
    t.circle(100)
    t.left(90)