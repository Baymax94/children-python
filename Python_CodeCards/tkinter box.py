# tkinter
# add a text entry box with a label
from tkinter import *

# Create a window and add a title:
window = Tk()
window.title("My application")

Label(window, text="Name:").grid(row=0, column=0)
my_text_box = Entry(window, width=10)
my_text_box.grid(row=0, column=1)

frame1 = Frame(window, height=20, width=50, bg="green")
frame1.grid(row=0, column=0)
frame2 = Frame(window, height=20, width=50, bg="red")
frame2.grid(row=1, column=1)

options = (1, 2, 3)
var = IntVar()
var.set("choose:")
my_dropdown = OptionMenu(window, var, *options)
my_dropdown.grid()

window.mainloop()