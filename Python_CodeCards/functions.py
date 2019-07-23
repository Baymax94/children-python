# functions
def add_two_numbers(a, b):
    print(a + b)


add_two_numbers(3, 4)

# Calling a function from the keyboard in tkinker
# bind up arrow to the move_up() function:
'''
import tkinter
window.bind("<Up>", move_up)
'''

# random numbers:
import random
dice_number = random.randint(1, 6)
print(dice_number)