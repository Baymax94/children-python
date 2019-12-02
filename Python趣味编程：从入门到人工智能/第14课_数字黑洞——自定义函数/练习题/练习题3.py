'''
3.请完善程序，实现计算两点之间的距离。
'''
import math
def distance(x1, y1, x2=0, y2=0):
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    d = round(d, 2)
    return d

d = distance(3, 4)
print(d)
