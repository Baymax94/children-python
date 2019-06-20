# SayMyName.py - prints a screen full of the user's name

# Ask the user for their name
name = input("What is your name? \n")

# Print their name 100 times
for x in range(100):
    # Print their name followed by a space, not a new line
    print(name, end = " ")