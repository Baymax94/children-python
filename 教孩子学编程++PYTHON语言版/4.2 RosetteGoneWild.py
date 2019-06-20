import turtle
t = turtle.Pen()
#Ask the user for the number of circles in their rosette, default to 6
number_of_circles = int(turtle.numinput("Number of circles","How many circles in your rosette?",6))
for x in range(number_of_circles):
    t.circle(100)
    t.circle(-50)
    t.left(360/number_of_circles)