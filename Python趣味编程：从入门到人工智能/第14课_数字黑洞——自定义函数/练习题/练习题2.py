'''
2.请完善程序，实现计算圆的周长和面积。
'''
def circle(r):
    d = round(3.14 * r * 2, 2)
    s = round(3.14 * r * r, 2)
    return (d, s)
    
(d, s) = circle(3)
print(d, s)
