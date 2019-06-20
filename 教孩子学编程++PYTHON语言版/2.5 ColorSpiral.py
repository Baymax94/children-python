#变量搞定螺旋线
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
# You can choose between 2 and 6 sides for some cool shapes!
#sides = 6
# 自定义边数
# eval() 函数用来执行一个字符串表达式，并返回表达式的值
sides = eval(input("Enter a number of sides between 2 and 6: \n"))
colors = ["red","yellow","blue","orange","green","purple"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    #width钢笔宽度
    t.width(x*sides/200)