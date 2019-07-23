# using images
from tkinter import *
window = Tk()

# build a canvas:
canvas = Canvas(window, bg="beige", height=100, width=100)
canvas.grid(row=0, column=0)

# add an image:
# cat = PhotoImage(file="C:\Users\LejuRobot\Desktop\少儿python\超能陆战队.jpg")
# cat = PhotoImage(file="C:/Users/LejuRobot/Desktop/少儿python/超能陆战队.jpg")
cat = PhotoImage(file="C:/Users/LejuRobot/Desktop/001.jpg")
canvas.create_image(20, 40, image=cat, anchor=NW)

window.mainloop()
