from tkinter import *
tk = Tk()
canvas = Canvas(tk,width=400,height=400)
canvas.pack()

# 画圆弧
canvas.create_arc(10,10,200,100,extent=180,style=ARC)

# 画多边形
canvas.create_polygon(10,10,100,10,100,110,fill="",outline="black")  # 三角形
canvas.create_polygon(200,10,240,30,120,100,140,120,fill="",outline="black")  # 不规则多边形