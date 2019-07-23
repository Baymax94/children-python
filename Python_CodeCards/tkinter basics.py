# tkinter basics
from tkinter import *

# Create a window and add a title:
window = Tk()
window.title("My application")


def bye():
    my_label.config(text="Bye bye")


my_label = Label(window, text="Hello World")
my_label.grid(row=0, column=0)

my_button = Button(window, text="Start", command=bye)
my_button.grid(row=1, column=0)

# Other code goes here

# Start the infinite loop which watches for changes:
window.mainloop()