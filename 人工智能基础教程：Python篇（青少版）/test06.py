# 百钱买百鸡问题
# x为公鸡数量；y为母鸡数量；z为雏鸡数量
x_max = int(100/5)
y_max = int(100/3)
for x in range(x_max):
    for y in range(y_max):
        z = 100 - x - y
        if(z%3==0)and(5*x+3*y+z/3==100):
            print("公鸡{0}只，母鸡{1}只，小鸡{2}只".format(x,y,z))
