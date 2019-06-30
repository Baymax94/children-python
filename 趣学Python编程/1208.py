from tkinter import *
tk = Tk()
tk = Tk()
canvas = Canvas(tk,width=500,height=500)
canvas.pack()

# 显示文字
canvas.create_text(150,100,text='There once was a man from Toulouse',fill='red')

# 制定字体名和字体大小
# eg. font=('Times',15);font=('Helvetica',20)······
canvas.create_text(220,300,text='There once was a man from Toulouse',font=('Courier',30))