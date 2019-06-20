import turtle
t = turtle.Pen()
# Ask the user for the number of sides or cicles, default to 6
number = int(turtle.numinput("Number of sides or circles","How many sides or circles in your shape?",6))
# Ask the user whether they want a polygon or rosette
shape = turtle.textinput("Which shape do you want","Enter 'p' for polygon or 'r' for rosette:")
for x in range(number):
    if shape == 'r':  # User selected rosette
        t.circle(100)
    else:             # Default to polygon
        t.forward(150)
    t.left(360/number)