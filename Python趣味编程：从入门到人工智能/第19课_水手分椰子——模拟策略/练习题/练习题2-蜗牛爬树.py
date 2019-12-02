'''
程序：蜗牛爬树
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》

提示：该题的编程思路可参考《Scratch趣味编程进阶》中的相同问题。
'''
import math

distance = 0
count = 0
while distance < 98:
    count += 1
    if count % 2 == 0:
        distance -= 7.8
    else:
        distance += 10

days = math.ceil(count / 2)
print('蜗牛爬到树顶要%d天' % days)
