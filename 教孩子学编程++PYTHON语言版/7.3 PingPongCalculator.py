def convert_in2cm(inches):
    return inches * 2.54

def convert_lb2kg(pounds):
    return pounds / 2.2

height_in = int(input("Enter your height in inches: "))
weight_lb = int(input("Enter your weight in pounds: "))

height_cm = convert_in2cm(height_in)
weight_kg = convert_lb2kg(weight_lb)

ping_pong_tall = round(height_cm / 4)
ping_pong_heavy = round(weight_kg * 1000 / 2.7)

feet = height_in // 12
inch = height_in % 12

print("At",feet,"feet",inch,"inches tall, and",weight_lb,"pounds,")
print("you messure",ping_pong_tall,"Ping_pong balls tall, and ")
print("you weight the same as", ping_pong_heavy,"Ping-Pong balls!")