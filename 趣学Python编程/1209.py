from tkinter import *
tk = Tk()
canvas = Canvas(tk,width=500,height=500)
canvas.pack()
my_image = PhotoImage(file='D:\\Users\\Baymax\\Desktop\\child03\\12\\001.gif')
canvas.create_image(0,0,anchor=NW,image=myimage)