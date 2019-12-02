'''
程序：几何拼贴画
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
from turtle import *
ht()
#调整绘图速度，取值为：slowest, slow, normal, fast, fastest
speed('slow')

#大地，画一条长为800像素的线段，画笔大小50像素，填充颜色'LightGreen'
pensize(50);pencolor('LightGreen')
up();goto(-400, -200);down();goto(400, -200)

#栅栏，画笔大小20像素，填充颜色'GoldEnrod'
pensize(20);pencolor('GoldEnrod')
up();goto(-400, -150);down();goto(400, -150)
up();goto(-250, -200);down();goto(-250, -100)
up();goto(-100, -200);down();goto(-100, -100)
up();goto(30, -200);down();goto(30, -100)
up();goto(300, -200);down();goto(300, -100)

#树干，画一条长为80像素的线段，画笔大小30像素，填充颜色'Olive'
pensize(30);pencolor('Olive')
up();goto(-150, -200);down();goto(-150, -120)

#树冠，分别以半径为80、60和40画出圆的内切正3边形，填充颜色'ForestGreen'
pensize(1);color('ForestGreen')
up();goto(-80, -120);down()
begin_fill();seth(60);circle(80, steps=3);end_fill()
up();goto(-95, -50);down()
begin_fill();seth(60);circle(60, steps=3);end_fill()
up();goto(-110, 0);down()
begin_fill();seth(60);circle(40, steps=3);end_fill()

#房子的墙体，画一个边长为200像素的正方形，填充颜色'RoyalBlue'
pensize(1);color('RoyalBlue')
up();home();fd(70);right(90);down()
begin_fill();fd(200);left(90);fd(200);left(90);fd(200);end_fill()

#烟囱，画一条长90像素的线段，画笔大小30像素，填充颜色'DimGray'
pensize(30);pencolor('DimGray');
up();goto(230, 30);down();goto(230, 120)

#房顶，画一个底角为30度、腰为200像素的等腰三角形，填充颜色'DeepPink'
pensize(1);color('DeepPink');up();home();down()
begin_fill();left(30);fd(200);right(60);fd(200);home();end_fill()

#窗户，画一个半径为50像素的圆的内切正4边形，填充颜色'Violet'
color('Violet');up();goto(160, -90);down()
begin_fill();seth(45);circle(50, steps=4);end_fill()

#门，画一个长120像素、宽60像素的长方形，填充颜色'Chocolate'
color('Chocolate');up();goto(250, -200);down();seth(90)
begin_fill()
fd(120);left(90);fd(60);left(90);fd(120);left(90);fd(60)
end_fill()

#炊烟，画3个依次变小的圆点，填充颜色'AliceBlue'
up();goto(250, 160);dot(30, 'AliceBlue')
goto(270, 200);dot(20, 'AliceBlue')
goto(300, 220);dot(10, 'AliceBlue')

#太阳，画一个80像素的圆点，填充颜色'Gold'
goto(-260, 250);dot(80, 'Gold')
