import turtle
t = turtle.Pen()
colors = ["red","black","blue","green","yellow","orange"]
for x in range(6):
    t.pencolor(colors[x%6])
    t.circle(100)
    t.left(60)