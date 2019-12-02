'''
程序：求三角形周长
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
import math
c = 100
a = math.sin(math.radians(35)) * c
b = math.cos(math.radians(35)) * c
d = int(a + b + c)
print(d)
