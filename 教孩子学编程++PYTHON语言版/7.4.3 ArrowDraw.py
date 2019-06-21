import turtle
t = turtle.Pen()
t.speed(0)
t.turtlesize(2,2,2)
def up():
    t.forward(50)
def left():
    t.left(90)
def right():
    t.right(90)
turtle.onkeypress(up,"Up")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")
turtle.listen()