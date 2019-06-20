import turtle  # Set up turtle graphics
t = turtle.Pen()
turtle.bgcolor("black")

#Set up a list of any 8 valid Python color names
colors = ["red","yellow","blue","green","orange","purple","white","gray"]

# Ask the user for the number of sides, between 1 and 8, with a default of 4
sides = int(turtle.numinput("Number of sides","How many sides do you want (1-8)?",4,1,8))

# Draw a colorful spiral with the user-specified number of sides
for x in range(360):
    # t.pencolor(colors[x%4])  # Rotate through the four colors
    # t.penup()  # Don't draw the regular spiral lines
    # t.forward(x*4)  # Just move the turtle on the screen
    # t.pendown()  # Write the user's name, bigger each time
    # t.write(your_name, font = ("Arial", int((x+4)/4),"bold"))
    # t.left(91)  # Turn left, just as in our other spirals
    t.pencolor(colors[x % sides])  # Only use the right number of colors
    t.forward(x * 3 / sides + x)  # Change the size to match number of sides
    t.left(360 / sides + 1)  # Turn 360 degrees/number of sides, plus 1
    t.width(x * sides / 200)  # Make the pen larger as it goes outward