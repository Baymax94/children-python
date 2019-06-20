import random
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red","yellow","blue","green","orange","purple","white","gray"]
for n in range(50):
    # Generate spirals of random sizes/colors at random locations
    t.pencolor(random.choice(colors))          # Pick a random color
    size = random.randint(10,40)               # Pick a random spiral size
    # Generate a random (x,y) location on the screen
    x = random.randrange(0,turtle.window_width()//2)
    y = random.randrange(0,turtle.window_height()//2)
    # First spiral
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)
    # Second spiral
    t.penup()
    t.setpos(-x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)
    # Third spiral
    t.penup()
    t.setpos(-x,-y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)
    # Fourth spiral
    t.penup()
    t.setpos(x,-y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)