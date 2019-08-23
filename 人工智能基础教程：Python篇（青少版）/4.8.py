import turtle
t=turtle.Pen()
turtle.bgcolor("black")
name_str="['Leo','Lily','Tom','Alex','Max']"
name_list=eval(name_str)
colors=["yellow","green","white","brown","gray"]
for x in range(150):
    t.pencolor(colors[x % len(name_list)])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(name_list[x % len(name_list)],font=('Arial',int((x+4)/4)))
    t.left(360/len(name_list)+3)