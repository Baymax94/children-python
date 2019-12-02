'''
程序：冰雹猜想
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
n = int(input('请输入一个正整数:'))
state = True
while state:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print(n)
    if n == 1: 
        state = False  #让循环结束
