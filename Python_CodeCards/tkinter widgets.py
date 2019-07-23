# tkinter widgets
from tkinter import *

# Create a window and add a title:
window = Tk()
window.title("My application")

my_canvas = Canvas(bg="green", height=50, width=100)
my_canvas.grid(row=0, column=0)

window.mainloop()