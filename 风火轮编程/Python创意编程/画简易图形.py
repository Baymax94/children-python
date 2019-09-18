import turtle
def draw(t,length):
    """
    画三角形函数
    """
    t.begin_fill()
    for x in range(3):
        t.fd(length)
        t.left(120)
    t.end_fill()

# 设定海龟画笔和填充颜色
turtle.color('red','blue')

# 迭代x变量4次
for x in range(4):
    draw(turtle,100)
    turtle.fd(100)
    turtle.rt(90)
