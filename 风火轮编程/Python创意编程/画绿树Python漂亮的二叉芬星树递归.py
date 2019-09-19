from turtle import *
from coloradd import *


def draw_tree(t, n, distance):
    # 画二叉树的函数
    if n > 0:
        t.fd(distance)
        t.left(45)
        draw_tree(t, n-1, distance-20)
        t.right(90)
        draw_tree(t, n-1, distance-20)
        t.left(45)
        t.bk(distance)


screen = Screen()
screen.colormode(255)
screen.title("画绿树")
screen.tracer(0)

t = Turtle(visible=False)
t.left(90)
t.bk(100)

color = (29, 195, 10)
width = 100

<
div id = "rml_fade_content" style = "position: absolute";
bottom: 0em;
width: 100 %;
height: 10em;
background: -webkit-linear-gradient(rgba(255, 255, 255, 0)0 %,  # ffffff  100%);
background-image: -moz-linear-gradient(rgba(255, 255, 255, 0)0 %,  # ffffff  100%);
background-image: -o-linear-gradient(rgba(255, 255, 255, 0)0 %,  # ffffff  100%);
background-image: linear-gradient(rgba(255, 255, 255, 0)0 %,  # ffffff  100%);
background-image: -ms-linear-gradient(rgba(255, 255, 255, 0)0 %,  # ffffff  100%);
>
</div >
