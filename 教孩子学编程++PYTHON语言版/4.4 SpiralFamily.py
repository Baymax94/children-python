import turtle  # Set up turtle graphics
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red","yellow","blue","green","orange","purple","white","brown","gray","pink"]

# Ask the user's name using turtle's textinput pop-up window
# your_name = turtle.textinput("Enter your name","What is your name?")

family = []  # Set up an empty list for family names

# Ask for the first name
name = turtle.textinput("My family","Enter a name, or just hit [ENTER] to end:")
# Keep asking for names
while name != "":
    # Add their name to the family list
    family.append(name)
    # Ask for another name, or end
    name = turtle.textinput("My family","Enter a name, or just hit [ENTER] to end:")

# Draw a spiral of the name on the screen, written 100 times
for x in range(100):
    t.pencolor(colors[x%len(family)])  # Rotate through the colors
    t.penup()  # Don't draw the regular spiral lines
    t.forward(x*4)  # Just move the turtle on the screen
    t.pendown()  # Write the user's name, bigger each time
    t.write(family[x%len(family)], font = ("Arial", int((x+4)/4),"bold"))
    t.left(360/len(family) + 2)  # Turn left, just as in our other spirals