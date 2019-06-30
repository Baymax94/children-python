from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk,width=500,height=500)
canvas.pack()
# 注意坐标
canvas.create_line(0,0,500,500)  # 画线
canvas.create_rectangle(10,10,50,50)  # 画方块
canvas.create_rectangle(10,10,300,50)
canvas.create_rectangle(10,10,50,300)
# 画很多矩形
def random_rectangle(width,height):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1,y1,x2,y2)

# random_rectangle(500,500)

for x in range(0,100):
    random_rectangle(500,500)

# 画带颜色填充的矩形
def random_rectangle(width,height,fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1,y1,x2,y2,fill=fill_color)

random_rectangle(500,500,'green')
random_rectangle(500,500,'red')
random_rectangle(500,500,'blue')
random_rectangle(500,500,'yellow')

# 颜色选择器
# colorchooser.askcolor()