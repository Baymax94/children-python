# 趣味练习，绘图
import turtle
t=turtle.Pen()
for x in range(6):
    t.circle(100)
    t.left(60)

answer = input("Do you want to see a spiral?")
if answer == 'y':
    print("Working……")
    t.width(2)
    for x in range(100):
        t.forward(x*2)
        t.left(88)
else:
    print("What a pity!")
print("Done!")